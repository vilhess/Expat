import streamlit as st

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://samyvilhes:Rt8qTQwzkN6ev5pN@cluster0.4mrsu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["commentaires"]

def insert_commentaire(school:str, year:int, comm:str, major:str):
    collection = db[school]
    full_comm = {
    "Année":year,
    "Options":major,
    "Commentaires":comm
    }
    collection.insert_one(full_comm)
    return 

def get_df_comments(school):

    collection = db[school]

    dic_df = {
        "Année":[],
        "Options":[],
        "Commentaires":[]
        }
    
    for doc in collection.find():
        dic_df['Année'].append(doc["Année"])
        dic_df['Options'].append(doc["Options"])
        dic_df['Commentaires'].append(doc["Commentaires"])

    return dic_df
