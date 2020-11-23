from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
def index(request):
    return JsonResponse({'aver': 'aaaaaa'})

