from django.shortcuts import render,HttpResponse
from . import models


def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    collect = {'articles': articles}
    return render(request, 'articles/articleslist.html', collect)
def detail(request, slug):
    return HttpResponse(slug)
