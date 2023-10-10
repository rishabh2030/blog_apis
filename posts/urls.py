from django.urls import path
from .apis import BlogApis

urlpatterns = [
    path('blog/',BlogApis.as_view(), name='Blog_apis')
]
