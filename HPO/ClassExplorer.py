#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:54:20 2024

@author: jackkausch
"""

import pandas as pd


def ClassyAnd(class1,class2,dictionary,dataframe):
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
    mean = abs((dictionary.get(class1)+dictionary.get(class2))/2)
    values = []
    for i in dataframe['value']:
        values.append(i%mean)
    dataframe['value'] = values

    dataframe = dataframe.sort_values(by=['value'], ascending=False)
    name= []
    for i in dataframe['name']:
        name.append(i)
    return(dataframe)
    


def ClassyOr(class1,class2,dictionary,dataframe):
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
    orMean = abs(dictionary.get(class1)+dictionary.get(class2)-(dictionary.get(class1)*dictionary.get(class2)))
    values = []
    for i in dataframe['value']:
        values.append(i%orMean)
    dataframe['value'] = values

    dataframe = dataframe.sort_values(by=['value'], ascending=False)
    name= []

    for i in dataframe['name']:
        name.append(i)
    return(dataframe)
    


def ClassyNot(class1, dictionary, dataframe):
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
    notMean = abs(1-dictionary.get(class1))
    values = []
    for i in dataframe['value']:
        values.append(i%notMean)
    dataframe['value'] = values
       
    dataframe = dataframe.sort_values(by=['value'], ascending=False)
    name= []

    for i in dataframe['name']:
        name.append(i)
    return(dataframe)
    


classynames = pd.read_csv('human.phenotype.ontology.embeddings.csv')
classynames_dict = classynames.set_index('name')['value'].to_dict()    


query1 = ClassyNot('MA:0000538',classynames_dict,classynames)
query2 = ClassyOr('chew','http://purl.obolibrary.org/obo/UBERON_0004727',classynames_dict,classynames)
query3 = ClassyAnd('pedal','abnormality',classynames_dict,classynames)

print(query1)

