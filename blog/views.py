# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.

def home(request):
    nama = "TASYA AMELIA PUTRI"
    buah = {'Semangka', 'Pear','Jeruk'}
    return render(request, 'index.html', {'nama':nama, 'buah':buah})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')
    
    

