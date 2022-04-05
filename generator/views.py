from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.



def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    characters = list('adsadfsdfsdfsdfafdafdasasdasdasdadscfgh')

    if request.GET.get('uppercase'):
        characters.extend(list('ASDSFSDFGVXFDGSDFSFSFRGER'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    lenght = 0
    for key, values in request.GET.lists():
        if key == 'lengh':
            lenght = values
        if key == 'uppercase':
            characters.extend(list('ASDSFSDFGVXFDGSDFSFSFRGER'))
        if key == 'Special':
            characters.extend(list('!@#$%^&*()'))
        if key == 'numbers':
            characters.extend(list('0123456789'))
    thepassword = ''
    for x in range(int(lenght[0])):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})
