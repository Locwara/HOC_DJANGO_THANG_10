from django.shortcuts import render

# Create your views here.
def get_baiviet(request):
    return render(request, 'post/baiviet.html')