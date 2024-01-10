#!/usr/bin/env python3
'''
Module for retrieving data from mongodb
'''


def list_all(mongo_collection):
    '''
    Function to get all documents in a collection
    '''
    crusor = mongo_collection.find({})
    list_doc = list(crusor)
    return list_doc
