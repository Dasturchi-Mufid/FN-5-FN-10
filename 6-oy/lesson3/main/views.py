from django.shortcuts import render
from django.http import HttpResponse

def salom_ber(req):
    return HttpResponse('<h1>Assalomu alaykum</h1>')