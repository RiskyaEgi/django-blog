from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


# =========================
# MODEL POST
# =========================
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    header_image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# =========================
# MODEL COMMENT
# =========================
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


# =========================
# MODEL BERITA
# =========================
class Berita(models.Model):
    judul = models.CharField(max_length=200)
    ringkasan = models.TextField()
    isi = models.TextField()
    gambar = models.ImageField(upload_to='post_images/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.judul


#article
class Article(models.Model):
    ARTICLE_TYPE = (
        ('post', 'Post'),
        ('berita', 'Berita'),
    )

    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = HTMLField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    article_type = models.CharField(max_length=10, choices=ARTICLE_TYPE)
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

