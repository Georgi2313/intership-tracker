from django.shortcuts import render
from .models import Card
from django.utils import timezone
from .forms import PostForm

def home(request):
    if request.method=="POST":
        card=PostForm(request.POST)
        if card.is_valid():
            post=card.save(commit=False)
            post.create_date=timezone.now()
            post.save()
        
   
    form=PostForm()
    cards=Card.objects.order_by('create_date')
    return render(request,'intrn_track/home.html',{'cards': cards, 'form':form})
