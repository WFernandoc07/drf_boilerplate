from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

class Mailing:
    def __init__(self):
        self.sender = settings.EMAIL_HOST_USER
    

    def email_reset_password(self, recipient, name, password):
        html = render_to_string(
            template_name='reset_password.html',
            context={'name': name, 'password': password}
        )
        return self.__send_email(
            f'Reseteo de contraseña - {name}',
            [recipient],
            html
        )

    def __send_email(self, subject, recipients, html):
        return send_mail(
            message=None,
            subject=subject,
            recipient_list=recipients,
            html_message=html,
            from_email=self.sender
        )
            

