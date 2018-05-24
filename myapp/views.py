from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def submit(request):
    info = request.POST['info']
    #here add code so that response from router is printed
    return HttpResponse(info+'Output')