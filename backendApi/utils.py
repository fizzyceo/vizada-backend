# utils.py
from django.core.mail import send_mail
from django.conf import settings

# def send_custom_email(subject, message, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL):
#     send_mail(
#         subject,
#         message,
#         from_email,
#         recipient_list,
#         fail_silently=False,
#     )

# def send_admin_email(subscribe_instance):
#     """
#     Send an email to the admin with the subscription and user information.
    
#     :param subscribe_instance: The newly created Subscribe instance
#     """
#     subject = 'New Subscription Created'
#     user = subscribe_instance.Id_user
#     message = (
#         f"A new subscription has been created.\n\n"
#         f"User Info:\n"
#         f"Name: {user.get_full_name}\n"
#         f"Email: {user.email}\n"
#         f"Phone: {user.ntel}\n"
#         f"\nSubscription Info:\n"
#         f"Subscription Type: {subscribe_instance.get_typeS_display()}\n"
#         f"Date of Subscription: {subscribe_instance.Datesub}\n"
#         # f"Active: {'Yes' if subscribe_instance.active else 'No'}\n"
#     )
#     recipient_list = [settings.ADMIN_EMAIL]  # Ensure you have an ADMIN_EMAIL set in your settings.py
    
#     send_custom_email(subject, message, recipient_list)


# utils.py
from django.core.mail import EmailMessage
from django.conf import settings

def send_custom_email(subject, message, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL):
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )

def send_admin_email(subscribe_instance):
   
    subject = 'Nouveau abonnement créer'
    user = subscribe_instance.Id_user
    html_content = f"""
    <html>
    <body>
        <h2>Vous avez un nouveau abbonenement crréer sur votre site web vizada</h2>
        <p><strong>Vueillez traiter l'abonnement ,Voici Info user:</strong></p>
        <ul>
            <li><strong>Name:</strong> {user.get_full_name}</li>
            <li><strong>Email:</strong> {user.email}</li>
            <li><strong>Phone:</strong> {user.get_phone_number}</li>
        </ul>
        <p><strong>Subscription Info:</strong></p>
        <ul>
            <li><strong>Subscription Type:</strong> {subscribe_instance.get_typeS_display()}</li>
            <li><strong>Date of Subscription:</strong> {subscribe_instance.Datesub}</li>
            <li><strong>Montant payé:</strong> {subscribe_instance.get_price()}</li>
                        <li><strong>Catégorie:</strong> {subscribe_instance.get_category_display()}</li>

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
