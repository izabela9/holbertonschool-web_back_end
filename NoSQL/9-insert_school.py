#!/usr/bin/env python3
'''
Module for retrieving data from mongodb
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Function to insert a document
    '''
    inserted_doc = mongo_collection.insert_one(kwargs)
    return inserted_doc.inserted_id
