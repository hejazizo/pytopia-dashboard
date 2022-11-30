import os
import json

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    from db.models import BannedWord, Message, User

    with open('data/pytopia_short.json', 'r') as f:
        data = json.load(f)

    # Drop previous data
    for user in User.objects.all():
        user.delete()
    for msg in Message.objects.all():
        msg.delete()

    # Populate data
    for message in data['messages']:
        if message['type'] != 'message':
            continue

        user, _ = User.objects.get_or_create(
            id=int(message['from_id'].replace('user', '')),
            username=message['from'],
        )

        plain_text = message['text']
        if type(message['text']) != str:
            plain_text = ""
            for part in message['text']:
                if type(part) == str:
                    plain_text += part
                else:
                    plain_text += part['text']

        Message.objects.create(
            message_id=message['id'],
            text=plain_text,
            user=user,
            date=message['date'],
        )

