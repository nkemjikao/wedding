from django.shortcuts import render


def home(request):
    
    return render(request, 'index.html', {})

def trad(request):
    return render(request,'trad.html',{})
