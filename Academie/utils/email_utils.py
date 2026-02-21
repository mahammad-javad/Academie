from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags





from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_custom_email(subject, to, context, template_name):
    if isinstance(to, str):
        to = [to]

    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=to,
        html_message=html_message,
        fail_silently=False
    )























# def send_custom_email(subject, message, recipient_list, from_email=None):
#     """
#     ارسال ایمیل به صورت عمومی
#     :param subject: عنوان ایمیل
#     :param message: متن ایمیل
#     :param recipient_list: لیست ایمیل گیرنده‌ها
#     :param from_email: ایمیل فرستنده، اگر None از DEFAULT_FROM_EMAIL استفاده می‌شود
#     """
#     if from_email is None:
#         from_email = settings.DEFAULT_FROM_EMAIL
#
#     send_mail(
#         subject=subject,
#         message=message,
#         from_email=from_email,
#         recipient_list=recipient_list,
#         fail_silently=False,  # True می‌کنید که خطاها در سایت نمایش داده نشه
#     )

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# def send_custom_email(subject, to, context, template_name, from_email=None):
#     """
#     ارسال ایمیل با استفاده از template
#
#     :param subject: عنوان ایمیل
#     :param to: ایمیل گیرنده (string) یا لیست ایمیل‌ها
#     :param context: دیکشنری داده‌ها برای template
#     :param template_name: مسیر template ایمیل
#     :param from_email: ایمیل فرستنده (اختیاری)
#     """
#
#     if from_email is None:
#         from_email = settings.DEFAULT_FROM_EMAIL
#
#     # اگر یک ایمیل بود، لیستش کن
#     if isinstance(to, str):
#         to = [to]
#
#     html_message = render_to_string(template_name, context)
#     plain_message = strip_tags(html_message)
#
#     send_mail(
#         subject=subject,
#         message=plain_message,
#         from_email=from_email,
#         recipient_list=to,
#         html_message=html_message,
#         fail_silently=False,
#     )


# def send_custom_email(subject, to, context, template_name):
#     try:
#         html_message = render_to_string(template_name, context)
#         plain_message = strip_tags(html_message)
#         from_email = settings.EMAIL_HOST_USER
#         send_mail(subject, plain_message, from_email, [to], html_message=html_message)
#     except Exception as e:
#         print(e)