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
import netmiko
# Create your views here.
def submit(request):
    command = request.POST['info']
    #here add code so that response from router is printed
    try:
        net_connect = netmiko.ConnectHandler(
            device_type='cisco_ios',
            ip='192.168.1.10',
            username='cisco',
            password='cisco',
            # port=22,
            # global_delay_factor=2
        )
        net_connect.enable()
        #print('Connection successful')
        #print(net_connect)
        result = net_connect.send_command(command)
        #print(result)
        net_connect.disconnect()
        return HttpResponse(result.format())
    except netmiko.NetMikoTimeoutException as e:  # router getting timed out
        print(e)
    except netmiko.NetMikoAuthenticationException as e:
        print('AuthException')

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
