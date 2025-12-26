from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Comment, Berita


# =========================
# ADMIN BERITA
# =========================
@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'thumbnail', 'featured', 'created_at')
    list_editable = ('featured',)              # ✅ TOGGLE UNGGULAN LANGSUNG
    list_filter = ('featured', 'created_at')
    search_fields = ('judul', 'ringkasan')
    ordering = ('-created_at',)

    def thumbnail(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:4px; object-fit:cover;" />',
                obj.gambar.url
            )
        return '-'

    thumbnail.short_description = 'Preview'


# =========================
# ADMIN POST
# =========================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'text')
    ordering = ('-published_date',)


# =========================
# ADMIN COMMENT
# =========================
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date')
    search_fields = ('author', 'text')
