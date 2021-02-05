##!/usr/bin/env python
'''
                      ::::::
                    :+:  :+:
                   +:+   +:+
                  +#++:++#++:::::::
                 +#+     +#+     :+:
                #+#      #+#     +:+
               ###       ###+:++#""
                         +#+
                         #+#
                         ###
'''
__author__ = "Alex Pujols"
__copyright__ = "TBD"
__credits__ = ["Alex Pujols"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alex Pujols"
__email__ = "alex.pujols@gmail.com"
__status__ = "Prototype"

'''
What does this code do?
'''

# Import modules declarations
import string
import json

# Function declarations

# Function for TBD

# Function for TBD

# Function for TBD

# Function for TBD

# Function for TBD


# Main code begins
_filename_ = 'data.json'

# Open the file data.json and read from it
with open(_filename_) as f:
    data = json.load(f)
# Create a dictionary index with the value "Name" and store in new list "names"
names = []
for i in data:
    name = i['Name']
    names.append(name)

# Set global vaiables

# Begin main code execution
