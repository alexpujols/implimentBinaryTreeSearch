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
Title	      :	{TBD}
Date		  :	{XX-XX-20XX}
Description   :	{TBD}
Options	      :	{TBD}
Notes	      :	{TBD}
''''''


# Import modules declarations
import string
import json

## Class declarations

# Class for TBD
class Node:
    """ A class that models attributes of people """

    def __init__(self, data):
        """ Initialize data categories """
        self.left = None
        self.right = None
        self.data = data
    # Method to insert new value into tree - inorder method
    def Insert(self, data):
        if self.data:                       # If parent node exists
            if data < self.data:            ## If value is less than parent node
                if self.left is None:       ### If left node is empty
                    self.left = Node(data)  #### Assign data value to left node
                else:                       ### If left node is NOT empty
                    self.left.Insert(data)  #### recurrsively left.insert data until empty left node is found
            elif data > self.data:          ## If value is greater than parent node
                if self.right is None:      ### If right node is empty
                    self.right = Node(data) #### Assign data value to right node
                else:                       ### If right node is NOT empty
                    self.right.Insert(data) #### recurrsively right.insert data until a value greater than parent node is encountered
        else:                               # If parent node does NOT exist
            self.data = data                ## Assign data value to parent node
    # Method to print tree values
    def PrintTree(self):
        if self.left:                       # If a left node value exists
            self.left.PrintTree()           ## recurrsively move left until at leftmost node
        print(self.data)                    # Print value active node data
        if self.right:                      # If right node value exists
            self.right.PrintTree()          ## recurrsively move right until at rightmost node



# Class for TBD

# Class for TBD

## Function declarations

# Function for TBD

# Function for TBD

# Function for TBD

# Function for TBD

# Function for TBD


### Main code begins ###

# Set global vaiables
_filename_ = 'data.json'

# Begin main code execution

# Open the file data.json and read from it
with open(_filename_) as f:
    data = json.load(f)
# Initialize arrays/class for data intake
names = []
people = Node(None)
# Read-in all JSON values
for i in data:
    name = i['Name']
    names.append(name)
    people.Insert(name)

people.PrintTree()

## Main code ends ###
