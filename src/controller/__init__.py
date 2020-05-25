""" Controller Initialization """

from flask_restx import Api

from .mail_controller import NS as send_mail_ns

API = Api(
    version='0.1.0',
    title='Resume API',
    description='Resume REST API for generic api functionality'
)

API.add_namespace(send_mail_ns)
