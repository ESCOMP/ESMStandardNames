#!/usr/bin/env python3

"""

This tool checks if all of the
standard names present in a
CCPP metadata file also exist
in the standard names dictionary.

The tool currently has two options:

1.  A path to a single metadata file
    is passed, in which case only that
    file's standard names are checked, e.g.:

./meta_stdname_check --metafile-loc /path/to/file.meta --stdname-dict /path/to/dict.xml

2.  A path to a directory is passed, in
    which case the directory is searched,
    along with any subdirectories, for
    metadata files, and all found files'
    standard names are checked, e.g.:

./meta_stdname_check --metafile-loc /meta/path/ --stdname-dict /path/to/dict.xml

"""

######################################
#Import needed standard python modules
######################################

import argparse
import sys
import os
import os.path
import datetime
from collections import OrderedDict

################################################
# Add lib modules to python path
################################################

_CURR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_CURR_DIR, "lib"))

#######################################
#Import needed framework python modules
#######################################

from xml_tools import read_xml_file

#################
#Helper functions
#################

#++++++++++++++++++++++++++++++
#Input Argument parser function
#++++++++++++++++++++++++++++++

def parse_arguments():

    """
    Parses command-line input arguments
    using the argparse python module and
    outputs the final argument object.
    """

    #Create description:
    desc = "Check if the metafile contains variable standard names\n"
    desc += "that are not in the provided standard names dictionary."

    #Create parser object:
    parser = argparse.ArgumentParser(description=desc)

    #Add input arguments to be parsed:
    parser.add_argument('-m', '--metafile-loc',
                        metavar='<path to directory or file>',
                        action='store', type=str,
                        help="Location of metadata file(s)")

    parser.add_argument('-s', '--stdname-dict',
                        metavar='<path to file>',
                        action='store', type=str,
                        help="Location of standard name dictionary (XML file)")

    #Parse Argument inputs
    args = parser.parse_args()

    return args.metafile_loc, args.stdname_dict

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Function to extract standard names from element tree root
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_dict_stdnames(xml_tree_root):

    """
    Extract all elements with the "standard_name" tag,
    find the "name" attribute for that tag, and collect
    all of those "names" in a set.
    """

    #Create empty set to store standard name names:
    std_dict_names = set()

    #Loop over all standard_name tags"
    for stdname in xml_tree_root.findall('./section/standard_name'):
        #Add the "name" attribute to the set:
        std_dict_names.add(stdname.attrib['name'])
    #End for

    return std_dict_names

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Function to parse a list of strings from a metadata file
#in order to find all standard names
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def find_metafile_stdnames(metafile_obj):

    """
    Find all lines that start with "standard_name",
    and then assume that all characters after an "="
    are part of the standard name, excluding those
    that are behind a comment delimiter (#).

    NOTE:

    The CCPP-framework has much more advanced parsers
    that can extract this same info, but bringing them
    into this repo would require many additional
    supporting source files to be brought in as well.

    However, if it is found that this simplified parser
    is hitting too many edge cases then it might be wise
    to use the actual CCPP-framework parser instead of
    expanding on this function or script.
    """

    #Create empty set to store found standard names:
    meta_stdname_set = set()

    #Loop over lines in metadata file object:
    for line in metafile_obj:

        #Check if line starts with "standard_name":
        if line.lstrip().startswith("standard_name"):

            #Attempt to find string index for "equals" sign:
            equals_index = line.find("=")

            #Check if an equals sign actually
            #exists:
            if equals_index != -1:

                #If so, then extract all text to the right
                #of the equals sign:
                stdname_text = line[equals_index+1:]

                #Attempt to find the index for a comment delimiter:
                comment_index = stdname_text.find("#")

                #If comment exists, then remove
                #it from the standard name text:
                if comment_index != -1:
                    stdname_text = stdname_text[:comment_index]
                #End if
            #End if

            #Add stripped/trimmed text to the standardname set:
            meta_stdname_set.add(stdname_text.strip())

        #End if
    #End for

    return meta_stdname_set

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Function to extract standard names in CCPP metadata file
#that are not in a provided set of accepted standard names
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def missing_metafile_names(metafile, stdname_set):

    """
    Extract all standard names listed in CCPP
    metadata file, and provide a list of all
    names that are not in the provide standard
    name set.
    """

    #Open metadata file:
    with open(metafile,'r', encoding='utf-8') as mfile:

        #Find all standard names in metadata file
        meta_stdname_set = find_metafile_stdnames(mfile)
    #End with

    #Create set of all standard names not in dictionary set:
    missing_stdname_set = meta_stdname_set.difference(stdname_set)

    #Return sorted list of missing standard names:
    return sorted(missing_stdname_set)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Function to find the paths to all metadata files within
#a given directory path
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def find_metadata_files(dir_path):

    """
    Walk through the provided directory
    and create a list of all found CCPP
    metadata files.
    """

    #Create new, empy list to store metadata file paths:
    metadata_files = []

    #Walk through provided directory:
    for root, _, files in os.walk(dir_path):
        #Ignore git directories:
        if '.git' not in root:

            #Find all metadata files in current root location:
            local_meta_files = [mfil for mfil in files if mfil[-5:] == '.meta']


            #Add all found metadata files to metadata list,
            #including their full path:
            for local_file in local_meta_files:
                metadata_files.append(os.path.join(root, local_file))
            #End for
        #End if
    #End for

    #Return list of metadata files:
    return metadata_files

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Function to print a "human-readable" list of all of the
#standard names in the provided CCPP metadata files that
#were not found in the provided standard name dictionary
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def print_missing_names(missing_names_dict):

    """
    Prints a list of the metadata files that
    contain standard names not found in the
    dictionary, and underneath each metadata
    file a list of each "missing" standard name.
    """

    #Get current date/time:
    curr_time = datetime.datetime.now()

    print("\n#######################")
    print("Date/time of when script was run:")
    print(curr_time)
    print("#######################")
    msg = "\nNon-dictionary standard names found in the following"
    msg += " metadata files:"
    print(msg)

    #Loop over dictionary keys, which should be
    #paths to metadata files:
    for metafile in missing_names_dict:

        print("\n--------------------------\n")
        print(f"{metafile}\n")

        #Extract standard names for file:
        missing_names_list = missing_names_dict[metafile]

        for stdname in missing_names_list:
            print(f"    - {stdname}")
        #End for

    #End for

    print("\n#######################")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

############
#Main script
############

#Parse command-line arguments:
metafile_loc, stdname_xml = parse_arguments()

#Open standard name dictionary:
_, stdname_dict_root = read_xml_file(stdname_xml)

#Extract all standard names from dictionary:
std_names = get_dict_stdnames(stdname_dict_root)

#Create new meta file/missing names dictionary:
meta_miss_names_dict = OrderedDict()

#Check if user passed in single metadata file:
if os.path.isfile(metafile_loc):

    #Find all metadata standard names
    #that are not in the dictionary:
    missing_stdnames = missing_metafile_names(metafile_loc,
                                              std_names)

    #If missing stdnames exist, then add the
    #file and missing names to dictionary:
    if missing_stdnames:
        meta_miss_names_dict[metafile_loc] = missing_stdnames
    #End if

#If not a file, then check if a directory:
elif os.path.isdir(metafile_loc):

    #Find all CCPP metadata files that are
    #located in or under this directory:
    meta_files = find_metadata_files(metafile_loc)

    #Loop through all metadata files:
    for meta_file in meta_files:

        #Find all metadata standard names
        #that are not in the dictionary
        missing_stdnames = missing_metafile_names(meta_file,
                                              std_names)

        #If missing stdnames exist, then add the
        #file and missing names to dictionary:
        if missing_stdnames:
            meta_miss_names_dict[meta_file] = missing_stdnames
        #End if
    #End for

else:
    #This is a non-supported input, so raise
    #an error:
    emsg = f"The metafile-loc arg input, '{metafile_loc}'\n"
    emsg += "is neither a file nor a directory,"
    emsg += " so script will end here."
    raise FileNotFoundError(emsg)
#End if

#Print list of metadata file standard
#names that are not in the dictionary:
if meta_miss_names_dict:
    #Print organized, human-readable
    #list of "missing" standard names
    #to the screen, along with the
    #metadata file they are associated
    #with
    print_missing_names(meta_miss_names_dict)
else:
    #Notify user that all standard names
    #exist in the dictionary:
    print("All standard names are in the dictionary!")
#End if


##############
#End of script
