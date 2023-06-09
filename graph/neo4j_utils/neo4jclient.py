from neo4j import GraphDatabase
from decouple import config
import os

class Neo4jClient:
    _instance = None

    @staticmethod
    def getInstance():
        if Neo4jClient._instance == None:
            Neo4jClient()
        return Neo4jClient._instance

    def __init__(self):
        if Neo4jClient._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            uri = os.getenv('NEO4J_URI')
            port = os.getenv('NEO4J_PORT')
            user = os.getenv('NEO4J_USER')
            password = os.getenv('NEO4J_PASSWORD')
            self.driver = GraphDatabase.driver(f"bolt://{uri}:{port}", auth=(user, password))
            Neo4jClient._instance = self

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters={}):
        with self.driver.session() as session:
            return list(session.run(query, parameters))