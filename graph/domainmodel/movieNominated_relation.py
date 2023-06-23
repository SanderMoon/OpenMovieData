from dataclasses import dataclass
from domainmodel.neo4j_node import Node
from domainmodel.neo4j_relation import Relation

@dataclass
class MovieNominatedForRelation(Relation):

    def __init__(self, movie: Node, oscar: Node):
        self.subject = movie
        self.object = oscar
        self.label = 'NOMINATED_FOR'

    def natural_keys(self) -> dict:
        return NotImplementedError("MovieNominatedForRelation.natural_keys() not implemented")