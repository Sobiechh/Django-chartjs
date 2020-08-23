from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User

#restframework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
        "sales": 100,
        "customers": 10,
        }
        return Response(data)