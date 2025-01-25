from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.pagination import PageNumberPagination


class ALP:

    def __init__(self, request, data, serializer, context=None):
        self.request = request
        self.data = data
        self.serializer = serializer
        self.context = context or {}

    def ret(self):
        if bool(int(self.request.GET.get('distinct', 0))):
            self.data = self.data.distinct().order_by()
        if bool(int(self.request.GET.get('excel', 0))):
            return self.excel()
        if self.request.GET.get('limit') == '-1':
            return self.listing()
        return self.pagination()

    def pagination(self):
        paginator = Pagination()
        pg = paginator.paginate_queryset(self.data, self.request)
        self.data = self.serializer(pg, many=True, context=self.context).data
        return paginator.get_paginated_response(self.data)

    def listing(self):
        if 'fields' in self.request.GET:
            fields = self.request.GET.get('fields').split(' ')
            if 'values_list' in self.request.GET and int(self.request.GET.get('values_list')):
                if len(fields) == 1:
                    self.data = self.data.values_list(*fields, flat=True)
                else:
                    self.data = self.data.values_list(*fields)
            else:
                self.data = self.data.values(*fields)
        else:
            self.data = self.serializer(self.data, many=True, context=self.context).data
        return Response({'results': self.data}, status=HTTP_200_OK)

    def excel(self):
        fields = self.request.GET.get('fields', 'id').split(' ')
        self.data = self.data.values(*fields)
        return Response(self.data, status=HTTP_200_OK)


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 1000