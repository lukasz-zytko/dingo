from django import forms
from posts.models import Author

class PostForm(forms.Form):
    title = forms.CharField(max_length=65, help_text="* Maksymalnie 65 znaków.")
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows":10, "cols":40}),
        help_text="* ",
        )
    author = forms.ChoiceField(
        choices=((a.id, a.nick) for a in Author.objects.all()),
        help_text="* "
    )

class AuthorForm(forms.Form):
    nick = forms.CharField(max_length=25, help_text="* Maksymalnie 25 znaków.")
    email = forms.EmailField(help_text="* ")
    bio = forms.CharField(required=False)