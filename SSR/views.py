from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def mission(request):
    return render(request,'mission.html')
def news(request):
    return render(request,'news.html')
def donate(request):
    return render(request,'donate.html')
def contact(request):
    return render(request,'contact.html')