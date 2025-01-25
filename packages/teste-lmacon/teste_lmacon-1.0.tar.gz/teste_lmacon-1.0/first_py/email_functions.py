from botcity.plugins.email import BotEmailPlugin, MailServers

def enviar_email(usuario: str, senha: str) -> None:

    # Instantiate the plugin
    email = BotEmailPlugin.config_email(MailServers.GMAIL, usuario, senha)

    # Search for all emails with subject: Test Message
    messages = email.search('SUBJECT "Test Message"')

    # Lista para armazenar as informações dos e-mails
    emails_info = []

    # For each email found: prints the date, sender address and text content of the email
    for msg in messages:
        email_data = {
            "Date": msg.date_str,
            "From": msg.from_,
            "Message": msg.text
        }
        emails_info.append(email_data)

    return emails_info