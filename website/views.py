from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ("this test work correctly for home page")
def about_view(request):
    return HttpResponse ("this test work correctly for about")
def contact_view(request):
    return HttpResponse ("this test work correctly for contact")