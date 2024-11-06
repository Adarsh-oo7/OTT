from django.db import models
from django.utils import timezone

# Create your models here.
class movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    video=models.FileField(upload_to='videos/')
    count=models.IntegerField()


class watch_list(models.Model):
    user_id=models.ForeignKey("admins.customUser", on_delete=models.CASCADE)
    movie_id=models.ForeignKey("moves.movie",  on_delete=models.CASCADE)


class watch_history(models.Model):
    user = models.ForeignKey("admins.customUser", on_delete=models.CASCADE)
    movie = models.ForeignKey("moves.movie", on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)  # Use auto_now_add for creation time

  
    def __str__(self):
        return f"{self.user} watched {self.movie} on {self.date_time}"