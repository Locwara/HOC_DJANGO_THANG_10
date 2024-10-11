from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_index(request):
    return HttpResponse('hi')
def get_index1(request):
    return render(request, 'home/index.html')
    