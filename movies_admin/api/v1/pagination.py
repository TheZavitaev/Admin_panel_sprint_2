from rest_framework import pagination
from rest_framework.response import Response


class PageNumberPaginationWithCount(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response(
            {
                'required': {
                    'count': self.page.paginator.count,
                    'total_pages': self.page.paginator.num_pages,
                    'prev': self.get_previous_link(),
                    'next': self.get_next_link(),
                    'results': data
                }
            }
        )
