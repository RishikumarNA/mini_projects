
from twilio.rest import Client

account_sid = 'ACf7959623a4275162a5679d91dcb06643'
auth_token = '59bf9757a4ebc5bb75a697f4fcce9ec6'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12343322418',
  body='iuhsiudcuxucuzxuvchvhcvcivcnvcj',
  to='+919791345488'
)

print(message.sid)