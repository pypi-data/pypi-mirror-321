from .document_search import DocumentSearchService
from .paginated_search import PaginatedSearchService
from .memsum_summary import SummarizationService
from .single_paper_search import SinglePaperService

class EndocClient:
    def __init__(self, api_key: str):
        self._summarization_service = SummarizationService(api_key)
        self._document_search_service = DocumentSearchService(api_key)
        self._paginated_search_service = PaginatedSearchService(api_key)
        self._single_paper_service = SinglePaperService(api_key)

    def summarize(self, id_value: str):
        return self._summarization_service.summarize_paper(id_value)

    def document_search(
        self,
        ranking_variable: str,
        keywords=None
    ):
        return self._document_search_service.search_documents(
            ranking_variable, keywords
        )

    def paginated_search(
        self,
        paper_list,
        keywords=None
    ):
        return self._paginated_search_service.paginated_search(
            paper_list, keywords
        )

    def single_paper(self, id_value: str):
        return self._single_paper_service.get_single_paper(id_value)