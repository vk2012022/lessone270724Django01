from django.db import models

# Создайте свои модели здесь.

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    username = models.CharField('Имя пользователя', max_length=100)  # Новое поле для имени пользователя

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
