from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})

def trad(request):
    return render(request,'trad.html',{})

def media(request):
    return render(request,'media.html',{})


def trad_gallery(request):
    return render(request,'trad_gallery.html',{})

def white_gallery(request):
    return render (request, 'white_gallery.html',{})

def ict_pics(request):
    return render(request,'ict_pics.html',{})