from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

moneys = [20, 20, 50, 5, 5, 100]
n = len(moneys)
def index(request):
    ticket_price = request.GET.get('ticket_price')
    cash = request.GET.get('cash')
    changes = isSubsetSum(ticket_price, cash)
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

def isSubsetSum(ticket_price, cash):
    sum = int(cash) - int(ticket_price)
    subset = ([[False for i in range(sum + 1)] for i in range(n + 1)])
    for i in range(n + 1):
        subset[i][0] = True
        for i in range(1, sum + 1):
            subset[0][i]= False
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j<moneys[i-1]:
                    subset[i][j] = subset[i-1][j]
                if j>= moneys[i-1]:
                    subset[i][j] = (subset[i-1][j] or subset[i - 1][j-moneys[i-1]])
    if subset[n][sum] : return 'Ada kembalian'
    else: return 'Tidak ada kembalian'