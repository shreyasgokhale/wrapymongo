#!/usr/bin/env python3

"""
MongoDB API Wrapper

@author:  Shreyas Gokhale
@contact: shreyas6gokhale@gmail.com
"""

import pymongo


class driver:

    def __init__(self, link=None, username=None, password=None, authdb='admin'):
        """
        Define client for object
        :param link: MongoDB link for connection
        """
        # By default, DB is created on localhost port 27017, no username - password 
        self.client = pymongo.MongoClient(link, username=username, password=password, authSource=authdb)   
        
    def defineDB(self, database_name="database"):
        """
        Defines a database

        :param database_name: Name of the database
        """
        self.database_name = database_name
        self.database = self.client[database_name]

    def defineCollection(self, collection_name="collection"):
        """
        Defines a collection (Table equivalant of MySQL)

        :param collection_name:
        """
        self.collection_name = collection_name
        # Define collection with this name
        self.collection = self.database[self.collection_name]

    def checkCollectionExists(self):
        """
         Check if the collection exists in current db
        :return: True if exists
        """
        self.database.list_collection_names()
        if self.collection_name in self.database.list_collection_names():
            return True
        else:
            return False

    def dropCollection(self):
        """
        Drop collection

        """
        self.collection.drop()
        return True

    def dropDatabase(self):
        """
        Drop database

        """
        if (self.client.drop_database(self.database_name) == True):
            self.collection = None
            self.database = None
            self.database_name = None
            self.collection_name = None
            print("Collection Dropped Successfully!")
            return True
        else:
            print("Collection Does not Exist!")
            return False

    def insertOneRecord(self, record):
        """
        Insert record in collection.
        :param records: JSON object with records
        """
        try:
            result = self.collection.insert_one(record)
            print("Insert Successful")
            return True               # Return ObjectID(s)

        except Exception as e:
            print("An error occured:" + str(e))
            return False

    def insertRecords(self, records):
        """
        Insert multiple (JSON) records in the collection.
        :param records: JSON object with records
        """
        try:
            result = self.collection.insert_many(records)
            # print("Insert Successful")
            return True

        except Exception as e:
            print("An error occured:" + str(e))
            return False

    def insertWithoutDuplicates(self, records, query):
        """
        Insert multiple (JSON) records in the collection.
        Do not add if the record already exists
        :param records: JSON object with records
        """
        try:
            result = self.collection.update_many(
                filter=query, update=records, upsert=True)
            # print("Insert Successful")
            return True

        except Exception as e:
            print("An error occured:" + str(e))
            return False

    def findRecord(self, findQuery={}, maskingquery={'_id': False}):
        """
        Find multiple records
        :param findQuery: SON object stating what you want in the table. eg: { id : 1} means all the records with id = 1
        :param maskingquery: SON object stating what you want to omit from the results. By Default, omit '_id' from results.
        :return: list containing all the table values
        """
        try:
            res = list(self.collection.find(
                findQuery, projection=maskingquery))
            if res:
                print("Find Success")
                return res
            else:
                print("No matching records exist")
                return False

        except Exception as e:
            print("An error occured:" + str(e))

    def findLatestRecord(self, findQuery={}, maskingquery={'_id': False}):
        """
        Find one latest record
        :param findQuery: SON object stating what you want in the table. eg: { id : 1} means all the records with id = 1
        :param maskingquery: SON object stating what you want to omit from the results. By Default, omit '_id' from results.
        :return: list containing all the table values
        """
        try:
            res = self.collection.find_one(
                findQuery, projection=maskingquery, sort=[('_id', -1)])
            if res:
                print("Find_one latest Success")
                return res

            else:
                print("No matching records exist")
                return False

        except Exception as e:
            print("An error occured:" + str(e))


    def updateOneRecord(self, record_to_update, update_value, force=False):
        """

        :param record_to_update: JSON Object for search
        :param update_value: New value of the key.
        """
        try:

            setter = {}
            setter["$set"] = update_value
            result = self.collection.update_one(
                record_to_update, setter, upsert=force)
            return result.acknowledged

        except Exception as e:
            print("An error occured:" + str(e))
            return False

    
    def sortRecords(self, sortSON, limit = 100):
        """
        Aggregate based on given pipeline.

        :param sortSON: SON object stating your operations.
        :param limit: Limit records, by default 100
        :return: result
        """
        try:
            result = list(self.collection.find().sort(sortSON).limit(limit))
            return result

        except Exception as e:
            print("An error occured:" + str(e))
