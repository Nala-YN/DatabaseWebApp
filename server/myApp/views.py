import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def response_login(request):
    data=json.loads(request.body)
    if data.get("username")=="114514" and data.get("password")=="1919810":
        response={'success':True}
    else:
        response={'success':False}
    return JsonResponse(response)