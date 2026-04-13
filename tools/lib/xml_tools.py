#!/usr/bin/env python

"""
Parse and / or validate an XML file and return the captured variables.
"""

# Python library imports
from __future__ import print_function
import os
import os.path
import subprocess
import logging
from shutil import which
import xml.etree.ElementTree as ET
try:
    _XMLLINT = which('xmllint')
except ImportError:
    _XMLLINT = None

# Find python version
_LOGGER = None

###############################################################################
def call_command(commands, logger, silent=False):
###############################################################################
    # pylint: disable=line-too-long
    """
    Try a command line and return the output on success (None on failure)
    >>> call_command(['ls', 'really__improbable_fffilename.foo'], _LOGGER) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    RuntimeError: Execution of 'ls really__improbable_fffilename.foo' failed:
    [Errno 2] No such file or directory
    >>> call_command(['ls', 'really__improbable_fffilename.foo'], _LOGGER, silent=True)
    False
    >>> call_command(['ls'], _LOGGER)
    True
    """
    result = False
    outstr = ''
    if logger is None:
        silent = True
    try:
        cproc = subprocess.run(commands, check=True,
                               capture_output=True)
        if not silent:
            logger.debug(cproc.stdout)
        result = cproc.returncode == 0
    except (OSError, RuntimeError, subprocess.CalledProcessError) as err:
        if silent:
            result = False
        else:
            cmd = ' '.join(commands)
            emsg = "Execution of '{cmd}' failed with code: {err.returncode}\n"
            outstr = emsg.format(cmd, err.returncode)
            outstr += f"{err.output}"
            raise RuntimeError(outstr) from err
    return result


def validate_xml_file(filename, schema_file, logger, error_on_noxmllint=False):
###############################################################################
    """
    Find the appropriate schema and validate the XML file, <filename>,
    against it using xmllint
    """
    # Check the filename
    if not os.path.isfile(filename):
        raise ValueError("validate_xml_file: Filename, '{filename}', does not exist")
    if not os.access(filename, os.R_OK):
        raise ValueError("validate_xml_file: Cannot open '{filename}'")
    if not os.path.isfile(schema_file):
        raise ValueError(f"validate_xml_file: Cannot find schema file {schema_file}")
    if not os.access(schema_file, os.R_OK):
        emsg = "validate_xml_file: Cannot open schema, '{}'"
        raise ValueError(emsg.format(schema_file))
    if _XMLLINT is not None:
        if logger is not None:
            lmsg = "Checking file {} against schema {}"
            logger.debug(lmsg.format(filename, schema_file))
        cmd = [_XMLLINT, '--noout', '--schema', schema_file, filename]
        result = call_command(cmd, logger)
        return result
    lmsg = "xmllint not found, could not validate file {}"
    if error_on_noxmllint:
        raise ValueError("validate_xml_file: " + lmsg.format(filename))
    if logger is not None:
        logger.warning(lmsg.format(filename))
    return True # We could not check but still need to proceed

###############################################################################
def read_xml_file(filename, logger=None):
###############################################################################
    """Read the XML file, <filename>, and return its tree and root"""
    if not os.path.isfile(filename):
        raise ValueError(f"read_xml_file: Filename, '{filename}', does not exist")
    if not os.access(filename, os.R_OK):
        raise ValueError(f"read_xml_file: Cannot open '{filename}'")

    try:
        with open(filename, 'r', encoding="utf-8") as file_:
            tree = ET.parse(file_)
            root = tree.getroot()
    except ET.ParseError as perr:
        raise ValueError(f"read_xml_file: Cannot read {filename}, {perr}") from perr

    if logger:
        logger.debug(f"Read XML file, '{filename}'")
    return tree, root

###############################################################################
def get_standard_names_as_set(root):
###############################################################################
    """
    Extract all standard_name elements from root (at any nesting depth),
    collect their 'name' attributes, and return as a set.
    """
    std_names = set()
    for stdname in root.findall('.//standard_name'):
        std_names.add(stdname.attrib['name'])
    return std_names

###############################################################################

if __name__ == "__main__":
    _LOGGER = logging.getLogger('xml_tools')
    for handler in list(_LOGGER.handlers):
        _LOGGER.removeHandler(handler)
    _LOGGER.addHandler(logging.NullHandler())
    try:
        # First, run doctest
        import doctest
        doctest.testmod()
    except ValueError as cerr:
        print("{cerr}")
