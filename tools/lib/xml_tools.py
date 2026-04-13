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
# end try

# Find python version
_LOGGER = None

###############################################################################
def call_command(commands, logger, silent=False):
###############################################################################
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
    # end if
    try:
        cproc = subprocess.run(commands, check=True,
                               capture_output=True)
        if not silent:
            logger.debug(cproc.stdout)
        # end if
        result = cproc.returncode == 0
    except (OSError, RuntimeError, subprocess.CalledProcessError) as err:
        if silent:
            result = False
        else:
            cmd = ' '.join(commands)
            emsg = "Execution of '{}' failed with code:\n"
            outstr = emsg.format(cmd, err.returncode)
            outstr += "{}".format(err.output)
            raise RuntimeError(outstr)
        # end if
    # end of try
    return result

###############################################################################
def find_schema_file(schema_root, schema_path=None):
###############################################################################
    """Find and return the schema file based on <schema_root> or return None.
    If <schema_path> is present, use that as the directory to find the
    appropriate schema file. Otherwise, just look in the current directory."""

    schema_filename = f"{schema_root}.xsd".format(schema_root)
    if schema_path:
        schema_file = os.path.join(schema_path, schema_filename)
    else:
        schema_file = schema_filename
    # end if
    if os.path.exists(schema_file):
        return schema_file
    # end if
    return None

###############################################################################
def validate_xml_file(filename, schema_root, logger,
                      schema_path=None, error_on_noxmllint=False):
###############################################################################
    """
    Find the appropriate schema and validate the XML file, <filename>,
    against it using xmllint
    """
    # Check the filename
    if not os.path.isfile(filename):
        raise ValueError("validate_xml_file: Filename, '{}', does not exist".format(filename))
    # end if
    if not os.access(filename, os.R_OK):
        raise ValueError("validate_xml_file: Cannot open '{}'".format(filename))
    # end if
    if not schema_path:
        # Find the schema file
        thispath = os.path.abspath(__file__)
        pdir = os.path.dirname(os.path.dirname(os.path.dirname(thispath)))
        schema_path = os.path.join(pdir, 'schema')
    # end if
    schema_file = find_schema_file(schema_root, schema_path)
    if not (schema_file and os.path.isfile(schema_file)):
        raise ValueError(f"validate_xml_file: Cannot find schema file {schema_file}")
    # end if
    if not os.access(schema_file, os.R_OK):
        emsg = "validate_xml_file: Cannot open schema, '{}'"
        raise ValueError(emsg.format(schema_file))
    # end if
    if _XMLLINT is not None:
        if logger is not None:
            lmsg = "Checking file {} against schema {}"
            logger.debug(lmsg.format(filename, schema_file))
        # end if
        cmd = [_XMLLINT, '--noout', '--schema', schema_file, filename]
        result = call_command(cmd, logger)
        return result
    # end if
    lmsg = "xmllint not found, could not validate file {}"
    if error_on_noxmllint:
        raise ValueError("validate_xml_file: " + lmsg.format(filename))
    # end if
    if logger is not None:
        logger.warning(lmsg.format(filename))
    # end if
    return True # We could not check but still need to proceed

###############################################################################
def read_xml_file(filename, logger=None):
###############################################################################
    """Read the XML file, <filename>, and return its tree and root"""
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        file_open = (lambda x: open(x, 'r'))
        # end if
        with file_open(filename) as file_:
            try:
                tree = ET.parse(file_)
                root = tree.getroot()
            except ET.ParseError as perr:
                emsg = "read_xml_file: Cannot read {}, {}"
                raise ValueError(emsg.format(filename, perr))
    elif not os.access(filename, os.R_OK):
        raise ValueError("read_xml_file: Cannot open '{}'".format(filename))
    else:
        emsg = "read_xml_file: Filename, '{}', does not exist"
        raise ValueError(emsg.format(filename))
    # end if
    if logger:
        logger.debug("Read XML file, '{}'".format(filename))
    # end if
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
    # end for
    _LOGGER.addHandler(logging.NullHandler())
    try:
        # First, run doctest
        import doctest
        doctest.testmod()
    except ValueError as cerr:
        print("{}".format(cerr))
# no else:
