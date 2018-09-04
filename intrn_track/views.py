from django.shortcuts import render

def home(request):
    return render(request,'intrn_track/home.html',{})
