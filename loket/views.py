from itertools import chain
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

moneys = [20, 20, 50, 5, 5, 100]
n = len(moneys)
def index(request):
    ticket_price = request.GET.get('ticket_price') or 0
    cash = request.GET.get('cash') or 0
    is_changes = isSubsetSum(ticket_price, cash)
    changes = getSubset(ticket_price, cash)
    if(ticket_price and cash):
        return render(request, "loket.html",
        {
            'cash': cash,
            'ticket_price': ticket_price,
            'sum': int(cash)-int(ticket_price),
            'moneys': moneys,
            'is_changes': is_changes,
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

def getSubset(ticket_price, cash):
    sum_all = int(cash) - int(ticket_price)
    result = []
    def fork(i= 0, s= 0, t = []):
        if (s == sum_all ):
            result.append(t)
            return
        if(i == len(moneys)):
            return
        if(s + moneys[i] <= sum_all):
            fork(i+1, s+moneys[i], [t, moneys[i]])
        fork(i+1, s, t)
    fork()
    return result
