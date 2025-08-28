from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
import datetime
from .forms import RegisterForm, PostForm
from .models import User, Comment

def index_view(request):
    return redirect('comments')

def users_view(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'keijiban/users.html', context)

def user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)

    context = {
        'user' : user
    }

    return render(request, 'keijiban/user.html', context)

def comments_view(request):
    comments = Comment.objects.all() 
    context = {
        'comments' : comments
    }
    return render(request, 'keijiban/comments.html', context)

def comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    context = {
        'comment' : comment
    }
    return render(request, 'keijiban/comment.html', context)

def register_view(request):

    if request.method == 'POST': #POSTリクエストかどうかの確認

        form = RegisterForm(request.POST) #POSTの中身を受け取ってRegisterFormクラスのインスタンスを生成
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            age = form.cleaned_data.get('age')
            
            user = User(username=username, email=email, age=age) #POSTの中身を保存できる形に成形
            user.save() #DBに保存

            return redirect('users') #リダイレクト

    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }

    return render(request, 'keijiban/register.html', context)

def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data.get('text')
            user = form.cleaned_data.get('user')
            comment = Comment(text = text)
            comment.user = user
            comment.save()

            return redirect('comments')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'keijiban/post.html', context)