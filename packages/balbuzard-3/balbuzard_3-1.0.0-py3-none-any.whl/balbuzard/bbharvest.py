#! /usr/bin/env python3
"""
bbharvest

bbharvest is a tool to analyse malware that uses obfuscation such as XOR, ROL,
ADD (and many combinations) to hide information such as IP addresses, domain
names, URLs, strings, embedded files, etc. It is targeted at malware
using several obfuscation transforms and/or several keys in a single file.
It tries all possible keys of selected transforms and extracts all patterns of
interest using the balbuzard engines.
It is part of the Balbuzard package.

Author: Philippe Lagadec
Maintainer: Corey Forman (digitalsleuth)
License: BSD, see source code or documentation

Project Repository: https://github.com/digitalsleuth/balbuzard
"""

# LICENSE:
#
# bbharvest is copyright (c) 2013-2019, Philippe Lagadec (http://www.decalage.info)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# ------------------------------------------------------------------------------
# CHANGELOG:
# 2013-03-15       PL: - harvest mode in bbcrack: run all transforms, extract all
#                        significant patterns
# 2013-12-06 v0.01 PL: - moved harvest code from bbcrack to bbharvest
# 2013-12-08 v0.02 PL: - added CSV output, renamed multi_trans to harvest
# 2013-12-09 v0.03 PL: - merged patterns list with balbuzard in patterns.py
# 2014-01-04 v0.04 PL: - use functions from bbcrack to simplify main
#                      - added -i option for incremental level
# 2014-01-06 v0.05 PL: - added the possibility to write transform plugins
# 2019-06-16 v0.20 PL: - added main function for pip entry points (issue #8)
# 2024-12-03 v1.0.0 CF: - Ported all code to Python 3

__version__ = "1.00"

# ------------------------------------------------------------------------------
# TODO:
# + option to save copy of every matching file
# + csv output for profiling mode
# + main: same fix as balbuzard for fname in zip


# --- IMPORTS ------------------------------------------------------------------

import sys
import time
import argparse
import csv
from operator import attrgetter

try:
    from bbcrack import load_plugins, list_transforms, read_file, select_transforms
    from bbpatterns import harvest_patterns
    from balbuzard import Balbuzard
except (ImportError, ModuleNotFoundError):
    from balbuzard.bbcrack import load_plugins, list_transforms, read_file, select_transforms
    from balbuzard.bbpatterns import harvest_patterns
    from balbuzard.balbuzard import Balbuzard


# --- PATTERNS -----------------------------------------------------------------


# --- FUNCTIONS ----------------------------------------------------------------


def harvest(raw_data, transform_classes, filename, profiling=False, csv_writer=None):
    """
    apply all transforms to raw_data, and extract all patterns of interest
    (Slow, but useful when a file uses multiple transforms.)
    """
    print("*** WARNING: harvest mode may return a lot of false positives!")
    # here we only want to extract patterns of interest
    bbz = Balbuzard(harvest_patterns)
    if not profiling:
        for Transform_class in transform_classes:
            # iterate over all possible params for that transform class:
            for params in Transform_class.iter_params():
                # instantiate a Transform object with these params
                transform = Transform_class(params)
                msg = f"transform {transform.shortname}          \r"
                print(msg, end=" ")
                # transform data:
                data = transform.transform_string(raw_data)
                # search each pattern in transformed data:
                for pattern, matches in bbz.scan(data):
                    for index, match in matches:
                        if len(match) > 3:
                            # limit matched string display to 50 chars:
                            m = repr(match)
                            if len(m) > 50:
                                m = f"{m[:24]}...{m[-23:]}"
                            print(
                                f"{transform.shortname}: at {index:08X} {pattern.name}, string={m}"
                            )
                            if csv_writer is not None:
                                # ['Filename', 'Transform', 'Index', 'Pattern name', 'Found string', 'Length']
                                csv_writer.writerow(
                                    [
                                        filename,
                                        transform.shortname,
                                        f"0x{index:08X}",
                                        pattern.name,
                                        m,
                                        len(match),
                                    ]
                                )
        print("                                      ")
    else:
        # same code, with profiling:
        count_trans = 0
        count_patterns = 0
        start_time = time.process_time()
        for Transform_class in transform_classes:
            # iterate over all possible params for that transform class:
            for params in Transform_class.iter_params():
                count_trans += 1
                # instantiate a Transform object with these params
                transform = Transform_class(params)
                msg = f"transform {transform.shortname}          \r"
                print(msg, end=" ")
                # transform data:
                start_trans = time.process_time()
                data = transform.transform_string(raw_data)
                transform.time = time.process_time() - start_trans
                # search each pattern in transformed data:
                for pattern, matches in bbz.scan_profiling(data):
                    count_patterns += 1
                    for index, match in matches:
                        if len(match) > 3:
                            print(
                                f"{transform.shortname}: {pattern.name} at index {index:X}, string={repr(match)}"
                            )
                if count_trans % 10 == 0:
                    t = time.process_time() - start_time
                    print(
                        f"PROFILING: {count_trans} transforms in {t:.1f}s, {((t * 1000) / count_trans):.2f} ms/trans"
                    )
                    for pattern in sorted(
                        bbz.patterns, key=attrgetter("total_time"), reverse=True
                    ):
                        print(
                            f"- {pattern.name}: {100 * pattern.total_time / t:.1f}%, total time = {pattern.total_time}s"
                        )
        print(" " * 38)


# === MAIN =====================================================================


def main():
    usage = "%(prog)s [options] <filename>"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument(
        "file",
        help="filename",
        nargs="*",
    )
    parser.add_argument(
        "-l",
        "--level",
        dest="level",
        default=1,
        type=int,
        help="select transforms level 1, 2 or 3",
    )
    parser.add_argument(
        "-i",
        "--inclevel",
        dest="inclevel",
        default=None,
        help="select transforms only with level 1, 2 or 3 (incremental)",
    )
    parser.add_argument("-c", "--csv", dest="csv", help="export results to a CSV file")
    parser.add_argument(
        "-t",
        "--transform",
        dest="transform",
        default=None,
        help='only check specific transforms (comma separated list, or "-t list" to display all available transforms)',
    )
    parser.add_argument(
        "-z",
        "--zip",
        dest="zip_password",
        default=None,
        help="if the file is a zip archive, open first file from it, using the provided password (requires Python 2.6+)",
    )
    parser.add_argument(
        "-p",
        action="store_true",
        dest="profiling",
        help="profiling: measure time spent on each pattern.",
    )

    args = parser.parse_args()

    # load transform plugins
    load_plugins()

    # if option "-t list", display list of transforms and quit:
    if args.transform == "list":
        list_transforms()

    # Print help if no argurments are passed
    if len(sys.argv[1:]) == 0:
        print(__doc__)
        parser.print_help()
        sys.exit()

    for fname in args.file:
        raw_data = read_file(fname, args.zip_password)
    
        transform_classes = select_transforms(
            level=args.level,
            incremental_level=args.inclevel,
            transform_names=args.transform,
        )
    
        # open CSV file
        if args.csv:
            print(f"Writing output to CSV file: {args.csv}")
            with open(args.csv, "w", newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(
                    ["Filename", "Transform", "Index", "Pattern name", "Found string", "Length"]
                )
        else:
            csv_writer = None
        harvest(
            raw_data,
            transform_classes,
            fname,
            profiling=args.profiling,
            csv_writer=csv_writer,
        )


if __name__ == "__main__":
    main()

# This was coded while listening to Mogwai "The Hawk Is Howling".
