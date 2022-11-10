from django.conf import settings
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from address.models import Address
from person.models import Person
from person.forms import PersonForm
from rest_framework import generics
from .serializers import PersonSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    CreateView,
)

User = settings.AUTH_USER_MODEL


@login_required
def index(request):
    return render(request,'example/index.html')

@login_required
def sucesso3(request):
    return render(request, 'sucesso.html')

@login_required
def homeperson(request):
    success = False
    addresses = Address.objects.all()
    if settings.GOOGLE_API_KEY:
        google_api_key_set = True
    else:
        google_api_key_set = False

    if request.method == 'POST':
        form = PersonForm(request.user, request.POST, request.FILES)

        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.user = request.user
            prestador.save()
            return sucesso3(request)
    else:
        form = PersonForm(request.user)

    context = {'form': form,
               'google_api_key_set': google_api_key_set,
               'success': success,
               'addresses': addresses}


    return render(request, 'example/home_map.html', context)
#C:\Users\thiago.fideles\Documents\lojadaneidy\templates\example


#API to get all records
@login_required
class PersonAPIView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer    
