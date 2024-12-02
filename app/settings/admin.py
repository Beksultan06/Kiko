from django.contrib import admin
from app.settings.models import *
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Image)

# @admin.register(KikoUpdate)
# class KikoUpdateAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']

class KikoUpdateAdmin(TranslationAdmin):
    list_display = ('title', 'title_en', 'descriptions', 'descriptions_en', 'image_preview')
    search_fields = ('title', 'descriptions')

    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" />') if obj.image else 'Нет изображения'
    image_preview.short_description = 'Фото'

    class Meta:
        model = KikoUpdate

admin.site.register(KikoUpdate, KikoUpdateAdmin)

@admin.register(PriceKiko)
class PriceKikoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']

@admin.register(Offers)
class OffersAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']

#########################################################

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

############################################################

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(AboutPynkt)
class AboutPynktAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

############################################################

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(ImagePages)

@admin.register(GalleryPynkt)
class GalleryPynktAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

###############################################################

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(NewsParagraph)
class NewsParagraphAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

###############################################################

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(PriceShop)
class PriceShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']

@admin.register(PriceBlog)
class PriceBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']

@admin.register(ShopBlog)
class ShopBlog(admin.ModelAdmin):
    list_display = ['id', 'title', 'title2']