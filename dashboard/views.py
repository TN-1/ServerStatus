from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):

    if request.user.is_authenticated:
        auth = True
        return render(request, 'dashboard/index.html', {'auth': auth})
    else:
        return HttpResponseRedirect(reverse('login'))