from rest_framework.pagination import PageNumberPagination


class SmallResultsSetPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000
