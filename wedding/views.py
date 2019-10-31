from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})

def trad(request):
    return render(request,'trad.html',{})

def media(request):
    return render(request,'media.html',{})

def gallery(request):
    return render(request,'gallery.html',{})