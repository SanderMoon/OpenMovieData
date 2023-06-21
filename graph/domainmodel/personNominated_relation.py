from dataclasses import dataclass
from graph.domainmodel.neo4j_node import Node
from graph.domainmodel.neo4j_relation import Relation

@dataclass
class PersonNominatedForRelation(Relation):

    def __init__(self, person: Node, oscar: Node):
        self.subject = person
        self.object = oscar
        self.label = 'NOMINATED_FOR'

    def natural_keys(self) -> dict:
        return NotImplementedError("PersonNominatedRelation.natural_keys() not implemented")