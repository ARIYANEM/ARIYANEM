from django.shortcuts import render,HttpResponse
from . import models
from django.contrib.auth.decorators import login_required


def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    collect = {'articles': articles}
    return render(request, 'articles/articleslist.html', collect)
def detail(request, slug):
    #return HttpResponse(slug)
    Link = models.Article.objects.get(slug=slug)
    return render(request, 'articles/articles_detail.html',{'Linker':Link})

@login_required(login_url = "/accounts/login")
def articles_create(request):
    return render(request, 'articles/create.html',)
