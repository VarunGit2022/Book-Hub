from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    cover_image = models.URLField(null=True)
    rating = models.CharField(max_length=100, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True)
    published_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recommended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} recommends {self.book.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.book.title}"
    
class Like(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)