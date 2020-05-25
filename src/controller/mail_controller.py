""" Comtroller for Mailing """

from flask import request
from flask_restx import Namespace, Resource

from schema.mail_content_fields import message
from service.mail import send_mail

NS = Namespace(
    'api/send-mail',
    description="Operation capable of sending mail"
)

MAIL_BODY = NS.model("Mail_Body", message())


@NS.route("")
class SendMail(Resource):
    """ Send mail class """

    @NS.expect(MAIL_BODY, validate=True)
    def post(self):
        """ Send Mail Controller """
        return send_mail(request.json)
