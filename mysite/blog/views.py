from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articles,biji,jsbooks
from django.utils.timezone import utc
import datetime


# Create your views here.
def index(request):
    article_list = Articles.objects.order_by('-id')
    return render(request,'blog/index.html',{'article_list':article_list})


def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article = get_object_or_404(Articles,pk=article_id)
    return render(request, 'blog/edit_page.html',{'article':article})

def edit_body(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    create_time = datetime.datetime.utcnow().replace(tzinfo=utc)
    article_id = request.POST.get('article_id','0')
    if article_id == '0':
        article_list = Articles.objects.order_by('-id')
        Articles.objects.create(title=title,content=content,create_time=create_time)
        return render(request,'blog/index.html',{'article_list':article_list})
    article = get_object_or_404(Articles,pk=article_id)
    article.title  = title
    article.content = content
    article.save()
    return render(request,'blog/details.html',{'article':article})

def details(request,article_id):
    # article = Articles.objects.get(pk=article_id)
    article = get_object_or_404(Articles,pk=article_id)
    return render(request,'blog/details.html',{'article':article})

def daomubiji(request):
    jsbooks_list = jsbooks.objects.all()
    return render(request,'blog/daomubiji.html',{'jsbooks_list':jsbooks_list})

def daomubiji_page(request,id):
    jsbook = get_object_or_404(jsbooks,pk=id)
    return render(request,'blog/detail_biji.html',{'jsbook':jsbook})