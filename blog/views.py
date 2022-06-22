from django.shortcuts import render
from .model import Post

# Create your views here.
def PostListView():
    class Meta:
        model = Post
        fields ="__all__"
        success_url  = reverse_lazy(“blog:all”)
        
        
def PostDetailView():
    class Meta:
        model = Post
        
def PostUpdateView():
    class Meta:
        model = Post
        fields = “__all__”
        success_url  = reverse_lazy(“blog:all”)
        
def PostDeleteView():
    class Meta:
        model = Post
        fields = “__all__”
        success_url  = reverse_lazy(“blog:all”)