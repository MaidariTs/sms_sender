# sms_sender
This little project can send sms message to your phone number.
```

Instruction:

1. Clone and create a virtual environment:
    git clone git@github.com:MaidariTs/sms_sender.git
    python -m venv venv
    source venv/Scripts/activate

2. Install requirements:
    pip install -r requirements.txt

3. Register on the site 'https://www.sms.ru/', where u can get an API_ID

4. Create an '.env' file in the project directory and enter your data in it:
    RECEIVER_PHONE = ''
    API_ID = ''

5. It`s all