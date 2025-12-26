# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import logout

from .models import Post, Berita
from .forms import PostForm, CommentForm, BeritaForm


# =======================
# HOME (PTI UMS STYLE)
# =======================

def post_list(request):
    query = request.GET.get('q')

    # Berita unggulan untuk Home
    featured_berita = Berita.objects.filter(featured=True)

    # Optional search global
    if query:
        featured_berita = featured_berita.filter(
            Q(judul__icontains=query) |
            Q(ringkasan__icontains=query)
        )

    featured_berita = featured_berita[:3]

    return render(request, 'blog/post_list.html', {
        'featured_berita': featured_berita,
        'query': query
    })


# =======================
# BERITA (PUBLIC)
# =======================

def berita(request):
    query = request.GET.get('q')
    berita_qs = Berita.objects.all()

    if query:
        berita_qs = berita_qs.filter(
            Q(judul__icontains=query) |
            Q(ringkasan__icontains=query)
        )

    paginator = Paginator(berita_qs, 6)
    page_number = request.GET.get('page')
    berita_list = paginator.get_page(page_number)

    return render(request, 'blog/berita.html', {
        'berita_list': berita_list,
        'query': query
    })


def berita_detail(request, pk):
    berita = get_object_or_404(Berita, pk=pk)
    return render(request, 'blog/berita_detail.html', {
        'berita': berita
    })


# =======================
# BERITA (ADMIN / EDITOR)
# =======================

@permission_required('blog.add_berita', raise_exception=True)
def berita_create(request):
    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('berita')
    else:
        form = BeritaForm()
    return render(request, 'blog/berita_form.html', {'form': form})


@permission_required('blog.change_berita', raise_exception=True)
def berita_edit(request, pk):
    berita = get_object_or_404(Berita, pk=pk)
    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES, instance=berita)
        if form.is_valid():
            form.save()
            return redirect('berita_detail', pk=pk)
    else:
        form = BeritaForm(instance=berita)
    return render(request, 'blog/berita_form.html', {'form': form})


@permission_required('blog.delete_berita', raise_exception=True)
def berita_delete(request, pk):
    berita = get_object_or_404(Berita, pk=pk)
    berita.delete()
    return redirect('berita')


@permission_required('blog.view_berita', raise_exception=True)
def dashboard_berita(request):
    berita = Berita.objects.all().order_by('-created_at')
    return render(request, 'blog/dashboard_berita.html', {
        'berita_list': berita
    })


# =======================
# POST / BLOG
# =======================

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# =======================
# PROFIL & AUTH
# =======================

def profil(request):
    return render(request, "blog/profil.html")


def custom_logout(request):
    logout(request)
    return redirect('/')
