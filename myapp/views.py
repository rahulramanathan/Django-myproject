#from django.shortcuts import render
from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
#from django.template import RequestContext
#from myapp.forms import *
#from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .netmikocode import fn
# Create your views here.
def submit(request):
    command = request.POST['info']
    #here add code so that response from router is printed
    return HttpResponse(fn(command), content_type='text/plain')

@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user}
    )

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
