from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField('Информация', blank=True, null=True)
    image = models.ImageField('Фото', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователья'

class Project(models.Model):
    title = models.CharField('Название', max_length=225)
    description = models.TextField('Описание')
    start_date = models.DateTimeField('Дата старта', auto_now=True)
    end_date = models.DateTimeField('Дата окончания', blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser, related_name='projects')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проект'

class Task(models.Model):
    title = models.CharField('Название', max_length=225)
    description = models.TextField('Описание')
    deadline_date = models.DateTimeField('Срок до:')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

