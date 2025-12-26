from django import forms
from .models import Post, Comment, Berita


# =========================
# FORM POST
# =========================
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6
            }),
            'header_image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


# =========================
# FORM COMMENT
# =========================
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }


# =========================
# FORM BERITA
# =========================
class BeritaForm(forms.ModelForm):
    featured = forms.BooleanField(
        required=False,
        label='Jadikan sebagai Berita Unggulan'
    )

    class Meta:
        model = Berita
        fields = ['judul', 'ringkasan', 'isi', 'gambar', 'featured']
        widgets = {
            'judul': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ringkasan': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'isi': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6
            }),
            'gambar': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
