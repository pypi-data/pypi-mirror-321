#! /usr/bin/env python3
"""
bbcrack

bbcrack is a tool to crack malware obfuscation such as XOR, ROL, ADD (and
many combinations), by bruteforcing all possible keys and and checking for
specific patterns (IP addresses, domain names, URLs, known file headers and
strings, etc) using the balbuzard engine.
It is part of the Balbuzard package.

Author: Philippe Lagadec
Maintainer: Corey Forman (digitalsleuth)
License: BSD, see source code or documentation

Project Repository: https://github.com/digitalsleuth/balbuzard
"""

# LICENSE:
#
# bbcrack is copyright (c) 2013-2019, Philippe Lagadec (http://www.decalage.info)
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
# 2013-02-24 v0.01 PL: - 1st version, moved code from balbuzard
#                      - Transform classes instead of functions
# 2013-03-05 v0.02 PL: - progressive cracking: first simple/fast patterns on all
#                        cases, select best ones, then more elaborate patterns
# 2013-03-15 v0.03 PL: - harvest mode: run all transforms, extract all
#                        significant patterns
# 2013-03-21 v0.04 PL: - open file from password-protected zip (inspired from
#                        Didier Steven's pdfid, thanks Didier! :-)
# 2013-03-26 v0.05 PL: - switched from regex to multi-string patterns, 8x speed
#                        increase in harvest mode.
#                      - fixed bug in xor_add transform
# 2013-04-02 v0.06 PL: - added Transform_XOR_DEC
# 2013-12-06 v0.07 PL: - moved multiple trans code to bbharvest
# 2014-01-04 v0.08 PL: - improved transform names
#                      - moved code from main to functions
#                      - added -i option for incremental level
# 2014-01-06 v0.09 PL: - added the possibility to write transform plugins
# 2014-01-20 v0.10 PL: - added Transform_ROL, added patterns for stage 1
# 2014-01-23 v0.11 PL: - moved and merged patterns into patterns.py
# 2014-01-28 v0.12 PL: - ignore transforms with null scores at the end of stage 2
# 2014-04-09 v0.13 PL: - added transform_int to simplify char transforms
# 2014-05-22 v0.14 PL: - simplified all Transform_chars with transform_int
# 2019-06-16 v0.20 PL: - added main function for pip entry points (issue #8)
# 2024-12-03 v1.0.0 CF: - Ported all code to Python 3

__version__ = "1.00"

# ------------------------------------------------------------------------------
# TODO
# + Transform classes should have a name (short) and a description (long)
# + improve display for stage 1 results (option to be more verbose?)
# + patterns for stage 1 and 2 should be more coherent (include stage 1 results)
# + -e option to encrypt output files with zip password
# + -f option to select file(s) within zip instead of the 1st one
# + profiling to see which patterns take more time => find which regex hangs
# + increase default params - k=30 s=5?
# + two stage regex, or string+regex, multiple strings, stop after 1 match
# + move main code to functions
# + test yara engine to see if faster
# - merge regex of same weight to improve speed?
# - try acora for faster multi-string search, or other libraries?
# - try pyre2 for faster regex search?
# - option to launch balbuzard with bbcrack patterns only
# - distributed processing on several machines with slave processes
# - add patterns: file path Windows, Unix
# - performance improvement: use findall in Pattern rather than finditer?
#   OR even just find the 1st occurence?
# - inverse transform in each transform class? (useful in bbtrans)
# - option to run balbuzard automatically on best scores
# - csv output for stage1+2
# - optimize patterns with strings + case-insensitive (with lower())
# - Transforms: class method or attribute to return total number of params, to
#   be able to display progression as % or ETA.

# other transforms to be added:
# sub inc rol
# xor add rol
# xor rol add
# add xor rol
# base64
# hex
# LZNT1 when applicable?
# split with two transforms
# xor chained with previous char


# --- IMPORTS ------------------------------------------------------------------

import sys
import os
import time
import argparse
import zipfile

try:
    from balbuzard import Balbuzard, rglob, PLUGINS_DIR
    from bbpatterns import bbcrack_patterns, bbcrack_patterns_stage1
except (ImportError, ModuleNotFoundError):
    from balbuzard.balbuzard import Balbuzard, rglob, PLUGINS_DIR
    from balbuzard.bbpatterns import bbcrack_patterns, bbcrack_patterns_stage1


# --- CLASSES ------------------------------------------------------------------


class Transform_string:
    """
    Generic class to define a transform that acts on a string globally.
    """

    # generic name and id for the class:
    gen_name = "Generic String Transform"
    gen_id = "string"

    def __init__(self, params=None):
        """
        constructor for the Transform object.
        This method needs to be overloaded for every specific Transform.
        It should set name and shortname according to the provided parameters.
        (for example shortname="xor_17" for a XOR transform with params=17)
        params: single value or tuple of values, parameters for the transformation
        """
        self.name = "Undefined String Transform"
        self.shortname = "undefined_string"
        self.params = params

    def transform_string(self, data):
        """
        Method to be overloaded, only for a transform that acts on a string
        globally.
        This method should apply the transform to the data string, using params
        as parameters, and return the transformed data as a string.
        (the resulting string does not need to have the same length as data)
        """
        raise NotImplementedError

    @staticmethod
    def iter_params():
        """
        Method to be overloaded.
        This static method should iterate over all possible parameters for the
        transform function, yielding each set of parameters as a single value
        or a tuple of values.
        (for example for a XOR transform, it should yield 1 to 255)
        This method should be used on the Transform class in order to
        instantiate a Transform object with each set of parameters.
        """
        raise NotImplementedError


class Transform_char(Transform_string):
    """
    Generic class to define a transform that acts on each character of a string
    separately.
    """

    # generic name for the class:
    gen_name = "Generic Character Transform"
    gen_id = "char"

    def __init__(self, params=None):
        """
        constructor for the Transform object.
        This method needs to be overloaded for every specific Transform.
        It should set name and shortname according to the provided parameters.
        (for example shortname="xor_17" for a XOR transform with params=17)
        params: single value or tuple of values, parameters for the transformation
        """
        self.name = "Undefined Character Transform"
        self.shortname = "undefined_char"
        self.params = params

    def transform_string(self, data):
        """
        This method applies the transform to the data string, using params
        as parameters, and return the transformed data as a string.
        Here, each character is transformed separately by calling transform_char.
        A translation table is used to speed up the processing.
        (the resulting string should have the same length as data)
        """
        # for optimal speed, we build a translation table:
        if isinstance(data, bytes):
            data = data.decode('latin-1')
        self.trans_table = ""
        for i in range(256):
            self.trans_table += self.transform_char(chr(i))
        return data.translate(self.trans_table)

    def transform_char(self, char):
        """
        Method that can be overloaded, only for a transform that acts on a character.
        This method should apply the transform to the provided char, using params
        as parameters, and return the transformed data as a character.
        NOTE: it is usually simpler to overload transform_int and leave this one
        untouched.
        (here character = string of length 1)
        """
        # by default, call transform_int using ord(char), and convert it back
        # to a single character:
        return chr(self.transform_int(ord(char)))

    def transform_int(self, i):
        """
        Method to be overloaded, only for a transform that acts on a character.
        This method should apply the transform to the provided integer which is
        the ASCII code of a character (i.e. ord(c)), using params
        as parameters, and return the transformed data as an integer.
        (here character = string of length 1)
        """
        raise NotImplementedError


# --- TRANSFORMS ---------------------------------------------------------------


class Transform_identity(Transform_string):
    """
    Transform that does not change data.
    """

    # generic name for the class:
    gen_name = "Identity Transformation, no change to data. Parameters: none."
    gen_id = "identity"

    def __init__(self, params=None):
        self.name = self.gen_name
        self.shortname = self.gen_id
        self.params = None

    def transform_string(self, data):
        return data

    @staticmethod
    def iter_params():
        yield None


# ------------------------------------------------------------------------------
class Transform_XOR(Transform_char):
    """
    XOR Transform
    """

    # generic name for the class:
    gen_name = "XOR with 8 bits static key A. Parameters: A (1-FF)."
    gen_id = "xor"

    def __init__(self, params):
        assert isinstance(params, int)
        #assert params > 0 and params < 256
        assert 0 < params < 256
        self.params = params
        self.name = f"XOR {params:02X}"
        self.shortname = f"xor{params:02X}"

    def transform_int(self, i):
        # here params is an integer
        return i ^ self.params

    @staticmethod
    def iter_params():
        # the XOR key can be 1 to 255 (0 would be identity)
        #for key in range(1, 256):
        #    yield key
        yield from range(1, 256)


# ------------------------------------------------------------------------------
class Transform_XOR_INC(Transform_string):
    """
    XOR Transform, with incrementing key
    """

    # generic name for the class:
    gen_name = (
        "XOR with 8 bits key A incrementing after each character. Parameters: A (0-FF)."
    )
    gen_id = "xor_inc"

    def __init__(self, params):
        assert isinstance(params, int)
        #assert params >= 0 and params < 256
        assert 0 <= params < 256
        self.params = params
        self.name = f"XOR {params:02X} INC"
        self.shortname = f"xor{params:02X}_inc"

    def transform_string(self, data):
        # here params is an integer
        # TODO: use a list comprehension + join to get better performance
        # this loop is more readable, but likely to  be much slower
        out = ""
        if isinstance(data, bytes):
            data = data.decode('latin-1')        
        for i in range(len(data)):
            xor_key = (self.params + i) & 0xFF
            out += chr(ord(data[i]) ^ xor_key)
        return out

    @staticmethod
    def iter_params():
        # the XOR key can be 0 to 255 (0 is not identity here)
        #for xor_key in range(0, 256):
        #    yield xor_key
        yield from range(0, 256)


# ------------------------------------------------------------------------------
class Transform_XOR_DEC(Transform_string):
    """
    XOR Transform, with decrementing key
    """

    # generic name for the class:
    gen_name = (
        "XOR with 8 bits key A decrementing after each character. Parameters: A (0-FF)."
    )
    gen_id = "xor_dec"

    def __init__(self, params):
        assert isinstance(params, int)
        #assert params >= 0 and params < 256
        assert 0 <= params < 256
        self.params = params
        self.name = f"XOR {params:02X} DEC"
        self.shortname = f"xor{params:02X}_dec"

    def transform_string(self, data):
        # here params is an integer
        # TODO: use a list comprehension + join to get better performance
        # this loop is more readable, but likely to  be much slower
        out = ""
        if isinstance(data, bytes):
            data = data.decode('latin-1')        
        for i in range(len(data)):
            xor_key = (self.params + 0xFF - i) & 0xFF
            out += chr(ord(data[i]) ^ xor_key)
        return out

    @staticmethod
    def iter_params():
        # the XOR key can be 0 to 255 (0 is not identity here)
        #for xor_key in range(0, 256):
        #    yield xor_key
        yield from range(0, 256)


# ------------------------------------------------------------------------------
class Transform_XOR_INC_ROL(Transform_string):
    """
    XOR Transform, with incrementing key, then ROL N bits
    """

    # generic name for the class:
    gen_name = "XOR with 8 bits key A incrementing after each character, then rotate B bits left. Parameters: A (0-FF), B (1-7)."
    gen_id = "xor_inc_rol"

    def __init__(self, params):
        self.params = params
        self.name = f"XOR {params[0]:02X} INC then ROL {params[1]}"
        self.shortname = f"xor{params[0]:02X}_inc_rol{params[1]}"

    def transform_char(self, char):
        # here params is a tuple
        xor_key, rol_bits = self.params
        return chr(rol(ord(char) ^ xor_key, rol_bits))

    def transform_string(self, data):
        # here params is a tuple
        # TODO: use a list comprehension + join to get better performance
        # this loop is more readable, but likely to  be much slower
        xor_key_init, rol_bits = self.params
        out = ""
        if isinstance(data, bytes):
            data = data.decode('latin-1')        
        for i in range(len(data)):
            xor_key = (xor_key_init + i) & 0xFF
            out += chr(rol(ord(data[i]) ^ xor_key, rol_bits))
        return out

    @staticmethod
    def iter_params():
        "return (XOR key, ROL bits)"
        # the XOR key can be 0 to 255 (0 is not identity here)
        for xor_key in range(0, 256):
            # the ROL bits can be 1 to 7:
            for rol_bits in range(1, 8):
                yield (xor_key, rol_bits)


# ------------------------------------------------------------------------------
class Transform_SUB_INC(Transform_string):
    """
    SUB Transform, with incrementing key
    """

    # generic name for the class:
    gen_name = (
        "SUB with 8 bits key A incrementing after each character. Parameters: A (0-FF)."
    )
    gen_id = "sub_inc"

    def __init__(self, params):
        assert isinstance(params, int)
        #assert params >= 0 and params < 256
        assert 0 <= params < 256
        self.params = params
        self.name = f"SUB {params:02X} INC"
        self.shortname = f"sub{params:02X}_inc"

    def transform_string(self, data):
        # here params is an integer
        # TODO: use a list comprehension + join to get better performance
        # this loop is more readable, but likely to  be much slower
        out = ""
        if isinstance(data, bytes):
            data = data.decode('latin-1')        
        for i in range(len(data)):
            key = (self.params + i) & 0xFF
            out += chr((ord(data[i]) - key) & 0xFF)
        return out

    @staticmethod
    def iter_params():
        # the SUB key can be 0 to 255 (0 is not identity here)
        #for key in range(0, 256):
        #    yield key
        yield from range(0, 256)


def rol(byte, count):
    byte = (byte << count | byte >> (8 - count)) & 0xFF
    return byte


###safety checks
##assert rol(1, 1) == 2
##assert rol(128, 1) == 1
##assert rol(1, 7) == 128
##assert rol(1, 8) == 1


# ------------------------------------------------------------------------------
class Transform_XOR_Chained(Transform_string):
    """
    XOR Transform, chained with previous character.
    xor_chained(c[i], key) = c[i] xor c[i-1] xor key
    """

    # generic name for the class:
    gen_name = (
        "XOR with 8 bits key A chained with previous character. Parameters: A (1-FF)."
    )
    gen_id = "xor_chained"

    def __init__(self, params):
        assert isinstance(params, int)
        #assert params >= 0 and params < 256
        assert 0 <= params < 256
        self.params = params
        self.name = f"XOR {params:02X} Chained"
        self.shortname = f"xor{params:02X}_chained"

    def transform_string(self, data):
        # here params is an integer
        # TODO: it would be much faster to do the xor_chained once, then all
        #      xor transforms using translate() only
        # TODO: use a list comprehension + join to get better performance
        # this loop is more readable, but likely to  be much slower

        if len(data) == 0:
            return ""
        xor_key = self.params
        # 1st char is just xored with key:
        if isinstance(data, bytes):
            data = data.decode('latin-1')    
        out = chr(ord(data[0]) ^ xor_key)
        for i in range(1, len(data)):
            out += chr(ord(data[i]) ^ xor_key ^ ord(data[i - 1]))
        return out

    @staticmethod
    def iter_params():
        # the XOR key can be 0 to 255 (0 is not identity here)
        #for xor_key in range(0, 256):
        #    yield xor_key
        yield from range(0, 256)


# ------------------------------------------------------------------------------
class Transform_XOR_RChained(Transform_string):
    """
    XOR Transform, chained with next character. (chained on the right)
    xor_rchained(c[i], key) = c[i] xor c[i+1] xor key
    """

    # generic name for the class:
    gen_name = "XOR with 8 bits key A chained with next character (Reverse order from end to start). Parameters: A (1-FF)."
    gen_id = "xor_rchained"

    def __init__(self, params):
        assert isinstance(params, int)
        #assert params >= 0 and params < 256
        assert 0 <= params < 256
        self.params = params
        self.name = f"XOR {params:02X} RChained"
        self.shortname = f"xor{params:02X}_rchained"

    def transform_string(self, data):
        # here params is an integer
        # TODO: it would be much faster to do the xor_rchained once, then all
        #      xor transforms using translate() only
        # TODO: use a list comprehension + join to get better performance
        # this loop is more readable, but likely to  be much slower
        if len(data) == 0:
            return ""
        out = ""
        xor_key = self.params
        # all chars except last one are xored with key and next char:
        if isinstance(data, bytes):
            data = data.decode('latin-1')         
        for i in range(len(data) - 1):
            out += chr(ord(data[i]) ^ xor_key ^ ord(data[i + 1]))
        # last char is just xored with key:
        out += chr(ord(data[len(data) - 1]) ^ xor_key)
        return out

    @staticmethod
    def iter_params():
        # the XOR key can be 0 to 255 (0 is not identity here)
        #for xor_key in range(0, 256):
        #    yield xor_key
        yield from range(0, 256)


# ------------------------------------------------------------------------------
class Transform_XOR_RChainedAll(Transform_string):
    """
    XOR Transform, chained from the right with all following characters.
    (as found in Taidoor malware)
    NOTE: this only works well in harvest mode, when testing all 256
          possibilities, because the key is position-dependent.
    xor_rchained_all(c[i], key) = c[i] xor key xor c[i+1] xor c[i+2]... xor c[N]
    """

    # generic name for the class:
    gen_name = "XOR Transform, chained from the right with all following characters. Only works well with bbharvest."
    gen_id = "xor_rchained_all"

    def __init__(self, params):
        assert isinstance(params, int)
        #assert params >= 0 and params < 256
        assert 0 <= params < 256
        self.params = params
        self.name = f"XOR {params:02X} RChained All"
        self.shortname = f"xor{params:02X}_rchained_all"

    def transform_string(self, data):
        # here params is an integer
        # TODO: it would be much faster to do the xor_rchained once, then all
        #      xor transforms using translate() only
        # TODO: use a list comprehension + join to get better performance
        # this loop is more readable, but likely to  be much slower
        if len(data) == 0:
            return ""
        xor_key = self.params
        # transform data string to list of integers:
        l = list(map(ord, data))
        # loop from last char to 2nd one:
        for i in range(len(data) - 1, 1, -1):
            l[i - 1] = l[i - 1] ^ xor_key ^ l[i]
        # last char is only xored with key:
        l[len(data) - 1] = l[len(data) - 1] ^ xor_key
        # convert back to list of chars:
        l = list(map(chr, l))
        out = "".join(l)
        return out

    @staticmethod
    def iter_params():
        # the XOR key can be 0 to 255 (0 is not identity here)
        #for xor_key in range(0, 256):
        #    yield xor_key
        yield from range(0, 256)


# ------------------------------------------------------------------------------
class Transform_ROL(Transform_char):
    """
    ROL Transform
    """

    # generic name for the class:
    gen_name = "ROL - rotate A bits left. Parameters: A (1-7)."
    gen_id = "rol"

    def __init__(self, params):
        self.params = params
        self.name = f"ROL {params}"
        self.shortname = f"rol{params}"

    def transform_int(self, i):
        # here params is an int
        rol_bits = self.params
        return rol(i, rol_bits)

    @staticmethod
    def iter_params():
        "return (ROL bits)"
        # the ROL bits can be 1 to 7:
        #for rol_bits in range(1, 8):
        #    yield rol_bits
        yield from range(1, 8)


# ------------------------------------------------------------------------------
class Transform_XOR_ROL(Transform_char):
    """
    XOR+ROL Transform - first XOR, then ROL
    """

    # generic name for the class:
    gen_name = "XOR with static 8 bits key A, then rotate B bits left. Parameters: A (1-FF), B (1-7)."
    gen_id = "xor_rol"

    def __init__(self, params):
        self.params = params
        self.name = f"XOR {params[0]:02X} then ROL {params[1]}"
        self.shortname = f"xor{params[0]:02X}_rol{params[1]}"

    def transform_int(self, i):
        # here params is a tuple
        xor_key, rol_bits = self.params
        return rol(i ^ xor_key, rol_bits)

    @staticmethod
    def iter_params():
        "return (XOR key, ROL bits)"
        # the XOR key can be 1 to 255 (0 would be like ROL)
        for xor_key in range(1, 256):
            # the ROL bits can be 1 to 7:
            for rol_bits in range(1, 8):
                yield (xor_key, rol_bits)


# ------------------------------------------------------------------------------
class Transform_ADD(Transform_char):
    """
    ADD Transform
    """

    # generic name for the class:
    gen_name = "ADD with 8 bits static key A. Parameters: A (1-FF)."
    gen_id = "add"

    def __init__(self, params):
        self.params = params
        self.name = f"ADD {params:02X}"
        self.shortname = f"add{params:02X}"

    def transform_int(self, i):
        # here params is an integer
        add_key = self.params
        return (i + add_key) & 0xFF

    @staticmethod
    def iter_params():
        "return ADD key"
        # the ADD key can be 1 to 255 (0 would be identity):
        #for add_key in range(1, 256):
        #    yield add_key
        yield from range(1, 256)


# ------------------------------------------------------------------------------
class Transform_ADD_ROL(Transform_char):
    """
    ADD+ROL Transform - first ADD, then ROL
    """

    # generic name for the class:
    gen_name = "ADD with static 8 bits key A, then rotate B bits left. Parameters: A (1-FF), B (1-7)."
    gen_id = "add_rol"

    def __init__(self, params):
        self.params = params
        self.name = f"ADD {params[0]:02X} then ROL {params[1]}"
        self.shortname = f"add{params[0]:02X}_rol{params[1]}"

    def transform_int(self, i):
        # here params is a tuple
        add_key, rol_bits = self.params
        return rol((i + add_key) & 0xFF, rol_bits)

    @staticmethod
    def iter_params():
        "return (ADD key, ROL bits)"
        # the ADD key can be 1 to 255 (0 would be like ROL)
        for add_key in range(1, 256):
            # the ROL bits can be 1 to 7:
            for rol_bits in range(1, 8):
                yield (add_key, rol_bits)


# ------------------------------------------------------------------------------
class Transform_ROL_ADD(Transform_char):
    """
    ROL+ADD Transform - first ROL, then ADD
    """

    # generic name for the class:
    gen_name = "rotate A bits left, then ADD with static 8 bits key B. Parameters: A (1-7), B (1-FF)."
    gen_id = "rol_add"

    def __init__(self, params):
        self.params = params
        self.name = f"ROL {params[0]} then ADD {params[1]:02X}"
        self.shortname = f"rol{params[0]}_add{params[1]:02X}"

    def transform_int(self, i):
        # here params is a tuple
        rol_bits, add_key = self.params
        return (rol(i, rol_bits) + add_key) & 0xFF

    @staticmethod
    def iter_params():
        "return (ROL bits, ADD key)"
        # the ROL bits can be 1 to 7:
        for rol_bits in range(1, 8):
            # the ADD key can be 1 to 255 (0 would be identity)
            for add_key in range(1, 256):
                yield (rol_bits, add_key)


# ------------------------------------------------------------------------------
class Transform_XOR_ADD(Transform_char):
    """
    XOR+ADD Transform - first XOR, then ADD
    """

    # generic name for the class:
    gen_name = "XOR with 8 bits static key A, then ADD with 8 bits static key B. Parameters: A (1-FF), B (1-FF)."
    gen_id = "xor_add"

    def __init__(self, params):
        self.params = params
        self.name = f"XOR {params[0]:02X} then ADD {params[1]:02X}"
        self.shortname = f"xor{params[0]:02X}_add{params[1]:02X}"

    def transform_int(self, i):
        # here params is a tuple
        xor_key, add_key = self.params
        return ((i ^ xor_key) + add_key) & 0xFF

    @staticmethod
    def iter_params():
        "return (XOR key1, ADD key2)"
        # the XOR key can be 1 to 255 (0 would be identity)
        for xor_key in range(1, 256):
            # the ADD key can be 1 to 255 (0 would be identity):
            for add_key in range(1, 256):
                yield (xor_key, add_key)


# ------------------------------------------------------------------------------
class Transform_ADD_XOR(Transform_char):
    """
    ADD+XOR Transform - first ADD, then XOR
    """

    # generic name for the class:
    gen_name = "ADD with 8 bits static key A, then XOR with 8 bits static key B. Parameters: A (1-FF), B (1-FF)."
    gen_id = "add_xor"

    def __init__(self, params):
        self.params = params
        self.name = f"ADD {params[0]:02X} then XOR {params[1]:02X}"
        self.shortname = f"add{params[0]:02X}_xor{params[1]:02X}"

    def transform_int(self, i):
        # here params is a tuple
        add_key, xor_key = self.params
        return ((i + add_key) & 0xFF) ^ xor_key

    @staticmethod
    def iter_params():
        "return (ADD key1, XOR key2)"
        # the ADD key can be 1 to 255 (0 would be identity):
        for add_key in range(1, 256):
            # the XOR key can be 1 to 255 (0 would be identity)
            for xor_key in range(1, 256):
                yield (add_key, xor_key)


# --- TRANSFORM GROUPS ---------------------------------------------------------

# Transforms level 1
transform_classes1 = [
    Transform_identity,
    Transform_XOR,
    Transform_ADD,
    Transform_ROL,
    Transform_XOR_ROL,
    Transform_ADD_ROL,
    Transform_ROL_ADD,
]

# Transforms level 2
transform_classes2 = [
    Transform_XOR_ADD,
    Transform_ADD_XOR,
    Transform_XOR_INC,
    Transform_XOR_DEC,
    Transform_SUB_INC,
    Transform_XOR_Chained,
    Transform_XOR_RChained,
]

# Transforms level 3
transform_classes3 = [
    Transform_XOR_INC_ROL,
    Transform_XOR_RChainedAll,
]

# all transforms
transform_classes_all = transform_classes1 + transform_classes2 + transform_classes3


# --- PATTERNS -----------------------------------------------------------------

# see bbpatterns.py

# === FUNCTIONS ================================================================


def list_transforms():
    """
    Display the list of available transforms on the console, grouped by level.
    Then exit the application.
    """
    print("Available transforms - Level 1:")
    for Transform in transform_classes1:
        print(f"- {Transform.gen_id}: {Transform.gen_name}")
    print("")
    print("Level 2:")
    for Transform in transform_classes2:
        print(f"- {Transform.gen_id}: {Transform.gen_name}")
    print("")
    print("Level 3:")
    for Transform in transform_classes3:
        print(f"- {Transform.gen_id}: {Transform.gen_name}")
    sys.exit()


def select_transforms(level=2, incremental_level=None, transform_names=None):
    """
    Select transform based on options, by order or precedence:
    - transform_names: str, comma-separated list of transform ids
    - incremental_level: int or None, only the transforms from that level
    - level: int, all transforms up to that level
    """
    # First check transform_names:
    if transform_names is not None:
        # options.transform is either a transform name, or a comma-separated list
        transform_classes = []
        trans_names = transform_names.split(",")
        for tname in trans_names:
            for trans in transform_classes_all:
                if trans.gen_id == tname:
                    transform_classes.append(trans)
        # check if any transform was found:
        if len(transform_classes) == 0:
            sys.exit(
                f'Transform "{transform_names}" does not exist. Use "-t list" to see all available transforms.'
            )
        return transform_classes

    # then incremental level:
    if incremental_level is not None:
        if incremental_level == 1:
            transform_classes = transform_classes1
        elif incremental_level == 2:
            transform_classes = transform_classes2
        else:
            transform_classes = transform_classes3
        return transform_classes

    # otherwise, simple level:
    if level == 1:
        transform_classes = transform_classes1
    elif level == 2:
        transform_classes = transform_classes1 + transform_classes2
    else:
        transform_classes = transform_classes_all
    return transform_classes


def read_file(filename, zip_password=None):
    """
    Open a file, read and return its data as a string.
    If zip_password is provided, the file will be opened as a zip file, and the
    password will be used to decrypt and read the 1st file in the zip archive.
    """
    if zip_password is not None:
        # extract 1st file from zip archive, using password
        print(f'Opening zip archive {filename} with password "{zip_password}"')
        z = zipfile.ZipFile(filename, "r")
        print(f"Opening first file: {z.infolist()[0].filename}")
        raw_data = z.read(z.infolist()[0], zip_password)
    else:
        # normal file
        print(f"Opening file {filename}")
        f = open(filename, "rb")
        raw_data = f.read()
        f.close()
    return raw_data


def add_transform(transform, level=2):
    """
    Add a Transform to the given level.
    (to be used for transform plugins)
    """
    if level == 1:
        transform_classes1.append(transform)
    elif level == 2:
        transform_classes2.append(transform)
    else:
        transform_classes3.append(transform)


def load_plugins():
    """
    Load plugin scripts
    """
    for f in rglob(PLUGINS_DIR, "trans*.py"):
        print(f"Loading transform plugin from {f}")
        exec(compile(open(f, "rb").read(), f, "exec"))


# === MAIN =====================================================================


def main():
    usage = "usage: %(prog)s [options] <filename>"
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
        default=2,
        type=int,
        help="select transforms with level 1, 2 or 3 and below",
    )
    parser.add_argument(
        "-i",
        "--inclevel",
        dest="inclevel",
        default=None,
        help="select transforms only with level 1, 2 or 3 (incremental)",
    )
    parser.add_argument(
        "-k",
        "--keep",
        dest="keep",
        default=20,
        type=int,
        help="number of transforms to keep after stage 1",
    )
    parser.add_argument(
        "-s",
        "--save",
        dest="save",
        default=10,
        type=int,
        help="number of transforms to save to files after stage 2",
    )
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
    
        # STAGE 1: quickly count some significant characters to select best transforms
        print("STAGE 1: quickly counting simple patterns for all transforms")
        results1 = []
        best_score = 0
        start_time = time.process_time()
        bbz1 = Balbuzard(bbcrack_patterns_stage1)
        for Transform_class in transform_classes:
            # iterate over all possible params for that transform class:
            for params in Transform_class.iter_params():
                # instantiate a Transform object with these params
                transform = Transform_class(params)
                # transform data:
                data = transform.transform_string(raw_data.decode('latin-1'))
                score = 0
                # search each pattern in transformed data:
                for pattern, count in bbz1.count(data):
                    score += count * pattern.weight
                msg = f"\rTransform {transform.shortname}: stage 1 score={score}          "
                print(msg, end=" ")
                results1.append((transform, score))
                if score >= best_score:
                    best_score = score
                    print(
                        f"\rBest score so far: {transform.shortname}, stage 1 score={score}"
                    )
        print("")
        t = time.process_time() - start_time
        print(
            f"Checked {len(results1)} transforms in {t} seconds - {len(results1) / t} transforms/s"
        )
        # sort transform results by score:
        results1 = sorted(results1, key=lambda r: r[1], reverse=True)
        # keep only the N best scores:
        results1 = results1[: args.keep]
        print(f"\nTOP {args.keep} SCORES stage 1:")
        for res in results1:
            print(f"{res[0].shortname:>20}: {res[1]}")
        ##    raw_input()
    
        # STAGE 2: search patterns on selected transforms
        results = []
        bbz = Balbuzard(bbcrack_patterns)  # balbuzard.patterns) #
    
        for transform, _ in results1:
            # transform data again (data was not kept)
            data = transform.transform_string(raw_data.decode('latin-1'))
            score = 0
            for pattern, matches in bbz.scan(data):
                for _, match in matches:
                    score += len(match) * pattern.weight
                print(f"Found {len(matches)} * {pattern.name} weight={pattern.weight}")
                
            print(f"Transform {transform.shortname}: score={score}\n")
            results.append((transform, score, data))
    
        print("\nHIGHEST SCORES (>0):")
        results = sorted(results, key=lambda x: x[1], reverse=True)
        # take the best N:
        for transform, score, data in results[: args.save]:
            if score > 0:
                print(f"{transform.shortname}: score {score}")
                base, ext = os.path.splitext(fname)
                fname_trans = f"{base}_{transform.shortname}{ext}"
                print(f"saving to file {fname_trans}")
                with open(fname_trans, "wb") as output:
                    output.write(data.encode())


if __name__ == "__main__":
    main()


# This was coded while listening to The Walkmen "Heaven".
