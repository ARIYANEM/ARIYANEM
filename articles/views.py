from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms


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
    if request.method == 'POST':
        form = forms.ArticleCreate(request.POST,request.FILES)
        if form.is_valid():
            #save
            return redirect('articles:list')
    else:
        form = forms.ArticleCreate()
    return render(request , 'articles/create.html',{'form':form})
