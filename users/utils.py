# utils.py
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail

def send_custom_email(subject, message, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL):
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )

def send_admin_email(user):
    """
    Send an email to the admin with the new user information.
    
    :param user: The newly created User instance
    """
    subject = 'New User Registered'
    html_content = f"""
    <html>
    <body>
        <h2>New User Registered</h2>
        <p><strong>User Info:</strong></p>
        <ul>
            <li><strong>Name:</strong> {user.get_full_name}</li>
            <li><strong>Email:</strong> {user.email}</li>
        </ul>
    </body>
    </html>
    """
    recipient_list = [settings.ADMIN_EMAIL]  
    
    email = EmailMessage(
        subject,
        html_content,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list
    )
    email.content_subtype = 'html'  
    email.send()


def send_contactus_email(subject, message, recipient_list, sender_email, from_email=settings.DEFAULT_FROM_EMAIL): 
    """ 
    Send a contact us email to the admin with the provided subject, message, and sender email. 
 
    :param subject: The subject of the email. 
    :param message: The message body of the email. 
    :param recipient_list: List of recipients to send the email to. 
    :param sender_email: The email address of the sender. 
    :param from_email: The sender's email address. 
    """ 
    full_subject = f"contact-us: {subject}" 
    message_with_email = f"Email from: {sender_email}\n\n Message:{message}" 
    send_mail( 
        full_subject, 
        message_with_email, 
        from_email, 
        recipient_list, 
        fail_silently=False, 
    )