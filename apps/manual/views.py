from django.shortcuts import render

# Create your views here.

def manual (request):
    return render(request, 'manual/manual.html')

