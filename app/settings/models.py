from django.db import models
from ckeditor.fields import RichTextField

from app.settings.icon import ICON

# Create your models here.
class Settings(models.Model):
    title = RichTextField(
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    title_proposals = models.CharField(
        max_length=100,
        verbose_name='Заголовка Предложений'
    )
    title_proposals_2 = models.CharField(
        max_length=100,
        verbose_name='Заголовка Школы'
    )
    descriptions_proposals = RichTextField(
        verbose_name='Описание Предложения'
    )
    image2 = models.ImageField(
        upload_to='settings',
        verbose_name='Фото Предложения'
    )
    title_teahers = models.CharField(
        max_length=155,
        verbose_name='Заголовка Учильки'
    )
    title_courses = models.CharField(
        max_length=155,
        verbose_name='Заголовка Курсов'
    )
    descriptions_courses = RichTextField(
        verbose_name='Описание курсов'
    )
    image3 = models.ImageField(
        upload_to='settings',
        verbose_name='Фото курсов - 1'
    )
    image4 = models.ImageField(
        upload_to='settings',
        verbose_name='Фото курсов - 2'
    )
    title_available = models.CharField(
        max_length=155,
        verbose_name='Заголовка Доступности'
    )
    title_price = models.CharField(
        max_length=155,
        verbose_name='Заголовка Цены'
    )
    image5 = models.ImageField(
        upload_to='settings',
        verbose_name='Фото Цены'
    )
    title_suggestion = models.CharField(
        max_length=155,
        verbose_name='Заголовка Предположение'
    )
    title_events = models.CharField(
        max_length=155,
        verbose_name='Заголовка Мероприятий'
    )
    title_recommendations = models.CharField(
        max_length=155,
        verbose_name='Заголовка рекомендации'
    )
    title_study = models.CharField(
        max_length=155,
        verbose_name='Заголовка исследования'
    )
    image6 = models.ImageField(
        upload_to='settings',
        verbose_name='Фото рекомендации'
    )
    title_online_lessons = models.CharField(
        max_length=155,
        verbose_name='Заголовка Онлайн урока'
    )
    title_Education = models.CharField(
        max_length=155,
        verbose_name='Заголовка Образование'
    )
    title_details_info = models.CharField(
        max_length=155,
        verbose_name='Заголовка Детального просмотра'
    )
    descriptions_details = RichTextField(
        verbose_name='Описание Детального просмотра'
    )
    image7 = models.ImageField(
        upload_to='settings',
        verbose_name='Фото Детального просмотра'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройки Главной страницы'

class Image(models.Model):
    image1 = models.ImageField(
        upload_to='image',
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to='image',
        verbose_name='Фото 2'
    )

    class Meta:
        verbose_name_plural = 'Галлерия'

class KikoUpdate(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='kiko/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Обновленный Kiko'

class PriceKiko(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    imgae = models.ImageField(
        upload_to='price_kiko/',
        verbose_name='Фото',
        blank=True, null=True
    )
    details = models.CharField(
        max_length=100,
        verbose_name='Просмотры детально'
    )
    icon = models.CharField(
        max_length=50,
        verbose_name='Иконка',
        choices=ICON
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Цены на Kiko'

class Offers(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    image = models.ImageField(
        upload_to='offers/',
        verbose_name='ФОто'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'предложения'


##############################################

class Contact(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to='contact/',
        verbose_name='Фото'
    )
    title_contact = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    title_contact_2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка - 2'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    title_books = models.CharField(
        max_length=155,
        verbose_name='Заголовка Книги предоставлены'
    )
    descriptions_books = RichTextField(
        verbose_name='Описание Книги предоставлены'
    )
    image_books = models.ImageField(
        upload_to='contact',
        verbose_name='Фото'
    )
    title_computer = models.CharField(
        max_length=155,
        verbose_name='Заголовка Компьютерный зал '
    )
    descriptions_computer = RichTextField(
        verbose_name='Описание Компьютерный зал'
    )
    image_computer = models.ImageField(
        upload_to='contact',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наши контакты'

class ContactForm(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = RichTextField(
        verbose_name='Сообщение'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Форма контакта'

########################################################

class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )
    title_origin = models.CharField(
        max_length=155,
        verbose_name='Заголовка происхождение'
    )
    title_choice = models.CharField(
        max_length=155,
        verbose_name='Заголовка Выбара'
    )
    title_lessons = models.CharField(
        max_length=155,
        verbose_name='Заголовка Урока'
    )
    descriptions = RichTextField(
        verbose_name='Описание Урока'
    )
    title_about = models.CharField(
        max_length=155,
        verbose_name='Заголовка о нас'
    )
    title_about2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка о нас 2'
    )
    descriptions_about = RichTextField(
        verbose_name='Описание о нас '
    )
    image_abotu = models.ImageField(
        upload_to='about/about',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'О нас'

class AboutPynkt(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    number = models.IntegerField(
        verbose_name='Нумерация'
    )
    plus1 = models.CharField(
        max_length=155,
        verbose_name='Плюсы 1 '
    )
    plus2 = models.CharField(
        max_length=155,
        verbose_name='Плюсы 2 '
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Пункты О нас'

###################################################

class Gallery(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to='gallery',
        verbose_name='Фото'
    )
    title_gellary = RichTextField(
        verbose_name='Заголовка'
    )
    title_discounts = models.CharField(
        max_length=155,
        verbose_name='Заголовка скидки'
    )
    title_Discounts_Available = models.CharField(
        max_length=155,
        verbose_name='Заголовка Доступные скидки'
    )
    descriptions_discounts = RichTextField(
        verbose_name='Описание'
    )
    image_discounts = models.ImageField(
        upload_to='gallery',
        verbose_name='Фото скидки'
    )
    image_static = models.ImageField(
        upload_to='static/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Страница Галлерия'

class Statistic(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    static = models.IntegerField(
        verbose_name='Статистика'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статистика'

class ImagePages(models.Model):
    image1 = models.ImageField(
        upload_to='image',
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to='image',
        verbose_name='Фото 2'
    )

    class Meta:
        verbose_name_plural = 'Фото'

class GalleryPynkt(models.Model):
    title= models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='Пункты Галлерий',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Пункты Галлерий'

###########################################

class News(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='news',
        verbose_name='Фото'
    )
    title_news = models.CharField(
        max_length=155,
        verbose_name='Заголовка Новостей'
    )
    title_tuned = models.CharField(
        max_length=155,
        verbose_name='Заголовка настроенный'
    )
    title_tuned2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка под настроенный'
    )
    descriptions_tuned = RichTextField(
        verbose_name='Описание настроенный'
    )
    image1 = models.ImageField(
        upload_to='news',
        verbose_name='Фото'
    )
    image2 = models.ImageField(
        upload_to='news',
        verbose_name='Фото'
    )
    image_back = models.ImageField(
        upload_to='Фото на заднем фоне'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'

class NewsParagraph(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Параграф новостей'

########################################################

class Shop(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='shop',
        verbose_name='Фото'
    )
    title_share = models.CharField(
        max_length=155,
        verbose_name='Заголовка Акций'
    )
    title_share2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка Акций 2'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Магазин'

class PriceShop(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    image = models.ImageField(
        upload_to='priceshop',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Цена Магазин'

class PriceBlog(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    image = models.ImageField(
        upload_to='priceshop',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Блог Цены'

class ShopBlog(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка 1'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка 2'
    )
    image = models.ImageField(
        upload_to='priceshop',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Блог Магазин'