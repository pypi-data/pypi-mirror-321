#! /usr/bin/env python3
"""
bbtrans

bbtrans is a tool to apply a transform such as XOR, ROL, ADD (and many
combinations) to a file. This is useful to deobfuscate malware when the
obfuscation scheme is known, or to test bbcrack.
It is part of the Balbuzard package.

Author: Philippe Lagadec
Maintainer: Corey Forman (digitalsleuth)
License: BSD, see source code or documentation

Project Repository: https://github.com/digitalsleuth/balbuzard
"""
# LICENSE:
#
# bbtrans is copyright (c) 2013-2019, Philippe Lagadec (http://www.decalage.info)
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
# 2013-03-28 v0.01 PL: - first version
# 2013-12-09 v0.02 PL: - use hex for params instead of decimal
# 2014-01-20 v0.03 PL: - use function from bbcrack to list transforms
# 2019-06-16 v0.20 PL: - added main function for pip entry points (issue #8)
# 2024-12-03 v1.0.0 CF: - Ported all code to Python 3

__version__ = "1.00"

# ------------------------------------------------------------------------------
# TODO:
# + support wildcards and several files like balbuzard
# - option to choose output filename


import sys
import argparse
import zipfile
import os

try:
    from bbcrack import list_transforms, transform_classes_all
except (ImportError, ModuleNotFoundError):
    from balbuzard.bbcrack import list_transforms, transform_classes_all


def main():
    usage = "%(prog)s [options] <filename>"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument(
        "file",
        help="filename",
        nargs="*",
    )
    parser.add_argument(
        "-t",
        "--transform",
        dest="transform",
        default=None,
        help='transform to be applied (or "-t list" to display all available transforms)',
    )
    parser.add_argument(
        "-p",
        "--params",
        dest="params",
        default=None,
        help="parameters for transform (comma separated list)",
    )
    parser.add_argument(
        "-z",
        "--zip",
        dest="zip_password",
        default=None,
        help="if the file is a zip archive, open first file from it, using the provided password",
    )

    args = parser.parse_args()

    # if option "-t list", display list of transforms and quit:
    if args.transform == "list":
        list_transforms()

    # Print help if no argurments are passed
    if len(sys.argv[1:]) == 0 or args.transform is None:
        print(__doc__)
        parser.print_help()
        sys.exit()

    for fname in args.file:
        raw_data = None
        if args.zip_password is not None:
            # extract 1st file from zip archive, using password
            pwd = args.zip_password
            print(f'Opening zip archive {fname} with password "{pwd}"')
            with zipfile.ZipFile(fname, "r") as z:
            #z = zipfile.ZipFile(fname, "r")
                print(f"Opening first file: {z.infolist()[0].filename}")
                raw_data = z.read(z.infolist()[0], pwd)
        else:
            # normal file
            print(f"Opening file {fname}")
            #f = open(fname, "rb")
            with open(fname, "rb") as f:
                raw_data = f.read()
            #f.close()
    
    
        params = args.params.split(",")
        # params = map(int, params) # for decimal params
        # convert hex params to int:
        for i in range(len(params)):
            params[i] = int(params[i], 16)
        if len(params) == 1:
            params = params[0]
        else:
            params = tuple(params)
    
        for Transform_class in transform_classes_all:
            if Transform_class.gen_id == args.transform:
                print(f"Transform class: {Transform_class.gen_name}")
                print(f"Params: {params}")
                transform = Transform_class(params)
                print(f"Transform: {transform.name}")
                base, ext = os.path.splitext(fname)
                trans_fname = f"{base}_{transform.shortname}{ext}"
                print(f"Saving to file {trans_fname}")
                trans_data = transform.transform_string(raw_data)
                with open(trans_fname, "wb") as outfile:
                    outfile.write(trans_data.encode())


if __name__ == "__main__":
    main()
