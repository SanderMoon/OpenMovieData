from dataclasses import dataclass
from graph.domainmodel.neo4j_node import Node
from graph.domainmodel.neo4j_relation import Relation

@dataclass
class MovieHasWonRelation(Relation):

    def __init__(self, movie: Node, oscar: Node):
        self.subject = movie
        self.object = oscar
        self.label = 'HAS_WON'

    def natural_keys(self) -> dict:
        return NotImplementedError("MovieHasWonRelation.natural_keys() not implemented")