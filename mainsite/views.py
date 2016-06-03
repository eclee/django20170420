from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post)+"<hr>")
        post_lists.append("<small>" + str(post.body.encode('utf-8')) +"</small><br><br>")

    return HttpResponse(post_lists)