#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:54:20 2024

@author: jackkausch
"""

import pandas as pd


def ClassyAnd(class1,class2,dictionary,dataframe):
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
    mean = (dictionary.get(class1)+dictionary.get(class2))/2
    values = []
    for i in dataframe['value']:
        values.append(i)
    print(values)
    for i in values:
        i = i%mean
    print(values)
    dataframe['value'].transform(lambda x: x + mean)
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
   # print(dataframe)
    return(dataframe['name'])


def ClassyOr(class1,class2,dictionary,dataframe):
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
    print(dataframe)
    orMean = abs(dictionary.get(class1)+dictionary.get(class2)-(dictionary.get(class1)*dictionary.get(class2)))
    for i in dataframe['value']:
        i = abs(i)
        i = i%orMean
        return(dataframe)
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
    print(dataframe)
    return(dataframe['name'])


def ClassyNot(class1, dictionary, dataframe):
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
    print(dataframe)
    notMean = abs(1-dictionary.get(class1))
    print(dataframe)
    for i in dataframe['value']:
        i = abs(i)
        i = i%notMean
        return(dataframe)
    dataframe = dataframe.sort_values(by=['value'], ascending=True)
    print(dataframe)
    return(dataframe['name'])


classynames = pd.read_csv('hpo.embeddings54.csv')
classynames_dict = classynames.set_index('name')['value'].to_dict()    

#print(classynames['name'])

#ClassyNot('cell',classynames_dict,classynames)
#ClassyOr('pedal','abnormality',classynames_dict,classynames)
ClassyAnd('pedal','abnormality',classynames_dict,classynames)

#print(classynames_dict)