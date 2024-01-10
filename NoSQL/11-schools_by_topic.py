#!/usr/bin/env python3
'''
Module for retrieving data from mongodb
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Function that returns the list of school
    '''
    crusor = mongo_collection.find({'topics': topic})
    school_list = list(crusor)
    return school_list
