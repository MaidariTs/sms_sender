# sms_sender
This little project can send sms message to your phone number.
```

Instruction:

1. Clone and create a virtual environment:
    git clone git@github.com:MaidariTs/sms_sender.git
    python -m venv venv
    source venv/Scripts/activate

2. Install Requirements:
    pip install -r requirements.txt

3. Register on the site 'https://www.twilio.com/'

4. Create an '.env' file in the project directory and enter your data in it:
    SID = ''
    AUTH_TOKEN = ''
    SENDER_PHONE = ''
    RECEIVER_PHONE = ''

5. It`s all