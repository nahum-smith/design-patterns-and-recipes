"""An Example of how to insert a document"""

import sys

from pymongo import MongoClient
from datetime import datetime
from pymongo.errors import ConnectionFailure

def main():
    """ Connect to MongoDB """
    try:
        c = MongoClient() # host="localhost", port=27017 are default arguments
        print("Connected successfully")
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: {}".format(e))
        sys.exit(1)
    # Get a Database handle to a database named "video"
    dbh = c["test"]

    # Demonstrate the db.connection property to retrieve a reference to the
    # Connection object, in case it goes out of scope.

    assert dbh._Database__client == c
    assert dbh._Database__name == 'test'
    print("Successfully set up a databse handle")

    user_doc = {
        "username": "blackblizzard",
        "firstname": "John",
        "lastname": "Snow",
        "dob": datetime(2009, 4, 12),
        "email": "knownothing@got.com",
        "dead": False
    }
    users = dbh.users
    users.insert_one(user_doc)
    print("Successfully inserted document: {}".format(user_doc))

if __name__ == "__main__":
    main()
