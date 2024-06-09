from django.shortcuts import render

# Create your views here.

def paginainicial_view(request):
    return render(request, 'paginainicial/index.html')
