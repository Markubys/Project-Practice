from django.contrib import admin

from game_project.models import User, Level, Exercise, Achievement, Progress

admin.site.register(User)
admin.site.register(Level)
admin.site.register(Exercise)
admin.site.register(Achievement)
admin.site.register(Progress)
