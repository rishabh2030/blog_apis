from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from helper.functions import *
from .models import BlogPost
from .serializers import BlogPostSerializer
from authentication.serializers import UserSerializer
from authentication.models import User
import messages,keys
from django.core.exceptions import ObjectDoesNotExist

class BlogApis(generics.RetrieveUpdateDestroyAPIView,generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get(self, request, *args, **kwargs):
        try:
            blog_posts = BlogPost.objects.all()
            serializer = BlogPostSerializer(blog_posts, many=True,context={'request':request})
            return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS, serializer.data), status=status200)
        except ObjectDoesNotExist:
            return Response(ResponseHandling.success_response_message(messages.OPERATION_FAILED,  messages.NO_DATA), status=status400)

    def post(self, request, *args, **kwargs):
        try:
            user = UserSerializer(request.user)
            file = request.data.get(keys.POST_FILE)
            blog_test = request.data.get(keys.BLOG_TEXT)
            blog_obj= BlogPost.objects.create(user=User.objects.get(mobile=user.data.get(keys.MOBILE))) 
            blog_obj.blog_text = blog_test
            blog_obj.post_file = file
            blog_obj.save()

            res = {
                "blog_post_ID":blog_obj.id
            }
            
            return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS, res), status=status200)
        except ObjectDoesNotExist:
            return Response(ResponseHandling.success_response_message(messages.OPERATION_FAILED, messages.NO_DATA), status=status400)

    def delete(self, request, *args, **kwargs):
        try:
            post_id = request.GET.get(keys.POST_ID)
            blog_obj = BlogPost.objects.get(id=post_id)
            blog_obj.delete()
            return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS, messages.POST_DELETED), status=status200)
        except ObjectDoesNotExist:
            return Response(ResponseHandling.success_response_message(messages.OPERATION_FAILED, messages.NO_DATA), status=status400)
