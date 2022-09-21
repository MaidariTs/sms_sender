from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv()


def sending_sms(text, receiver):

    try:
        account_sid = os.getenv('SID')
        auth_token = os.getenv('AUTH_TOKEN')

        client = Client(account_sid, auth_token)

        client.messages.create(
            body=text,
            from_=os.getenv('SENDER_PHONE'),
            to=receiver
        )
        return 'The message was successfully sent'

    except Exception as ex:
        return 'Something was wrong...', ex


def main():
    text = input('Please enter your message: ')
    print(sending_sms(text=text, receiver=os.getenv('RECEIVER_PHONE')))


if __name__ == '__main__':
    main()
