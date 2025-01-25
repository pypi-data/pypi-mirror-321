import dspy
from abc import abstractmethod
from Ombralis.core.datatypes import QueryWithEntities

class EntityReranker(dspy.Module):
    
    @abstractmethod
    def forward(self, query: QueryWithEntities) -> QueryWithEntities:
        raise NotImplementedError(
            f"EntityReranker {type(self).__name__} is missing the required 'forward' method."
        )