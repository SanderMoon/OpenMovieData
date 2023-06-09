
from dataclasses import dataclass
from domainmodel.neo4j_node import Node
from domainmodel.neo4j_relation import Relation

@dataclass
class ActedInRelation(Relation):

    def __init__(self, person: Node, movie: Node):
        self.subject = person
        self.object = movie
        self.label = 'ACTED_IN'

    def natural_keys(self) -> dict:
        return NotImplementedError("ActedInRelation.natural_keys() not implemented")