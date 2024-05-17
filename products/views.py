from django.shortcuts import render

# Create your views here.
def shop_detail(reguest):
    return render(reguest, 'detail.html')

def favorites(reguest):
    return render(reguest,"favorites.html" )

def shop(reguest):
    return render(reguest, 'shop.html')