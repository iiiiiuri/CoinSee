from django.shortcuts import render

def index(request):
    return render(request, 'coin_see/index.html')