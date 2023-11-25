from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'doctor/index.html')