from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib.auth import authenticate,login

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

    return render(request, 'article/create_article.html')


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


def login_user(request):
    if(request.method=='POST'):

        print("this is rquest post",request.POST)
        username = request.POST.get('username')
        print("this is username",username)
        password = request.POST.get('password')
        print("this is password",password)

        user = authenticate(username=username,password=password)
        print("this is user",user)
        if user is None:
            return HttpResponse("not matched credentials")
        role = user.role

        print("This is user role",role)
        if(user.role=='admin'):
            login(request,user)
            return render(request,'admin/dashboard.html')
        login(request,user)
        return redirect('home')
    return render(request,'accounts/login.html')


@login_required
def admin_dashboard(request):

    if(request.user.role=='admin'):
        return render(request,'admin/dashboard.html')
    else:
        return render(request,'home/home.html')




@login_required
def list_article(request):
    if(request.user.role=='admin'):
        article = Article.objects.all()
        context={
            'name':article
        }
        return render(request,'admin/list-article.html',context=context)
    else:
        return render(request,'home/home.html')


@login_required

def edit_article(request,id):
    if(request.method=='POST'):
        print("the request method",request.POST)
        edited_title = request.POST.get("edit-title")
        edited_authorname = request.POST.get("edit-authorname")
        edited_content = request.POST.get("edit-content")

        article = Article.objects.get(id=id)
        article.title = edited_title
        article.authorname = edited_authorname
        article.content = edited_content
        article.save()
        return redirect("home")
        
        pass
    print("this is edit wala ")
    # id=1
    if(request.user.role=='admin'):
        try:

            article = Article.objects.get(id=id)
            # article.title="title 1 ho"
            # print("this is article",article.title)
            context = {
                'detail':article
            }
            return render(request,'admin/edit-article.html',context=context)
        except Article.DoesNotExist:
            return HttpResponse("Article does not exist")
    return redirect('home')

