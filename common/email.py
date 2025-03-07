from django.core.mail import send_mail


def send_email(subject, body, sender, to_list, fail_silently=False):
    """問い合わせのメール処理"""
    send_mail(subject, body, sender, to_list, fail_silently)
