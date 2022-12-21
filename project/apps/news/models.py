from django.db import models


class Category(models.Model):
    isActive = models.BooleanField(default=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']



class News(models.Model):
    isActive = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='news', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Comment(models.Model):
    isActive = models.BooleanField(default=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']



class Image(models.Model):
    isActive = models.BooleanField(default=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['news']


class Video(models.Model):
    isActive = models.BooleanField(default=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.video.name
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['news']
