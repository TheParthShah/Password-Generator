from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upperCase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialCharacters'):
        characters.extend(list('!@#$%^&*()_+-'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    legthOfPassword = int(request.GET.get('legthOfPassword',12))
    password = ''
    for x in range(legthOfPassword):
        password += random.choice(characters)
    return render(request, 'generator/password.html',{'password':password})

def about(request):
    return render(request, 'generator/about.html')