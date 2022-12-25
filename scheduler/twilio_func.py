# whatsapp bot and twilio func are two different routes. here, user is not trigerring, whenever the day of the reminder comes, at 9am it is getting self triggered and sending a reminder, as opposed to the user triggered whatsapp bot

from twilio.rest import Client

account_sid="ACfbaf09f396affd820a988129dd37ed6e"
auth_token = "2378515d5948e82e6f5d812fdc5a3a34"
client = Client(account_sid, auth_token)

def send_rem(date,rem):
    message = client.messages.create(
        from_ = 'whatsapp:+14155238886',
        body = 'REMINDER '+date+"\n"+rem,
        to = 'whatsapp:8850621671'
    )
    print(message.sid)