#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fuzzy Logic Retrieval

Really simple baby script. Can perform the operations successfully. 

Things to discuss: precedence? Probably not important unless you are a mathematician.

Also we should discuss how the user should manipulate nested expressions.

Created on Sat Oct 28 10:24:12 2023

@author: jackkausch
"""

import pandas as pd

##These are functions which mimic the Boolean operators in a Fuzzy Logic Implementation


def fuzzyand(class1,class2):
    return class1*class2

def fuzzynot(class1):
    return 1-class1

def fuzzyor(class1, class2):
    return class1+class2-class1*class2
    ## This comes from the ability to define OR based on AND and NOT
    ## But in fuzzy logic this can be reduced with a simple algebra
    ## This implementation was taken from wikipedia
    ## x OR y = NOT( AND( NOT(x), NOT(y) ) )
    ## x OR y = NOT( AND(1-x, 1-y) )
    ## x OR y = NOT( (1-x)*(1-y) )
    ## x OR y = 1-(1-x)*(1-y)
    ## x OR y = x+y-xy

def fuzzyext(query, min, max):
    return 
    

## NOTA BENE: One of the questions is whether we want to define logical precedence or ignore it

##The data is loaded into two dataframes, one for natural language labels, and one for uris

fuzzynames = pd.read_csv("fuzzy_sets_names.csv", sep=',',
                         quotechar='"', escapechar="\\")
fuzzyuris = pd.read_csv("fuzzy_sets.csv", sep=',',
                        quotechar='"', escapechar="\\")


print("The following is the list of classes to select from the ontology")
list = list(fuzzynames.columns.values)
list.pop(0)
print(list)

## The following is a sample implementation of the three operators. It states the following
## Boolean formula: NOT('Food' OR ('SloppyGiuseppe' AND 'SauceTopping')) <<<<<<<<
## It shows how all three operators can be nested within each other. 
## Any possible set of operations of continuing complexity are possible, the only question is
## what order of precedence they should have.

## Boolean formula: NOT('Food' OR ('SloppyGiuseppe' AND 'SauceTopping')):
operation = fuzzynot(fuzzyor(fuzzyand(fuzzynames[list[1]],fuzzynames[list[2]]),fuzzynames[list[3]]))

## Now a new set of values for the instances has been composed from the operation
## We bind the instances to the new values in a new dataframe 
instances = fuzzynames["Instances"]
print(instances)

data = {"instances":instances,"values":operation}

frame = pd.DataFrame(data)

## The instances are sorted in ascending order
print(frame.sort_values("values",ascending=False))

##If necessary, the URIs from the fuzzyURIs dataframe can similarly be bound to the output



