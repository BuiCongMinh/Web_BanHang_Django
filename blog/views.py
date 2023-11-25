from django.shortcuts import render , HttpResponse, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import PostModel
from .forms import PostForm, PostModelForm

def main(req):
    return render(req,'main.html')

def list(request):
    # limit 
    limit = request.GET.get("limit")
    if limit and limit.isnumeric():
        limit = int(limit)
    else:
        limit = 3
    
    #sort
    sort = request.GET.get("sort")
    if sort not in ["created_at","-created_at","title"]:
        sort = "-created_at"

    # page
    page = request.GET.get("page", 1)

    # keyword
    keyword = request.GET.get("keyword")
    if keyword:
        post_list = PostModel.objects.filter(title__contains=keyword)
    else:
        post_list = PostModel.objects.all()
    post_list = post_list.order_by(sort).values()

    # paging
    post_paginator = Paginator(post_list, limit) 
    try:
        post_paginator = post_paginator.get_page(page)
    except PageNotAnInteger:
        post_paginator = post_paginator.get_page(1)
    except EmptyPage:
        post_paginator = post_paginator.get_page(post_paginator.num_pages)

    context = {
        "post_list" : post_paginator,
        "keyword" : keyword if keyword else "",
    }
    
    return render(request,'blog/list.html',context)


def detail(req,id):
    
    # post = PostModel.objects.get(pk=id)
    # post = PostModel.objects.filter(pk=id).values()[0]
    post = get_object_or_404(PostModel,pk=id)
    context = {
        "post":post,
    }
    
    return render(req,'blog/detail.html', context)

def add(request):
    # form = PostForm()
    form = PostModelForm()
    if request.method == "POST":
        # form = PostForm(request.POST)
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:list")
    
    context = {
        "form" : form
    }
    return render(request,"blog/add.html", context)


def edit(request, id):
    model = PostModel.objects.get(pk=id)
    form = PostModelForm(instance=model)    

    if request.method == "POST":
        form = PostModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect("blog:detail",model.id)

    context = {
        "form": form
    }
    return render(request,"blog/edit.html", context)

