from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")])
    points = models.IntegerField(default=0)  
    category = models.CharField(max_length=100, default="General") 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
    points_earned = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title} ({'Completed' if self.completed else 'In Progress'})"