from django.urls import path
from app.settings.views import index, about, contact, gallery, news, shop

urlpatterns = [
    path("", index, name='index'),
    path("about", about, name='about'),
    path("contact", contact, name='contact'),
    path("gallery", gallery, name='gallery'),
    path("news", news, name='news'),
    path("shop", shop, name='shop'),
]