from BlogApp.views import HomePage, AboutPage
from django.urls import path


urlpatterns = [
    path('', HomePage.as_view(), name='blog-homepage'),
    path('home/', HomePage.as_view(), name='blog-homepage'),
    path('about/', AboutPage.as_view(), name='blog-aboutpage'),
]
