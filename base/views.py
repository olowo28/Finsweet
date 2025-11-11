from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm,Subscriberform


# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def aboutus(request):
    return render(request, 'base/Aboutus.html')

def authors(request):
    return render(request, 'base/Author.html')

def blog(request):
    return render(request,'base/blog.html')

def blogpost(request):
    return render(request, 'base/blog post.html')

def category(request):
    return render(request, 'base/category.html')

def privacy(request):
    return render(request, 'base/privacy policy.html')

def contactroom(request):
    form= ContactForm()
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context ={'form':form}
    return render(request, 'base/contact.html', context)


def subscriberoom(request):
    
    if request.method == 'POST':
        form= Subscriberform(request.POST)
        if form.is_valid():
           try:
              form.save()
              messages.success(request, 'Thank you for subscribing')
           except:
               messages.error(request, 'This email is already ssubscribed')
        else:
            messages.error(request, 'Please enter a valid Email')

    return redirect(request.META.get('HTTP_REFERER', 'index'))
