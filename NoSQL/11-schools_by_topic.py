#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """
     Returns:
        A list of schools that have the given topic in their 'topics' field.
    """

    schools = mongo_collection.find({"topics": topic})
    return list(schools)
