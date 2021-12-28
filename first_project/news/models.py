from django.db import models
from django.urls import reverse


class News(models.Model):
    # objects = None
    title = models.CharField(max_length=150, verbose_name='Наименование')
    # max_length - установка максимальной длины текста в строке
    content = models.TextField(blank=True, verbose_name='Контент')
    # blank - возможность добавления пустой строки
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    # auto_now_add - возможность добавления даты без возможности редактирования
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # auto_now = можно будет видеть последнее время редактирования
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
