from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from haystack.generic_views import SearchView
from users.forms import AddCourseUserForm
from users.models import Enrollment, User

from .forms import CommentForm, PostForm
from .models import Course, LessonSubmitUser, Post
from .paginator import paginator


@login_required(login_url='/auth/login/')
def index(request):
    """Главная страница"""
    template = 'posts/index.html'
    groups = Enrollment.objects.filter(
        user=request.user).select_related('course')
    context = {
        'groups': groups,
    }
    return render(request, template, context)


@login_required(login_url='/auth/login/')
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


@login_required(login_url='/auth/login/')
def post_detail(request, post_id):
    """Страница подробной информации о посте"""
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, id=post_id)
    submit_users = LessonSubmitUser.objects.filter(
        post=post).select_related("user")
    comments = post.comments.all()
    form = CommentForm()

    if not Enrollment.objects.filter(
            user=request.user
    ).select_related('course').filter(course=post.group).exists():
        raise PermissionDenied()

    context = {
        'submit_users': submit_users,
        'post': post,
        'form': form,
        'comments': comments
    }
    if request.method == 'POST':
        submit_users = LessonSubmitUser.objects.create(post=post, user=request.user)
        submit_users.save()
        return redirect("posts:group_list", post.group.slug)
    return render(request, template, context)


@login_required(login_url='/auth/login/')
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


@login_required(login_url='/auth/login/')
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


@login_required(login_url='/auth/login/')
@permission_required('posts.delete_post', raise_exception=True)
def post_delete(request, post_id):
    """Функция удаления поста"""
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        if Post.objects.filter(id=post_id).exists():
            Post.objects.filter(id=post_id).delete()
            return redirect("posts:index")
    return redirect("posts:post_detail", post_id)


@login_required(login_url='/auth/login/')
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


@login_required(login_url='/auth/login/')
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
                Enrollment.objects.update_or_create(
                    user=students,
                    course=Course.objects.get(pk=i.pk)
                )
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
            search_result = User.objects.filter(fio__icontains=question)
            context["search_result"] = search_result

        return render(request, self.template, context=context)
