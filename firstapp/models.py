from django.db import models


class MainStartPage(models.Model):
    '''Главные страницы сайта'''
    slug = models.SlugField(max_length=30, unique=True, default="slug")
    title = models.CharField("Короткое название", max_length=150)
    description = models.CharField("Краткое описание", max_length=250)
    text = models.TextField("Текст статьи")
    image = models.ImageField(upload_to='pages/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class CategoryArticles(models.Model):
    '''Категории статей'''
    title = models.CharField("Короткое название", max_length=150)
    description = models.CharField("Краткое описание", max_length=250)
    image = models.ImageField(upload_to='categorys/',
                              blank=True, null=True)  # поле для картинки

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Articles(models.Model):
    '''Статьи'''
    title = models.CharField("Короткое название", max_length=150)
    description = models.CharField("Краткое описание", max_length=250)
    text = models.TextField("Текст статьи")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    image = models.ImageField(upload_to='articles/',
                              blank=True, null=True)  # поле для картинки
    category = models.ForeignKey(CategoryArticles, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
