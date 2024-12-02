from django.shortcuts import render, redirect
from app.settings.models import *

from django.core.mail import send_mail
from app.settings.utils import send_contact_email

# Create your views here.
def index(request):
    settings_id = Settings.objects.latest("id")
    image_all = Image.objects.all()
    kiko_all = KikoUpdate.objects.all()
    price_all = PriceKiko.objects.all()
    offers_all = Offers.objects.all()[:3]
    offers = Offers.objects.all()[3:]
    gallery_index_all = GalleryIndex.objects.all()
    return  render(request, 'base/index.html', locals())

def about(request):
    about = About.objects.latest("id")
    about_all = AboutPynkt.objects.all()
    return render(request, 'base/about-us/about.html', locals())


def contact(request):
    contact = Contact.objects.latest('id')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'Kiko - AI',
            f"""
            Здравствуйте.
            Спасибо за обратную связь, мы скоро с вами свяжемся.
            Ваше Имя: {name}
            Ваш email: {email}
            Ваше сообщение: {message}...
            """,
            "noreply@somehost.local",
            ["nurlanuuulubeksultan@gmail.com"],
        )
        print(f"Задача Celery: отправка контакта в очередь")
        send_contact_email.delay(name, email, message)

        return redirect('index')

    return render(request, 'base/contact-1/index.html', locals())

def gallery(request):
    gallery = Gallery.objects.latest("id")
    static_all = Statistic.objects.all()
    image_all = ImagePages.objects.all()
    gallery_all = GalleryPynkt.objects.all()
    return render(request, 'base/gallery/index.html', locals())

def news(request):
    news = News.objects.latest("id")
    news_all = NewsParagraph.objects.all()
    return render(request, 'base/news-page/index.html', locals())

def shop(request):
    shop = Shop.objects.latest("id")
    price_all = PriceShop.objects.all()
    price_blog_all = PriceBlog.objects.all()
    shop_blog_all = ShopBlog.objects.all()
    return render(request, 'base/shop1/index.html', locals())