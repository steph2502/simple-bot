from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from .import forms


def article_list(request):
    a_list = Article.objects.all().order_by('date')
    return render(request, 'hello/article_list.html',{'articles':a_list})


def articles_detail(request,slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    return render(request, "hello/articles_detail.html",{"article":article})

@login_required(login_url='/accounts/login/')
def article_add(request):
    if request.method == "POST":
        form = forms.CreateArticles(request.POST,request.FILES)
        if form.is_valid():
            #save
            instance = form.save(commit= False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticles()
    return render(request,"hello/article_add.html",{"form":form})