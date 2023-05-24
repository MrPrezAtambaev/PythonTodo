from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=256, blank=True)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(
        'auth.User', auto_created=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Auth(models.Model):
    email = models.EmailField(max_length=256, blank=True)
    password = models.CharField(max_length=256, blank=True)
    password2 = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.email


class Login(models.Model):
    email = models.EmailField(max_length=256, blank=True)
    password = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.email
