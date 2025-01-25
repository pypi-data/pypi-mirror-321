import dspy
from abc import abstractmethod
from Ombralis.core.datatypes import QueryWithGraphPrograms

class GraphProgramReranker(dspy.Module):
    
    @abstractmethod
    def forward(self, query: QueryWithGraphPrograms) -> QueryWithGraphPrograms:
        raise NotImplementedError(
            f"GraphProgramReranker {type(self).__name__} is missing the required 'forward' method."
        )