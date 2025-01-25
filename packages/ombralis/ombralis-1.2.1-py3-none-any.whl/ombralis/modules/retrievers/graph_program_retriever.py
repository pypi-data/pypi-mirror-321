import dspy
from abc import abstractmethod
from typing import Union
from Ombralis.core.datatypes import Query, QueryList, QueryWithGraphPrograms

class GraphProgramRetriever(dspy.Module):
    
    @abstractmethod
    def forward(self, query_or_queries: Union[Query, QueryList]) -> QueryWithGraphPrograms:
        raise NotImplementedError(
            f"GraphProgramRetriever {type(self).__name__} is missing the required 'forward' method."
        )