from django.http import HttpResponse
from django.shortcuts import render

def glowna(request):
    return render(request, 'Glowna.html')

def kontakt(request):
    return render(request, 'Kontakt.html')
    
def wozki(request):
    return render(request, 'Wozki.html')

def balkoniki(request):
    return render(request, 'Balkoniki.html')

def sanitarny(request):
    return render(request, 'Sanitarny.html')

def sportowo(request):
    return render(request, 'Sportowo.html')

def szyja(request):
    return render(request, 'Szyja.html')

def kregoslup(request):
    return render(request, 'Kregoslup.html')

def konczynagorna(request):
    return render(request, 'Konczynagorna.html')

def wypozyczalnia(request):
    return render(request, 'Wypozyczalnia.html')

def konczynadolna(request):
    return render(request, 'Konczynadolna.html')

def kompresoterapia(request):
    return render(request, 'Kompresoterapia.html')

def pieluchomajtki(request):
    return render(request, 'Pieluchomajtki.html')

def sprzetmedyczny(request):
    return render(request, 'Sprzetmedyczny.html')

def obuwiemedyczne(request):
    return render(request, 'Obuwiemedyczne.html')
