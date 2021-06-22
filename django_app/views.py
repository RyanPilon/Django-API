from django.http import JsonResponse
from django.shortcuts import render


def test_view(request):
    data = {
        "name": "test",
        "age": 13,
    }
    return JsonResponse(data)
