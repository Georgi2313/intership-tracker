from django.shortcuts import render
from .models import Card

def home(request):
    cards=Card.objects.order_by('create_date')
    return render(request,'intrn_track/home.html',{'cards': cards})
