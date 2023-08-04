from django.shortcuts import render , get_object_or_404 , redirect
from django.http import JsonResponse
from .models import *
from .forms import CommentForm
import json
# Create your views here.

def home(request):
    posts = Post.objects.all().filter(status='published')
   
    context = {
        'posts':posts ,
    
    }
    return render(request , 'blog/home.html' , context)

# ============================================= details
def detail(request , id):
    post = get_object_or_404(Post , pk=id)   
    comments = Comment.objects.all()
    context = {
        'post':post ,'comments':comments
    }
    return render(request , 'blog/detail.html' , context)

# ================================================= comment
def comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        postId = request.POST['postId']
        post = Post.objects.get(pk=postId)
        user = request.user
        # print(comment , postId , user , post)
        Comment.objects.create(
            post = post,
            body = comment ,
            user = user
        )
    return JsonResponse({'bool': True})


# ========================================== like function
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('postid'))
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.like_count -= 1
            result = post.like_count
            post.save()
        else:
            post.likes.add(request.user)
            post.like_count += 1
            result = post.like_count
            post.save()

        return JsonResponse({'result': result, })


# ============================== 
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name , email ,message)
        Contact.objects.create(
            name = name ,
            email = email,
            message = message
        )
    return JsonResponse({'bool' : True})