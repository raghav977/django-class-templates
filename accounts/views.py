from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article

from django.http import HttpResponse
# Create your views here.


def signup(request):
    return render(request,'accounts/signup.html')



def create_article(request):
    if request.method == 'POST':
        print("this is post ",request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        authorname = request.POST.get('authorname')
        image = request.FILES.get('image')
        ads = request.FILES.get('ads')

        article = Article.objects.create(
            title=title,
            content=content,
            authorname=authorname,
            image=image,
            ads=ads
        )
        return redirect('home')

    return render(request, 'accounts/create_article.html')


def home(request):

    article = Article.objects.all()
    for i in article:
        i.content = i.content[0:100]
    obj = {
        "name":article
    }
    return render(request,'home/home.html',context=obj)




def article_detail(request,id):
    print("this is id",id)
    try:

        article = Article.objects.get(pk=id)
    
    except Article.DoesNotExist:
        return HttpResponse("the article doesnot exist")
    detail = {
        'content':article
    }

    return render(request,'home/detail.html',context=detail)


def contact(request):
    return render(request,'home/contact.html')