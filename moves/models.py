from django.db import models

# Create your models here.
class movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    video=models.FileField(upload_to='videos/')
    count=models.IntegerField()


class watch_list(models.Model):
    user_id=models.OneToOneField("admins.customUser", on_delete=models.CASCADE)
    movie_id=models.OneToOneField("moves.movie",  on_delete=models.CASCADE)


class watch_history(models.Model):
    user_id=models.OneToOneField("admins.customUser",  on_delete=models.CASCADE)
    movie_id=models.OneToOneField("moves.movie",  on_delete=models.CASCADE)
    date_time=models.DateTimeField( auto_now=True,auto_now_add=False)