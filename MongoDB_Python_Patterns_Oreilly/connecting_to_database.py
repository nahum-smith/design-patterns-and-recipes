"""An Example of how to connect to MongoDB"""

import sys

from pymongo import MongoClient
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
    dbh = c["video"]
    print(dbh.__dict__)

    # Demonstrate the db.connection property to retrieve a reference to the
    # Connection object, in case it goes out of scope.

    assert dbh._Database__client == c
    assert dbh._Database__name == 'video'
    print("Successfully set up a databse handle")

if __name__ == "__main__":
    main()
