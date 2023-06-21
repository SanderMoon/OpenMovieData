from dataclasses import dataclass
from graph.domainmodel.neo4j_node import Node
from graph.domainmodel.neo4j_relation import Relation

@dataclass
class HasGenreRelation(Relation):

    def __init__(self, movie: Node, genre: Node):
        self.subject = movie
        self.object = genre
        self.label = 'HAS_GENRE'

    def natural_keys(self) -> dict:
        return NotImplementedError("HasGenreRelation.natural_keys() not implemented")