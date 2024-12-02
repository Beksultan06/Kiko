from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactForm

@shared_task
def send_contact_email(name, email, message):
    try:
        # Отправляем почту пользователю
        send_mail(
            'Спасибо за ваш запрос',
            f"Здравствуйте, {name}!\n\nСпасибо за вашу обратную связь. Мы скоро с вами свяжемся.\n\nВаше сообщение: {message}",
            'noreply@somehost.local',
            [email],  # Почта пользователя
            fail_silently=False,
        )

        # Отправляем уведомление вам
        send_mail(
            'Новый запрос через контактную форму',
            f"Новый запрос на сайте Kiko - AI:\n\nИмя: {name}\nEmail: {email}\nСообщение: {message}",
            'noreply@somehost.local',
            ['kikobeam.ai@gmail.com'],  # Ваша почта
            fail_silently=False,
        )

        # Сохраняем данные в базе данных
        ContactForm.objects.create(name=name, email=email, message=message)
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")

