from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.forms import *
from django.http import HttpResponseRedirect
# Create your views here.
def submit(request):
    info = request.POST['info']
    #here add code so that response from router is printed
    return HttpResponse(info+'-NetmikoOutput Expected Here')

@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user}
    )