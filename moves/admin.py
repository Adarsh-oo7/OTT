from django.contrib import admin
from .models import movie,watch_list,watch_history
# Register your models here.
admin.site.register(movie)
admin.site.register(watch_history)
admin.site.register(watch_list)