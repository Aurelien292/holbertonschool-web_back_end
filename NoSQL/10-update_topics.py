#!/usr/bin/env python3
"""change topics of a school """


def update_topics(mongo_collection, name, topics):
    """Change topics of a school document based on the name."""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
