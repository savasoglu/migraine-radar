import os

from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_TOKEN')
number = os.environ.get('TWILIO_NUMBER')

client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> str:
    message = client.messages.create(
        to=to,
        from_=number,
        body=message
    )

    return message.sid
