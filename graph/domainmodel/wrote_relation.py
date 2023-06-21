from dataclasses import dataclass
from graph.domainmodel.neo4j_node import Node
from graph.domainmodel.neo4j_relation import Relation

@dataclass
class WroteRelation(Relation):

    def __init__(self, person: Node, movie: Node):
        self.subject = person
        self.object = movie
        self.label = 'WROTE'

    def natural_keys(self) -> dict:
        return NotImplementedError("WroteRelation.natural_keys() not implemented")