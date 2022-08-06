from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

def index(request):
    User = get_user_model()
    users = User.objects.values()
    return render(request, 'users.html', {
        'users': users
    })

def getUser(request, user_id):
    User = get_user_model()
    user = User.objects.filter(id=user_id).values()
    print(user)
    return JsonResponse({
        'user': list(user)
    })

def addUser(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return redirect('/users')
    else:
        return HttpResponse('POST request')

def deleteUser(request, user_id):
    if request.method == 'POST':
        User = get_user_model()
        user = User.objects.get(id = user_id)
        user.delete()
        return redirect('/users')
    else:
        return HttpResponse('POST request')

def updateUser(request, user_id):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        User = get_user_model()
        user = User.objects.get(id = user_id)
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('/users')
    else:
        return HttpResponse('POST request')