from django.shortcuts import render


def home_view(request):
    return render(request,"site/index.html")

def about_view(request):
    return render(request,"site/about.html")

def contact_view(request):
    return render(request,'site/contact.html')

