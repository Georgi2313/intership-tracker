from django.shortcuts import render, get_object_or_404
from .models import Card, Direction
from django.utils import timezone
from .forms import PostForm, Process 

def edit(request,pk=2):
    
    if pk!=None:
        post=get_object_or_404(Card,pk=pk)
        form=PostForm(instance=post)

        if request.method=="POST":
            post=get_object_or_404(Card,pk=pk)
            form=PostForm(request.POST,instance=post)
            if form.is_valid():
                post=form.save(commit=False)
                post.save()
            #form=PostForm(request.POST,instance=post)

    else:   
        post=get_object_or_404(Card,pk=2)
        form=PostForm(instance=post)
    cards=Card.objects.order_by('create_date')
    return render(request,'intrn_track/edit.html',{'cards': cards, 'form':form})


def home(request):
    if request.method=="POST":
        card=PostForm(request.POST)
          
        if card.is_valid():
            #post=get_object_or_404(Card,pk=2)
            form=PostForm(request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                post.create_date=timezone.now()
                post.save()
        
    else:
        post=get_object_or_404(Card,pk=2)
        form=PostForm(instance=post)
     
    
    cards=Card.objects.order_by('create_date')
    return render(request,'intrn_track/home.html',{'cards': cards, 'form':form})
