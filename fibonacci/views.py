

# Create your views here.
from django.http import HttpResponse


def index(request):
    if(request.GET.get('number') ):
        fibo_numbers =  fibonacci(int(request.GET.get('number')))
        return HttpResponse(fibo_numbers, content_type="application/json")
    else:
        return HttpResponse('Masukan parameter number pada url (contoh: http://127.0.0.1:8000/fibonacci/?number=8)')
def fibonacci(value):
    fibo_number = []
    count = 0
    n1 = 0
    n2 = 1
    while count < value:
        fibo_number.append(n1)
        last_number = n1 + n2
        n1 = n2
        n2 = last_number
        count += 1
    return fibo_number