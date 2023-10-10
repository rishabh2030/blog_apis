from django.db import models
from helper.models import CreationModificationBase
from django.contrib.auth import get_user_model
# Create your models here.
Users = get_user_model()

class BlogPost(CreationModificationBase):
    blog_id = models.CharField(max_length=220,blank=True,null=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='_user')
    post_file = models.FileField(upload_to="post/files",blank=True,null=True)
    blog_text = models.TextField(blank=True, null=True)

    
