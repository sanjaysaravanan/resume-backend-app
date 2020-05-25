""" Fields for mail message """

from flask_restx import fields


def message():
    """ Fields for message """

    return {
        "name": fields.String(
            required=True,
            example="Sanjay Saravanan"
        ),
        "email": fields.String(
            required=True,
            example="Enter a email",
            pattern=r"^([a-zA-Z0-9_\-\.]+){1,64}@([a-zA-Z0-9_\-\.]+)"
                    r"{1,255}\.([a-zA-Z]{2,5})$",
        ),
        "phone": fields.String(
            required=True,
            example="Enter a phone number",
            pattern=r"^([0-9]+){10}$"
        ),
        "message": fields.String(
            required=True,
            example="Enter a message"
        )
    }
