import smtplib
from email.mime.text import MIMEText
from core.config import settings
from jinja2 import Environment, FileSystemLoader



def build_email_content(reservation, op='Confirmação'):
    subject = f'{op} de reserva'

    env = Environment(loader=FileSystemLoader('./static/'))
    template = env.get_template('reservation_email_template.html')

    template_data = {
        'user_name': reservation['user_name'],
        'session_id': reservation['session_id'],
        'confirmation_status': 'confirmada' if op == 'Confirmação' else 'cancelada',
        'reservation_id': reservation['id'],
        'movie_title': reservation['session']['movie']['title'],
        'session_begin': reservation['session']['begin']
    }

    message = template.render(template_data)
    return subject, message


def send_email(reservation, op='Confirmação'):
    try:
        subject, body = build_email_content(reservation, op)
        recipients = reservation['user_email']
        sender = settings.EMAIL_SENDER
        password = settings.EMAIL_APP_PASSWORD
        msg = MIMEText(body,'html')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
    except Exception as e:
        print(str(e))
        return False
    return True
