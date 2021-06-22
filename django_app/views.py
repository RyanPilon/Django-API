from django.http import JsonResponse
from django.shortcuts import render

#3rd party imports
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "name": "test",
            "age": 13,
        }
        return Response(data)

# def test_view(request):
#     data = {
#         "name": "test",
#         "age": 13,
#     }
#     return JsonResponse(data)
