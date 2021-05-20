from django.shortcuts import render, redirect
import time
from datetime import datetime
from home.models import Contact
from home.models import Blog
from django.contrib import messages
from hello import settings
from django.contrib.auth.decorators import login_required
from django.http import request
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponseRedirect



# Create your views here.
def index(request):

    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    if request.method== "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.now())
        contact.save()
        messages.success(request, 'Message Sent.')

    return render(request,"contact.html")

@login_required(redirect_field_name='/')  #this new thing will stop the us3er from accessing the write blog page and redirect thye user to login page
def writeablog(request):
    if request.method== "POST" and request.FILES['thumbnail']:
        name = request.POST.get('name')
        blogtitle = request.POST.get('blogtitle')
        blogsubtitle = request.POST.get('blogsubtitle')
        blogcontent = request.POST.get('blogcontent')
        thumbnail = request.FILES['thumbnail']
        fs = FileSystemStorage()
        filename = fs.save(thumbnail.name, thumbnail)
        blog = Blog(name=name,blogtitle=blogtitle,blogsubtitle=blogsubtitle,blogcontent=blogcontent,thumbnail=thumbnail,pub_date=datetime.today())
        blog.save()
        messages.success(request, 'Your Blog Is Posted Successfully')
    return render(request, "writeablog.html" )
    
def blogpost(request):
    myposts= Blog.objects.all()
    return render(request, 'blogpost.html',{'myposts':myposts})

def blog(request,id):
    post= Blog.objects.filter(post_id =id)[0]
    return render(request,'blog.html', {'post':post})

def error_404(request, *args, **argv):
        return render(request,'404.html')

def admin(request):
    return render(request,'fuckoff.html')
def accadmin(request):
    return render(request,'fuckoff.html')
