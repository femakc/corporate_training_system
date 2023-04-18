import time
from datetime import date

from haystack.generic_views import SearchView
from django.shortcuts import render, get_object_or_404, redirect
from cts.settings import ROLES_CHOICES
from .models import Post, Course
from users.models import Enrollment
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PostForm, CommentForm
from .paginator import paginator
from django.conf import settings
from users.models import User , Enrollment
from users.forms import AddCourseUserForm, SearchForm
from haystack.query import SearchQuerySet



@login_required(login_url='/auth/login/')
def index(request):
    """Главная страница"""
    # template = 'posts/index.html'
    template = 'posts/index_group.html'
    # post_list = Post.objects.all()
    groups = Enrollment.objects.filter(user=request.user).select_related('course')
    context = {

        'groups': groups,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Страница группы постов"""
    template = 'posts/group_list.html'
    group = get_object_or_404(Course, slug=slug)
    post_list = (
        Post
        .objects
        .filter(group=group)
    )
    context = {
        'group': group,
        'page_obj': paginator(post_list, request),
    }
    return render(request, template, context)


def post_detail(request, post_id):
    """Страница подробной информации о посте"""
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }
    return render(request, template, context)


@login_required
@permission_required('posts.add_post', raise_exception=True)
def post_create(request):
    """Страница создания поста"""
    form = PostForm(
        request.POST or None,
        files=request.FILES or None
    )
    template = 'posts/create_post.html'
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts:index")
    return render(request, template, {'form': form})


@login_required
@permission_required('posts.change_post', raise_exception=True)
def post_edit(request, post_id):
    """Страница редактирования поста"""
    template = 'posts/create_post.html'
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
    )
    if post.author != request.user:
        return redirect("posts:post_detail", post_id)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("posts:post_detail", post_id)
        return render(request, template, {'form': form})
    context = {
        'form': form,
        'is_edit': True,
        'post': post,
    }
    return render(request, template, context)


@login_required
@permission_required('posts.delete_post', raise_exception=True)
def post_delete(request, post_id):
    """Функция удаления поста"""
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        if Post.objects.filter(id=post_id).exists():
            Post.objects.filter(id=post_id).delete()
            return redirect("posts:index")
    return redirect("posts:post_detail", post_id)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


@login_required
@permission_required('posts.add_post', raise_exception=True)
def add_course_student(request, user_id):
    students = get_object_or_404(User, pk=user_id)
    user_groups = Enrollment.objects.filter(user=students).select_related('course')
    form = AddCourseUserForm(
        request.POST or None,
        files=request.FILES or None,
        instance=students
    )
    template = 'posts/add_course.html'

    if request.method == 'POST':
        if form.is_valid():
            my_m2ms = form.cleaned_data['user_group']
            for i in my_m2ms:
                Enrollment.objects.update_or_create(user=students, course=Course.objects.get(pk=i.pk))
            form.save()
            return redirect("posts:search_results", user_id)
        return render(request, template, {'form': form})
    contex = {
        'form': form,
        'students': students,
        'user_groups': user_groups
    }
    return render(request, template, contex)


class SearchView(SearchView):
    template = 'posts/find_student.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_result = User.objects.filter(username=question)
            context["search_result"] = search_result

        return render(request, self.template, context=context)


# @login_required
# def follow_index(request):
#     """Страница подписки"""
#     current_user = request.user
#     template = 'posts/follow.html'
#     followings = Follow.objects.select_related(
#         'user').filter(user_id=current_user)
#     post_list = Post.objects.select_related('author').filter(
#         author__in=[i.author_id for i in followings]
#     )
#     context = {
#         'page_obj': paginator(post_list, request),
#     }
#     return render(request, template, context)


# @login_required
# def profile_follow(request, username):
#     """Подписаться на автора"""
#     user = request.user
#     author = get_object_or_404(User, username=username)
#     if user != author:
#         if not Follow.objects.filter(user=user, author=author).exists():
#             Follow.objects.create(user=user, author=author)
#     return redirect('posts:follow_index')
#
#
# @login_required
# def profile_unfollow(request, username):
#     """Одписаться на автора"""
#     user = request.user
#     author = get_object_or_404(User, username=username)
#     if Follow.objects.filter(user=user, author=author).exists():
#         Follow.objects.filter(user=user, author=author).delete()
#     return redirect('posts:follow_index')
