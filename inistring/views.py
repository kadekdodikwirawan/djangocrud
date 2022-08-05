from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    if(request.GET.get('string') ):
        return HttpResponse(toCamelCase(request.GET.get('string')))
    else:
        return HttpResponse('Masukan parameter number pada url (contoh: http://127.0.0.1:8000/inistring/?string=iNi-aDalah-stRing)')
def toCamelCase(value):
    arr = []
    new_array = []
    if value.__contains__('_'):
        arr = value.split('_')
    if value.__contains__('-'):
        arr = value.split('-')
    if value.__contains__(' '):
        arr = value.split('')
    for i in range(len(arr)):
        new_array.append(arr[i].capitalize())
    return new_array