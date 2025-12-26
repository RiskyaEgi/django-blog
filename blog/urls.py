from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.post_list, name="post_list"),

    # Profil (login required)
    path("profil/", views.profil, name="profil"),

    # Berita (public)
    path("berita/", views.berita, name="berita"),
    path("berita/<int:pk>/", views.berita_detail, name="berita_detail"),

    # Post / Blog
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path('berita/<int:pk>/delete/', views.berita_delete, name='berita_delete'),
    path('berita/new/', views.berita_create, name='berita_create'),
    path('dashboard/berita/', views.dashboard_berita, name='dashboard_berita'),
    path("profil/", views.profil, name="profil"),



    #berita new
    path('berita/new/', views.berita_create, name='berita_create'),
path('berita/<int:pk>/edit/', views.berita_edit, name='berita_edit'),
    # Comment
    path(
        "post/<int:pk>/comment/",
        views.add_comment_to_post,
        name="add_comment_to_post"
    ),
]
