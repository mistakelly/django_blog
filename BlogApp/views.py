from typing import Any
from django.shortcuts import render, HttpResponse

# view modules
from django.views.generic import TemplateView, ListView
import django.views
import django.views.generic

# Databases
from BlogApp.models import Post
from django.contrib.auth.models import User


# Create your views here.
class HomePage(ListView):
    template_name = "home.html"
    model = Post
    context_object_name = 'posts'


class AboutPage(TemplateView):

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    all_post = [
        {
            "author": "John Doe",
            "date": "2024-05-27",
            "title": "First Post",
            "content": "This is the content of the first post.",
        },
        {
            "author": "Jane Smith",
            "date": "2024-05-28",
            "title": "Second Post",
            "content": "This is the content of the second post.",
        },
    ]

  

    template_name = 'about.html'

