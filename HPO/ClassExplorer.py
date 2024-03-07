#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:54:20 2024

@author: jackkausch
"""

import pandas as pd


dataframe = pd.read_csv('human.phenotype.ontology.embeddings.csv')
classynames_dict = dataframe.set_index('name')['value'].to_dict()    


def ClassyAnd(class1,class2):
    mean = abs((classynames_dict.get(class1)*classynames_dict.get(class2))/2)
    values = []
    for i in dataframe['value']:
        values.append(i%mean)
    dataframe['value'] = values

    dataframe.sort_values(by=['value'], ascending=False)
    name= []
    for i in dataframe['name']:
        name.append(i)
    return(dataframe)
    

def ClassyOr(class1,class2,):
    orMean = abs(classynames_dict.get(class1)+classynames_dict.get(class2)-(classynames_dict.get(class1)*classynames_dict.get(class2)))
    values = []
    for i in dataframe['value']:
        values.append(i%orMean)
    dataframe['value'] = values

    dataframe.sort_values(by=['value'], ascending=False)
    name= []

    for i in dataframe['name']:
        name.append(i)
    return(dataframe)
    


def ClassyNot(class1):
    notMean = abs(1-classynames_dict.get(class1))
    values = []
    for i in dataframe['value']:
        values.append(i%notMean)
    dataframe['value'] = values
       
    dataframe.sort_values(by=['value'], ascending=False)
    name= []

    for i in dataframe['name']:
        name.append(i)
    return(dataframe)

def Dictify(df):
    df.set_index('name')['value'].to_dict()
    

classynames = pd.read_csv('human.phenotype.ontology.embeddings.csv')


classynames_dict = classynames.set_index('name')['value'].to_dict()    


query1 = ClassyNot('MA:0000538')
query2 = ClassyOr('MA:0000538','http://purl.obolibrary.org/obo/UBERON_0004727')
query3 = ClassyAnd('pedal','abnormality')




print(query3)
print()