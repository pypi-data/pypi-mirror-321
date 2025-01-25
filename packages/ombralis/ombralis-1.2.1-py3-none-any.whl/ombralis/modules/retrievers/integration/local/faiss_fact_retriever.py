import dspy
import numpy as np
from enum import Enum
from typing import Optional, Union
import faiss
from Ombralis.memory import FactMemory
from Ombralis.embeddings import Embeddings
from Ombralis.core.datatypes import Query, QueryList, QueryWithFacts
from Ombralis.modules.retrievers import FactRetriever
from Ombralis.core.pipeline import Pipeline

class EmbeddingsDistance(str, Enum):
    Cosine = "cosine"
    Euclidean = "euclidean"

class FAISSFactRetriever(FactRetriever):
    """
    A class for retrieving facts using FAISS (Facebook AI Similarity Search) and embeddings.

    Parameters:
        fact_memory (FactMemory): An instance of FactMemory class which stores the facts.
        embeddings (Embeddings): An instance of Embeddings class which is used to convert text into numerical vectors.
        distance (str, optional): The distance metric to use for similarity search. Should be either "cosine" or "euclidean". Defaults to "cosine".
        max_distance (float, optional): The maximum distance threshold for considering a fact as a match. Defaults to 0.7.
        k (int, optional): The number of nearest neighbors to retrieve. Defaults to 5.
        reverse (bool, optional): Weither or not to reverse the final result. Default to True.
        reranker (Optional[Pipeline], optional): An instance of Pipeline class which is used to re-rank the retrieved facts. Defaults to None.
    """
    
    def __init__(
            self,
            fact_memory: FactMemory,
            embeddings: Embeddings,
            distance: str = "cosine",
            max_distance: float = 0.7,
            k: int = 5,
            reverse: bool = True,
            reranker: Optional[Pipeline] = None,
        ):
        self.fact_memory = fact_memory
        self.embeddings = embeddings
        if distance == EmbeddingsDistance.Cosine:
            self.distance = EmbeddingsDistance.Cosine
        elif distance == EmbeddingsDistance.Euclidean:
            self.distance = EmbeddingsDistance.Euclidean
        else:
            raise ValueError("Invalid distance provided, should be cosine or euclidean") 
        self.max_distance = max_distance
        self.reranker = reranker
        self.k = k
        self.reverse = reverse
        vector_dim = self.embeddings.dim
        if self.distance == "euclidean":
            self.index = faiss.IndexFlatL2(vector_dim)
        else:
            self.index = faiss.IndexFlatIP(vector_dim)
    
    def forward(self, query_or_queries: Union[Query, QueryList]) -> QueryWithFacts:
        """
        Retrieve facts based on the given query.

        Parameters:
            query_or_queries (Union[Query, QueryList]): An instance of Query or QueryList class which contains the query text.

        Returns:
            QueryWithFacts: An instance of QueryWithFacts class which contains the query text and the retrieved facts.
        """
        if not isinstance(query_or_queries, (Query, QueryList)):
            raise ValueError(f"{type(self).__name__} input must be a Query or QueryList")
        if isinstance(query_or_queries, Query):
            queries = QueryList()
            queries.queries = [query_or_queries.query]
        else:
            queries = query_or_queries
        result = QueryWithFacts()
        result.queries.queries = queries.queries
        embeddings_map = self.fact_memory._facts_embeddings
        vectors = np.array(list(embeddings_map.values()), dtype="float32")
        if vectors.shape[0] > 0:
            self.index.reset()
            if self.distance == "euclidean":
                faiss.normalize_L2(vectors)
            self.index.add(vectors)
            query_vectors = np.array(self.embeddings.embed_text([q.query for q in queries.queries]), dtype="float32")
            distances, indexes = self.index.search(query_vectors, min(vectors.shape[0], self.k))
            for i in range(min(vectors.shape[0], self.k)):
                if distances[0][i] < self.max_distance:
                    fact_index = indexes[0][i]
                    fact_id = list(embeddings_map.keys())[fact_index]
                    fact = self.fact_memory.get_facts(fact_id).facts[0]
                    result.facts.append(fact)
                else:
                    break
            if self.reranker is not None:
                result = self.reranker(result)
            if self.reverse:
                result.facts.reverse()
        return result