"""Python code to illustrate Sending mail from"""
# your Gmail account
import smtplib
import ssl
import os
# pylint:disable=invalid-name
# creates SMTP session
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = os.environ.get("RESUME_EMAIL_ID")
receiver_email = os.environ.get("RESUME_EMAIL_ID")
password = os.environ.get("RESUME_EMAIL_PASSWORD")

msg = """\
Subject: Hey, someone's trying to reach you

"""


def send_mail(data):
    """sending the mail"""
    try:
        message = """\
            Name:{}
            Email: {}
            Phone: {}
            Message: {}""".format(data['name'], data['email'], data['phone'],
                                  data['message'])

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email,
                            msg+message)
        return {"message": "Mail Sent Successfully"}, 200
    except Exception:  # pylint:disable=broad-except
        return {
            "errorMsg": "Something went wrong"
        }, 500
