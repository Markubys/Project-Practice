from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    hash_password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Level(models.Model):
    level_number = models.IntegerField(unique=True)
    difficulty = models.CharField(max_length=50)  # Например, "Легкий", "Средний", "Сложный"
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Level {self.level_number} - {self.difficulty}"


class Exercise(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="exercises")
    text = models.TextField()
    time_limit = models.IntegerField(help_text="Время в секундах", null=True, blank=True)

    def __str__(self):
        return f"Exercise {self.id} (Level {self.level.level_number})"


class Achievement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to="achievements/", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="progress")
    accuracy = models.FloatField(help_text="Точность в процентах")
    speed = models.FloatField(help_text="Скорость в символах в минуту")
    errors = models.IntegerField(help_text="Количество ошибок")

    def __str__(self):
        return f"{self.user.username} - Level {self.level.level_number}: {self.accuracy}% accuracy, {self.speed} CPM"