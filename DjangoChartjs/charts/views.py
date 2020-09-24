from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

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