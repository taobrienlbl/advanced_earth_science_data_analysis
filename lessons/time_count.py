#!/usr/bin/env python3
""" Counts the total time required to deliver a lesson plan.

    time_count.py LESSON1.md [LESSON2.md] [LESSON3.md]

    It is expected that the LESSON*.md files have a section formatted as follows:

        ## PREVIEW | Class Overview:
        (5 min) text
        (2 min) text
        .
        .
        .

    This code parses that section and calculates the total time.
"""

import sys

# check the number of input arguments
if len(sys.argv) < 2:
    print("Error: at least one argument is required")
    print(__doc__)
    quit()

# open the input file
input_files = sys.argv[1:]

# loop over input files
for input_file in input_files:
    with open(input_file) as fin:
        file_lines = [ l.rstrip() for l in fin.readlines() ]

    # loop over lines and find the "class overview" section
    section_name = ""
    total_time = 0
    for line in file_lines:
        # check for section name
        if line[:2] == "##":
            section_name = line.lower()

        # check if this is the "class overview" section
        if "class overview" in section_name:
            # only check non-blank lines
            if len(line) > 0:
                # check if this line fits the format of a time entry
                if line[0] == "(":
                    ilast = line.find(")")
                    time_part = line[1:ilast]
                    # extract the time if possible
                    try:
                        mins = int(time_part.split()[0])
                    except:
                        mins = 0
                    # add to the total time
                    total_time += mins

    # print the total time
    print(f"{input_file}: {total_time} mins")
