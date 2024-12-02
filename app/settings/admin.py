from django.contrib import admin
from app.settings.models import *
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin


class KikoUpdateAdmin(TranslationAdmin):
    list_display = ('title', 'title_en', 'descriptions', 'descriptions_en', 'image_preview')
    search_fields = ('title', 'descriptions')

    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" />') if obj.image else 'Нет изображения'
    image_preview.short_description = 'Фото'

    class Meta:
        model = KikoUpdate

admin.site.register(KikoUpdate, KikoUpdateAdmin)
# Generic method for displaying image preview
def image_preview(obj, field_name):
    """Generate an image preview for the admin."""
    if getattr(obj, field_name):
        return mark_safe(f'<img src="{getattr(obj, field_name).url}" width="100" />')
    return 'Нет изображения'

image_preview.short_description = 'Фото'

# ModelAdmin for Settings
@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'descriptions', 'descriptions_en']
    search_fields = ['title', 'descriptions']

# ModelAdmin for PriceKiko
@admin.register(PriceKiko)
class PriceKikoAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'price', 'image_preview']
    search_fields = ['title', 'descriptions']

    def image_preview(self, obj):
        return image_preview(obj, 'image')

# ModelAdmin for Offers
@admin.register(Offers)
class OffersAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'price', 'image_preview']
    search_fields = ['title', 'descriptions']

    def image_preview(self, obj):
        return image_preview(obj, 'image')

# ModelAdmin for GalleryIndex
@admin.register(GalleryIndex)
class GalleryIndexAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'title2', 'title2_en', 'descriptions', 'descriptions_en']
    search_fields = ['title', 'descriptions']

# ModelAdmin for Contact
@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'title_contact', 'title_contact_en', 'image_preview']
    search_fields = ['title', 'descriptions']

    def image_preview(self, obj):
        return image_preview(obj, 'image')

# ModelAdmin for ContactForm
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

# ModelAdmin for About
@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'title_origin', 'title_origin_en', 'title_choice', 'title_choice_en', 'descriptions', 'descriptions_en']
    search_fields = ['title', 'descriptions']

# ModelAdmin for AboutPynkt
@admin.register(AboutPynkt)
class AboutPynktAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'descriptions', 'descriptions_en', 'plus1', 'plus1_en', 'plus2', 'plus2_en']
    search_fields = ['title', 'descriptions']

# ModelAdmin for Gallery
@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'title_gellary', 'title_gellary_en', 'title_discounts', 'title_discounts_en', 'title_Discounts_Available', 'title_Discounts_Available_en', 'descriptions_discounts', 'descriptions_discounts_en', 'image_preview']
    search_fields = ['title', 'descriptions']

    def image_preview(self, obj):
        return image_preview(obj, 'image')

# ModelAdmin for Statistic
@admin.register(Statistic)
class StatisticAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'descriptions', 'descriptions_en']
    search_fields = ['title', 'descriptions']

# ModelAdmin for GalleryPynkt
@admin.register(GalleryPynkt)
class GalleryPynktAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'descriptions', 'descriptions_en']
    search_fields = ['title', 'descriptions']

# ModelAdmin for News
@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'title_news', 'title_news_en', 'title_tuned', 'title_tuned_en', 'title_tuned2', 'title_tuned2_en', 'descriptions_tuned', 'descriptions_tuned_en', 'image_preview']
    search_fields = ['title', 'descriptions']

    def image_preview(self, obj):
        return image_preview(obj, 'image')

# ModelAdmin for NewsParagraph
@admin.register(NewsParagraph)
class NewsParagraphAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'title2', 'title2_en', 'descriptions', 'descriptions_en']
    search_fields = ['title', 'descriptions']

# ModelAdmin for Shop
@admin.register(Shop)
class ShopAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'title_share', 'title_share_en', 'title_share2', 'title_share2_en']
    search_fields = ['title', 'descriptions']

# ModelAdmin for PriceShop
@admin.register(PriceShop)
class PriceShopAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'price', 'image_preview']
    search_fields = ['title']

    def image_preview(self, obj):
        return image_preview(obj, 'image')

# ModelAdmin for PriceBlog
@admin.register(PriceBlog)
class PriceBlogAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'price', 'image_preview']
    search_fields = ['title']

    def image_preview(self, obj):
        return image_preview(obj, 'image')

# ModelAdmin for ShopBlog
@admin.register(ShopBlog)
class ShopBlogAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'title_en', 'title2', 'title2_en']
    search_fields = ['title']

# Register ImagePages as normal (no translation)
admin.site.register(ImagePages)

# Register Image model for displaying images in the admin
admin.site.register(Image)