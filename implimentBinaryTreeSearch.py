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
Title	      :	Implimenting a Binary Tree
Date		  :	2-13-20X21
Description   :	Imports data from a JSON file, loads into a binary tree, and manipulates via various methods
Options	      :	{TBD}
Notes	      :	{TBD}
'''

# Import modules declarations
import string
import json
import sys

## Class declarations

# Class for people Node
class Node:
    # A class that models attributes of people

    def __init__(self, data):
        # Initialize data categories
        self.left = None
        self.right = None
        self.data = data
        self.count = 1
    # Method to insert new value into tree - inorder method
    def InsertTreeNode(self, data):
        if self.data:                               # If parent node exists
            if data < self.data:                    ## If value is less than parent node
                if self.left is None:               ### If left node does not exist
                    self.left = Node(data)          #### Assign data value to left node
                else:                               ### If left node is NOT empty
                    self.left.InsertTreeNode(data)  #### recurrsively left.insert data until empty left node is found
            elif data > self.data:                  ## If value is greater than parent node
                if self.right is None:              ### If right node does not exist
                    self.right = Node(data)         #### Assign data value to right node
                else:                               ### If right node is NOT empty
                    self.right.InsertTreeNode(data) #### recurrsively right.insert data until a value greater than parent node is encountered
            elif data == self.data:                 ## If value is equal to parent node
                self.count += 1                     ## Increment the counter for duplicates
                if self.right is None:              ### If right node does not exist
                    self.right = Node(data)         #### Assign data value to right node
                else:                               ### If right node is NOT empty
                    self.right.InsertTreeNode(data) #### recurrsively right.insert data until a value greater than parent node is encountered
        else:                                       # If parent node does NOT exist
            self.data = data                        ## Assign data value to parent node
    # Method to search the tree
    def SearchTree(self, value):
        if value < self.data:                       # If value to compare is less than parent node check the left side
            if self.left is None:                   ## If left node is empty we've reached the end
                return False
            return self.left.SearchTree(value)      ## Recurrsively call SearchTree until either the value is found or last node encountered
        elif value > self.data:                     # If value to compare is greater than parent node check the right side
            if self.right is None:                  ## If the node on the right does not exist
                return False
            return self.right.SearchTree(value)     ## Recurrsively call SearchTree until value until value is found or last node encountered
        else:                                       # If value to compare is not less OR greater than node value
            return True
    # Method to print tree values
    def PrintTree(self):
        if self.left:                               # If a left node value exists
            self.left.PrintTree()                   ## recurrsively move left until at leftmost node
            print(f"\t{self.count}\t{self.data}")   # Print value active node data
        if self.right:                              # If right node value exists
            self.right.PrintTree()                  ## recurrsively move right until at rightmost node

## Function declarations

# Function for validate filename location
def load_file_data(filename):
    print("-- Checking to see if file exists --")
    while True:
        try:
            # Open the file data.json and read from it
            with open(filename) as f:
                data = json.load(f)
            print(f"\t{filename} was found!")
            break
        except:
            sys.exit("\tThe file does not exist!")
    return data

### Main code begins ###

# Begin main code execution
filename = str(input("Please enter the name of the JSON file you wish to load: "))
data = load_file_data(filename)
# Initialize arrays/class for data intake
people = Node(None)
# Read-in all JSON values
print("-- Reading data into binary tree --")
try:
    for i in data:
        name = i['Name']
        people.InsertTreeNode(name)
except:
    sys.exit("\tError, unable to find specified fields!")
# Print results of the tree
print("-- Printing results of the tree --")
people.PrintTree()
### Main code ends ###
