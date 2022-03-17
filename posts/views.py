from django.shortcuts import render
from posts.models import Post, Author
from posts.forms import AuthorForm, PostForm
from django.contrib import messages


def home(request):
    return render(
        request=request,
        template_name="posts/main.html",
        context={}
    )

def posts_list(request):
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid:
            Post.objects.create(
                title = post_form.data["title"],
                content = post_form.data["content"],
                author_id = post_form.data["author"]
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy wpis!"
            )
    posts = Post.objects.all()
    post_form = PostForm()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={
            "posts": posts,
            "post_form": post_form
        }
    )

def post_details(request,id):
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"post":post}
    )

def authors_list(request):
    if request.method == "POST":
        author_form = AuthorForm(data=request.POST)
        bio_form = author_form.data["bio"] or None
        if author_form.is_valid:
            Author.objects.create(
                nick = author_form.data["nick"],
                email = author_form.data["email"],
                bio = bio_form
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowego autora!"
            )
    author_form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={
            "authors": authors,
            "author_form": author_form
        }
    )

def author_details(request,id):
    author = Author.objects.get(id=id)
    posts = Post.objects.filter(author_id=id)
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={
            "author": author,
            "posts": posts
        }
    )