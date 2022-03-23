from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=65,
        unique=True
    )
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        "posts.Author",
        on_delete=models.CASCADE,
        blank=True,
        null=True        
    )
    def __str__(self):
        return f"Title: {self.title} | Content: {self.content} | Author-id: {self.author_id}"
    class Meta:
        ordering = ["-modified"]

class Author(models.Model):
    nick = models.CharField(max_length=25, unique=True)
    bio = models.TextField(
        blank=True,
        null=True
    )
    email = models.EmailField()
    def __str__(self):
        return f"{self.nick}"