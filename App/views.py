from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Users
from .models import Payment
from .models import Wallet
from .models import Message
from .models import W_history

# Create your views here.

def index(request):
    context = {

    }
    return render(request, 'index.html', context)

def usersignup1(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('usersignup1')
            elif Users.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('usersignup1')
            else:
                user = Users.objects.create_user(username=username, email=email, password=password1, number=number)
                messages.success(request, 'account was created successfully')
                user.save()
                return redirect('userlogin2')
        else:
            messages.info(request, 'password not matching...')
            return redirect('usersignup1')
    context = {}
    return render(request, 'usersignup1.html', context)

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('adminpage')
            else:
                login(request, user)
                return redirect('dashboard')
        else:
            return redirect('userlogin')
            # messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'userlogin.html', context)

def adminpage(request):
    return render(request, 'adminpage.html')

def dashboard(request):

    user = Users.objects.get(username=request.user)

    context = {
        'user': user,
    }

    return render(request, 'dashboard.html', context)

def deposit(request):

    wallet = Wallet.objects.all()
    payment = Payment.objects.all()

    context = {
        'wallet': wallet,
        'payment': payment,
    }

    return render(request, 'deposit.html', context)

def edithprofile(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        city = request.POST['city']
        address = request.POST['address']
        pin = request.POST['pin']
        gender = request.POST['gender']
        picture = request.FILES.get('picture')

        user.city = city
        user.gender = gender
        user.address = address
        user.pin = pin
        user.picture = picture
        user.picture = picture

        user.save()
        return redirect('dashboard')
    context = {
        'user': user,
    }
    return render(request, 'edithprofile.html', context)

def messagedelete(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('message')

    context = {
        'message': message,
    }
    return render(request, 'messagedelete.html', context)

def message(request):

    message = Message.objects.filter().order_by('-id')
    # message = Message.objects.get(message=request.user)
    if request.method == 'POST':
        message = request.POST['message']
        # name = message.sender

        user = Message.objects.create(message=message)
        # messages.success(request, 'message sent successfully')
        user.save()
        return redirect('message')
    context = {
        'message': message,
    }
    return render(request, 'message.html', context)

def messages(request):

    message = Message.objects.all().order_by('-id')
    context = {
        'message': message
    }
    return render(request, 'messages.html', context)

def paymentdelete(request, pk):

    payment = Payment.objects.get(id=pk)
    if request.method == 'POST':
        payment.delete()
        return redirect('paymentedit')
    context = {
        'payment': payment,
    }
    return render(request, 'paymentdelete.html', context)

def paymentedit(request):

    payment = Payment.objects.all()

    if request.method == 'POST':
        price = request.POST['price']
        percentage = request.POST['percentage']
        total = request.POST['total']

        payment = Payment.objects.create(price=price, percentage=percentage, total=total)

        payment.save()
        return redirect('paymentedit')

    context = {
        'payment': payment,
    }

    return render(request, 'paymentedit.html', context)

def profile(request, pk):

    user = Users.objects.get(id=pk) # .order_by('-id')
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

def user(request, pk):

    user = Users.objects.get(id=pk)
    # user = Users.objects.filter(is_superuser=False)
    context = {
        'user': user,
    }
    return render(request, 'user.html', context)

def userblock(request, pk):

    user = Users.objects.get(id=pk)
    if request.method == 'POST':

        if user.block:
            user.block = False
            user.save()
            return redirect('users')

        user.block = True
        user.save()
        return redirect('users')
    context = {
        'user': user,
    }

    return render(request, 'userblock.html', context)

def userdelete(request, pk):

    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    context = {
        'user': user,
    }
    return render(request, 'userdelete.html', context)

def useredit(request, pk):

    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        price = int(request.POST["price"])
        percentage = int(request.POST["price"]) / int(request.POST["percentage"])
        total = int(request.POST["price"]) + int(request.POST["percentage"])

        user.money = price
        user.percentage = percentage
        user.total = total
        user.save()
        return redirect('users')
    context = {
        'user': user,
    }
    return render(request, 'useredit.html', context)

def users(request):
    users = Users.objects.filter(is_superuser=False).order_by('-id')
    # user = Users.objects.filter(is_superuser=False)
    context = {
        'users': users,
    }
    return render(request, 'users.html', context)

def walletdelete(request, pk):
    wallet = Wallet.objects.get(id=pk)
    if request.method == 'POST':
        wallet.delete()
        return redirect('walletedit')
    context = {
        'wallet': wallet,
    }
    return render(request, 'walletdelete.html', context)

def walletedit(request):

    wallet = Wallet.objects.all().order_by('-id')
    if request.method == 'POST':
        address = request.POST["type"]
        types = request.POST["address"]

        wallet = Wallet.objects.create(address=address, type=types)

        wallet.save()
        return redirect('walletedit')
    context = {
        'wallet': wallet,
    }

    return render(request, 'walletedit.html', context)

def withdraw(request):

    users = Users.objects.get(username=request.user)
    user = W_history.objects.all() # .order_by(-id)

    current_balance = users.money
    pin = users.pin
    name = users.username

    if request.method == 'POST':

        amount = request.POST['amount']
        address = request.POST['address']
        user_pin = request.POST['pin']

        if user_pin == pin:
            if amount >= current_balance:
                balance = current_balance - amount

                history = W_history.objects.create(balance=balance, name=name, address=address)
                history.save()
                return redirect('withdraw')

    context = {
        'user': user,
        'users': users,
    }
    return render(request, 'withdraw.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')










