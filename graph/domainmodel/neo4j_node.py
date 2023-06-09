from dataclasses import dataclass, asdict
from domainmodel.neo4j_object import Neo4jObject
import math

@dataclass
class Node(Neo4jObject):

    def __init__(self):
        self._fill_null()

    def __str__(self):
        return f'Node(label={self.label}, properties={self.get_properties()})'

    def _generate_key_string_and_params(self):
        keys = self.natural_keys()
        keys_string = " AND ".join(f"n.{key} = ${key}" for key in keys.keys())
        parameters = {key: value for key, value in keys.items()}
        return keys_string, parameters

    def create(self):
        properties = asdict(self)
        properties = {k: v for k, v in properties.items() if v is not None}
        properties_string = ", ".join(f"{key}: ${key}" for key in properties.keys())
        query = f"MERGE (n:{self.label} {{{properties_string}}}) RETURN n"
        result = self.execute_query(query, properties)
        return result[0] if result else None
    
    def read(self):
        keys_string, parameters = self._generate_key_string_and_params()
        query = f"MATCH (n:{self.label}) WHERE {keys_string} RETURN n"
        result = self.execute_query(query, parameters)
        return result[0] if result else None

    def update(self):
        properties = asdict(self)
        properties = {k: v for k, v in properties.items() if v is not None}
        properties_string = ", ".join(f"n.{key} = ${key}" for key in properties.keys())
        keys_string, parameters = self._generate_key_string_and_params()
        query = f"MATCH (n:{self.label}) WHERE {keys_string} SET n = {{{properties_string}}} RETURN n"
        parameters = {**parameters, **properties}
        result = self.execute_query(query, properties)
        return result[0] if result else None
    
    def delete(self):
        keys_string, parameters = self._generate_key_string_and_params()
        query = f"MATCH (n:{self.label}) WHERE {keys_string} DELETE n"
        result = self.execute_query(query, parameters)
        return result[0] if result else None   
     
    def create_index_if_not_exists(self):
        keys_string = ", ".join(f"(n.{key})" for key in self.natural_keys().keys())
        query = f"CREATE INDEX IF NOT EXISTS FOR (n:{self.label}) ON {keys_string}"
        result = self.execute_query(query)
        return result[0] if result else None   

    def _fill_null(self):
        for key, value in asdict(self).items():
            # check if dtype is float
            if isinstance(value, float) or isinstance(value, int):
                if math.isnan(value):
                    setattr(self, key, None)
            if isinstance(value, str):
                if value is None:
                    setattr(self, key, None)