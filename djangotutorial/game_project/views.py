from rest_framework import generics
from game_project.models import User, Level, Exercise, Achievement, Progress
from game_project.urls import UserSerializer, LevelSerializer, ExerciseSerializer, AchievementSerializer, ProgressSerializer


# Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Levels
class LevelListCreateView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


# Exercises
class ExerciseListCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


# Achievements
class AchievementListCreateView(generics.ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class AchievementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


# Progress
class ProgressListCreateView(generics.ListCreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


class ProgressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer