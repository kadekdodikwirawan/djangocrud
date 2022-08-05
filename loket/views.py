from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

moneys = [20, 20, 50, 5, 5, 100]
n = len(moneys)
def index(request):
    ticket_price = request.GET.get('ticket_price')
    cash = request.GET.get('cash')
    changes = isChangeReady(ticket_price, cash)
    if(ticket_price and cash):
        return render(request, "loket.html",
        {
            'cash': cash,
            'ticket_price': ticket_price,
            'moneys': moneys,
            'changes': changes
        }
        )
    else:
        return HttpResponse("Masukan parameter ticket_price dan cash. (contoh: http://127.0.0.1:8000/loket?ticket_price=25&cash=100)")

def isChangeReady(ticket_price, cash):
    sum = int(cash) - int(ticket_price)
    arr = np.array(moneys)
    changes = (np.cumsum(arr)<=5).argmin()
    return arr