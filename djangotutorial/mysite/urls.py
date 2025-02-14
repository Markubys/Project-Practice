"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.urls import path, include
from django.contrib.auth.models import User
from polls.models import Question
from game_project.models import User, Level, Exercise, Achievement, Progress

from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'hash_password']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['level_number', 'difficulty', 'description']

# ViewSets define the view behavior.
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ['level', 'text', 'time_limit']

# ViewSets define the view behavior.
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = ['name', 'description', 'icon', 'date']

# ViewSets define the view behavior.
class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class ProgressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Progress
        fields = ['user', 'level', 'accuracy', 'speed', 'errors']

# ViewSets define the view behavior.
class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'users', UserViewSet)
router.register(r'Level', LevelViewSet)
router.register(r'Exercise', ExerciseViewSet)
router.register(r'Achievement', AchievementViewSet)
router.register(r'Progress', ProgressViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin/", admin.site.urls),
]