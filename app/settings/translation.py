from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(KikoUpdate)
class KikoUpdateTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = (
        'title', 'descriptions', 'title_proposals', 'title_proposals_2',
        'descriptions_proposals', 'title_teahers', 'title_courses',
        'descriptions_courses', 'title_available', 'title_price',
        'title_suggestion', 'title_events', 'title_recommendations',
        'title_study', 'title_online_lessons', 'title_Education',
        'title_details_info', 'descriptions_details'
    )

@register(GalleryIndex)
class GalleryIndexTranslationOptions(TranslationOptions):
    fields = (
        'title', 'title2', 'descriptions', 'title2_2', 'title2_1', 'descriptions2'
    )

@register(PriceKiko)
class PriceKikoTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'details')

@register(Offers)
class OffersTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = (
        'title', 'title_contact', 'title_contact_2', 'descriptions',
        'title_books', 'descriptions_books', 'title_computer', 'descriptions_computer'
    )

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = (
        'title', 'title_origin', 'title_choice', 'title_lessons', 'descriptions',
        'title_about', 'title_about2', 'descriptions_about'
    )

@register(AboutPynkt)
class AboutPynktTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'plus1', 'plus2')

@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = (
        'title', 'title_gellary', 'title_discounts', 'title_Discounts_Available',
        'descriptions_discounts'
    )

@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

@register(GalleryPynkt)
class GalleryPynktTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'title_news', 'title_tuned', 'title_tuned2', 'descriptions_tuned')

@register(NewsParagraph)
class NewsParagraphTranslationOptions(TranslationOptions):
    fields = ('title', 'title2', 'descriptions')

@register(Shop)
class ShopTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'title_share', 'title_share2')

@register(PriceShop)
class PriceShopTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(PriceBlog)
class PriceBlogTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ShopBlog)
class ShopBlogTranslationOptions(TranslationOptions):
    fields = ('title', 'title2')
