#! /usr/bin/env python3
"""
balbuzard

Balbuzard is a tool to quickly extract patterns from suspicious files for
malware analysis (IP addresses, domain names, known file headers and strings,
etc).

Author: Philippe Lagadec
Maintainer: Corey Forman (digitalsleuth)
License: BSD, see source code or documentation

Project Repository: https://github.com/digitalsleuth/balbuzard
"""

# LICENSE:
#
# balbuzard is copyright (c) 2007-2019, Philippe Lagadec (http://www.decalage.info)
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
# 2007-07-11 v0.01 PL: - 1st version
# 2007-07-30 v0.02 PL: - added list of patterns
# 2007-07-31 v0.03 PL: - added patterns
#                        - added hexadecimal dump
# 2007-08-09 v0.04 PL: - improved some regexs, added Petite detection
# 2008-06-06 v0.05 PL: - escape non-printable characters with '\xNN' when
#                          displaying matches
#                      - optional custom pattern list in reScan_custom.py
#                      - optional call to magic.py to guess filetype
# 2011-05-06 v0.06 PL: - added bruteforce functions
# 2013-02-24 v0.07 PL: - renamed rescan to balbuzard
#                      - changed license from CeCILL v2 to BSD
#                      - added patterns for URL, e-mail, Flash
#                      - new Pattern class to add patterns
#                      - pattern can now be a regex or a string, with weigth
#                      - moved bruteforce functions to balbucrack
# 2013-03-18 v0.08 PL: - a few more/improved patterns
#                      - optionparser with option -s for short display
# 2013-03-21 v0.09 PL: - open file from password-protected zip (inspired from
#                        Didier Steven's pdfid, thanks Didier! :-)
#                      - improved plugin system
# 2013-03-26 v0.10 PL: - improved Pattern and Pattern_re classes
# 2013-07-31 v0.11 PL: - added support for Yara plugins
# 2013-08-28 v0.12 PL: - plugins can now be in subfolders
#                      - improved OLE2 pattern
# 2013-12-03 v0.13 PL: - moved patterns to separate file patterns.py
#                      - fixed issue when balbuzard launched from another dir
#                      - added CSV output
# 2013-12-04 v0.14 PL: - can now scan several files from command line args
#                      - now short display is default, -v for hex view
# 2013-12-09 v0.15 PL: - Pattern_re: added filter function to ignore false
#                        positives
# 2014-01-14 v0.16 PL: - added riglob, ziglob
#                      - new option -r to find files recursively in subdirs
#                      - new option -f to find files within zips with wildcards
# 2014-01-23 v0.17 PL: - Pattern: added partial support for filter function
# 2014-02-24 v0.18 PL: - fixed bug with main_dir when balbuzard is imported
# 2014-03-21 v0.19 PL: - fixed bug when Yara-python is not installed
# 2014-06-29 v0.20 PL: - simplified bbcrack transforms, added Yara signatures
# 2019-06-16       PL: - added main function for pip entry points (issue #8)
# 2024-12-03 v1.0.0 CF: - Ported all code to Python 3

__version__ = "1.00"


# ------------------------------------------------------------------------------
# TODO:
# + add yara plugins support to Balbuzard.count and scan_profiling
# + merge Balbuzard.scan_hexdump and short
# + option to choose which plugins to load: all (default), none, python or yara
#   only
# + option to use the Yara-python engine for searching (translating balbuzard
#   patterns to yara at runtime)
# - Yara plugins: keep track of the filename containing each set of Yara rules
# - option to support Unicode strings? (need to check 2 alignments and 2 byte
#   orders, or simply insert \x00 between all chars, e.g. 'T\x00E\x00S\x00T')
# + improve patterns to avoid some false positives: maybe use pefile or magic.py ?
# - HTML report with color highlighting
# - GUI ?
# - optional use of other magic libs (TrIDscan, pymagic, python-magic, etc: see PyPI)
# - provide samples
# - RTF hex object decoder?
# - option to decode stream before searching: unicode, hex, base64, etc
# - options for XML outputs
# - export to OpenIOC?
# ? zip file: open all files instead of only the 1st one, or add an option to
#   specify the filename(s) to open within the zip, with wildcards?


# ISSUES:
# - BUG: it seems that re ignores null bytes in patterns, despite what the doc says?
# - BUG: the URL pattern is not fully correct, need to find a better one
# - BUG: the e-mail pattern catches a lot of false positives.


# --- IMPORTS ------------------------------------------------------------------

import sys
import re
import os
import os.path
import argparse
import glob
import zipfile
import time
import fnmatch
import csv

if os.sys.platform != 'win32':
    try:
        import magic

        MAGIC = True
    except (ImportError, ModuleNotFoundError):
        MAGIC = False

else:
    try:
        from winmagic import magic

        MAGIC = True
    except (ImportError, ModuleNotFoundError):
        MAGIC = False

try:
    import yara

    YARA = True
except (ImportError, ModuleNotFoundError):
    YARA = False

try:
    from bbpatterns import Pattern, Pattern_re, patterns
except (ImportError, ModuleNotFoundError):
    from balbuzard.bbpatterns import Pattern, Pattern_re, patterns

MAIN_DIR = os.path.dirname(__file__)
PLUGINS_DIR = os.path.join(MAIN_DIR, "plugins")


# ------------------------------------------------------------------------------
class Balbuzard(object):
    """
    class to scan a string of data, searching for a set of patterns (strings
    and regular expressions)
    """

    def __init__(self, patterns=None, yara_rules=None):
        self.patterns = patterns
        if patterns is None:
            self.patterns = []
        self.yara_rules = yara_rules


    def scan(self, data):
        """
        Scans data for all patterns. This is an iterator: for each pattern
        found, yields the Pattern object and a list of matches as tuples
        (index in data, matched string).
        """
        # prep lowercase version of data for case-insensitive patterns
        data_lower = data.lower()
        for pattern in self.patterns:
            matches = pattern.find_all(data, data_lower)
            if len(matches) > 0:
                yield pattern, matches
        if YARA and self.yara_rules is not None:
            for rules in self.yara_rules:
                yara_matches = rules.match(data=data)
                for match in yara_matches:
                    # create a fake pattern object, with a single match:
                    pattern = Pattern(match.rule)
                    matches = []
                    for s in match.strings:
                        offset, _, d = s
                        matches.append((offset, d))
                    yield pattern, matches

    def scan_profiling(self, data):
        """
        Scans data for all patterns. This is an iterator: for each pattern
        found, yields the Pattern object and a list of matches as tuples
        (index in data, matched string).
        Version with profiling, to check which patterns take time.
        """
        start = time.process_time()
        # prep lowercase version of data for case-insensitive patterns
        data_lower = data.lower()
        for pattern in self.patterns:
            start_pattern = time.process_time()
            matches = pattern.find_all(data, data_lower)
            pattern.time = time.process_time() - start_pattern
            pattern.total_time += pattern.time
            if len(matches) > 0:
                yield pattern, matches
        self.time = time.process_time() - start

    def count(self, data):
        """
        Scans data for all patterns. This is an iterator: for each pattern
        found, yields the Pattern object and the count as int.
        """
        # prep lowercase version of data for case-insensitive patterns
        data_lower = data.lower()
        for pattern in self.patterns:
            count = pattern.count(data, data_lower)
            if count:
                yield pattern, count

    def scan_display(
        self, data, filename, hexdump=False, csv_writer=None, long_strings=False
    ):
        """
        Scans data for all patterns, displaying an hexadecimal dump for each
        match on the console (if hexdump=True), or one line for each
        match (if hexdump=False).
        """
        results = []
        for pattern, matches in self.scan(data):
            for index, match in matches:
                if isinstance(match, bytes) and match.isascii():
                    match = match.decode('latin-1')
                m = repr(match)
                if len(m) > 50 and not long_strings:
                    m = f"{m[:24]}...{m[-23:]}"
                results.append([index, pattern.name, m, len(match)])
        results = sorted(results, key=lambda x:x[0])
        for entry in results:
            index, pattern_name, m, match_len = entry
            if hexdump:
                print("-" * 79)
                print(f"{pattern_name}:")
                print(f"{index:08X}: {m}")
                # 5 lines of hexadecimal dump around the pattern: 2 lines = 32 bytes
                start = max(entry[0] - 32, 0) & 0xFFFFFFF0
                index_end = index + len(match)
                end = min(index_end + 32 + 15, len(data)) & 0xFFFFFFF0
                length = end - start
                print(hexdump3(data[start:end], length=16, startindex=start))
                print("")
             
            else:
                print(f"{index:08X}: {pattern_name} - {m}")
            if csv_writer is not None:
                csv_writer.writerow(
                    [filename, f"0x{index:08X}", pattern_name, m, match_len]
                )
        # blank line between each file:
        print("")



# --- FUNCTIONS ----------------------------------------------------------------


# HEXDUMP from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/142812

# my improved hexdump, to add a start index:
def hexdump3(src, length=8, startindex=0):
    """
    Returns a hexadecimal dump of a binary string.
    length: number of bytes per row.
    startindex: index of 1st byte.
    """
    FILTER = "".join([(len(repr(chr(x))) == 3) and chr(x) or "." for x in range(256)])
    result = []
    for i in range(0, len(src), length):
        s = (src[i : i + length])
        hexa = " ".join([f"{x:02X}" for x in s])
        s = s.decode('latin-1')
        printable = s.translate(FILTER)
        result.append(f"{i+startindex:04X}   {hexa:<{(length * 3)}}   {printable}\n")
    return "".join(result)


# recursive glob function to find plugin files in any subfolder:
# inspired by http://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python
def rglob(path, pattern="*.*"):
    """
    Recursive glob:
    similar to glob.glob, but finds files recursively in all subfolders of path.
    path: root directory where to search files
    pattern: pattern for filenames, using wildcards, e.g. *.txt
    """
    # TODO: more compatible API with glob: use single param, split path from pattern
    return [
        os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(path)
        for f in fnmatch.filter(files, pattern)
    ]


def riglob(pathname):
    """
    Recursive iglob:
    similar to glob.iglob, but finds files recursively in all subfolders of path.
    pathname: root directory where to search files followed by pattern for
    filenames, using wildcards, e.g. *.txt
    """
    path, filespec = os.path.split(pathname)
    for dirpath, _, files in os.walk(path):
        for f in fnmatch.filter(files, filespec):
            yield os.path.join(dirpath, f)


def ziglob(zipfileobj, pathname):
    """
    iglob in a zip:
    similar to glob.iglob, but finds files within a zip archive.
    - zipfileobj: zipfile.ZipFile object
    - pathname: root directory where to search files followed by pattern for
    filenames, using wildcards, e.g. *.txt
    """
    files = zipfileobj.namelist()
    for f in files:
        print(f)
    yield from fnmatch.filter(files, pathname)


def iter_files(files, recursive=False, zip_password=None, zip_fname="*"):
    """
    Open each file provided as argument:
    - files is a list of arguments
    - if zip_password is None, each file is opened and read as-is. Wilcards are
      supported.
    - if not, then each file is opened as a zip archive with the provided password
    - then files matching zip_fname are opened from the zip archive
    Iterator: yields (filename, data) for each file
    """
    # choose recursive or non-recursive iglob:
    if recursive:
        iglob = riglob
    else:
        iglob = glob.iglob
    for filespec in files:
        for filename in iglob(filespec):
            if zip_password is not None:
                # Each file is a zip archive:
                print(f"Opening zip archive {filename} with provided password")
                z = zipfile.ZipFile(filename, "r")
                print(f'Looking for file(s) matching "{zip_fname}"')
                for filename in ziglob(z, zip_fname):
                    print(f"Opening file in zip archive: {filename}")
                    data = z.read(filename, zip_password)
                    yield filename, data
            else:
                # normal file
                print(f"Opening file {filename}")
                with open(filename, "rb") as opened_file:
                    data = opened_file.read()
                    yield filename, data



# === MAIN =====================================================================

def main():

    usage = "%(prog)s [options] <filename>"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument(
        "file",
        help="filename",
        nargs="*",
    )
    parser.add_argument("-c", "--csv", dest="csv", help="export results to a CSV file")
    parser.add_argument(
        "-v",
        action="store_true",
        dest="verbose",
        help="verbose display, with hex view.",
    )
    parser.add_argument(
        "-r",
        action="store_true",
        dest="recursive",
        help="find files recursively in subdirectories.",
    )
    parser.add_argument(
        "-z",
        "--zip",
        dest="zip_password",
        default=None,
        help="if the file is a zip archive, open first file from it, using the provided password",
    )
    parser.add_argument(
        "-f",
        "--zipfname",
        dest="zip_fname",
        nargs="*",
        help="if the file is a zip archive, file(s) to be opened within the zip.",
    )
    parser.add_argument(
        "-l",
        "--long-strings",
        action="store_true",
        dest="long_strings",
        help="do not shorten strings found.",
    )

    args = parser.parse_args()

    # Print help if no argurments are passed
    if len(sys.argv[1:]) == 0:
        print(__doc__)
        parser.print_help()
        parser.exit()

    # load plugins
    for f in rglob(PLUGINS_DIR, "bbz*.py"):  # glob.iglob('plugins/bbz*.py'):
        print(f"Loading plugin from {os.path.relpath(f, PLUGINS_DIR)}")
        exec(compile(open(f, "rb").read(), f, "exec"))

    # load yara plugins
    if YARA:
        yara_rules = []
        for f in rglob(
            PLUGINS_DIR, "*.yar*"
        ):  # glob.iglob('plugins/*.yara'):  # or bbz*.yara?
            print(f"Loading yara rules from {os.path.relpath(f, PLUGINS_DIR)}")
            yara_rules.append(yara.compile(f))
    else:
        yara_rules = None

    #for fname in args.file:
    # open CSV file
    if args.csv:
        print(f"Writing output to CSV file: {args.csv}")
        csvfile = open(args.csv, "w", newline='')
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            ["Filename", "Index", "Pattern name", "Found string", "Length"]
        )
    else:
        csv_writer = None

    # scan each file provided as argument:
    for filename, data in iter_files(
        args.file, args.recursive, args.zip_password, args.zip_fname
    ):
        print("=" * 79)
        print(f"File: {filename}\n")
        if MAGIC:
            magic_object = magic.Magic(mime=True)
            print(f"Filetype according to magic: {magic_object.from_buffer(data)}\n")
        bbz = Balbuzard(patterns, yara_rules=yara_rules)
        bbz.scan_display(
            data,
            filename,
            hexdump=args.verbose,
            csv_writer=csv_writer,
            long_strings=args.long_strings,
        )

    # close CSV file
    if args.csv:
        csvfile.close()


if __name__ == "__main__":
    main()

# This was coded while listening to The National "Boxer".
