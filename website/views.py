from django.shortcuts import render, redirect
from .models import Member
from .forms import Memberform
from django.contrib import messages


def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all': all_members})


def join(request):
    if request.method == "POST":
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            age = request.POST['age']
            email = request.POST['email']
            password = request.POST['password']
            messages.success(request, 'There was an error in your form! Please, try again')
            # return redirect('join')
            return render(request, 'join.html',
                          {'first_name':first_name,
                           'last_name':last_name,
                           'age':age,
                           'email':email,
                           'password':password})
        messages.success(request, 'Your Form Has Been Submitted successfully')
        return redirect('home')
    else:
        return render(request, 'join.html', {})
