from django.shortcuts import render, get_object_or_404
from .models import Card, Direction
from django.utils import timezone
from .forms import PostForm, Process 

def edit(request):
    
    post=get_object_or_404(Card,pk=7)
    form=PostForm(instance=post)
    process=Process()
    
    cards=Card.objects.order_by('create_date')
    return render(request,'intrn_track/edit.html',{'cards': cards, 'form':form, 'process':process})


def home(request):
    if request.method=="POST":
        card=PostForm(request.POST)
        process=Process(request.POST)
        #pro=process.search
        
               
        if process.is_valid():
            #pros=Process(Direction,pk=1)
            #if pros.is_valid():
           
            pros=get_object_or_404(Direction,pk=1)
            post=get_object_or_404(Card,pk=pros.search)
            form=PostForm(request.POST,instance=post)
            #if form.is_valid():
            #    post=form.save(commit=False)
            #    post.create_date=timezone.now()
            #    post.save()
        
        elif card.is_valid():
            post=get_object_or_404(Card,pk=2)
            form=PostForm(request.POST,instance=post)
            if form.is_valid():
                post=form.save(commit=False)
                post.create_date=timezone.now()
                post.save()
        
    else:
        post=get_object_or_404(Card,pk=2)
        form=PostForm(instance=post)
        process=Process()
    
    cards=Card.objects.order_by('create_date')
    return render(request,'intrn_track/home.html',{'cards': cards, 'form':form, 'process':process})
