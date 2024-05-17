from django.shortcuts import render

# Create your views here.
def login(reguest):
    return render(reguest, 'login.html')

def register(reguest):
    return render(reguest,'register.html')