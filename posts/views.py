from django.shortcuts import render
from posts.models import Post, Author

def home(request):
    return render(
        request=request,
        template_name="posts/main.html",
        context={}
    )

def posts_list(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={"posts":posts}
    )

def post_details(request,id):
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"post":post}
    )

def authors_list(request):
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={"authors": authors}
    )

def author_details(request,id):
    author = Author.objects.get(id=id)
    posts = Post.objects.filter(author_id=id)
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={
            "author":author,
            "posts": posts
        }
    )