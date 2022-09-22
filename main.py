from dotenv import load_dotenv
import requests
import os


load_dotenv()


URL = 'https://sms.ru/sms/send?api_id={}&to={}&msg={}&json=1'


def sending_sms(text, receiver, api_id):

    try:

        response = requests.get(URL.format(api_id, receiver, text))
        response = response.json()
        return 'The message was successfully sent'

    except Exception as ex:
        return 'Something was wrong...', ex


def main():
    text = input('Please enter your message: ')
    text = str(text).split()
    text = '+'.join(text)
    print(sending_sms(
        text=text,
        receiver=os.getenv('RECEIVER_PHONE'),
        api_id=os.getenv('API_ID')
        ))


if __name__ == '__main__':
    main()
