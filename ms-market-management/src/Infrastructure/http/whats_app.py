import random 
from twilio.rest import Client
import datetime


account_sid = # acount_sid twilio
auth_token = # token de autenticação twilio
client = Client(account_sid, auth_token)
twilio_numero_whats = 'whatsapp:+14155238886'

whats_numeros_destino = [] # numero de destino

numero_aleatorio = random.randint(1000, 9999)

for numero in whats_numeros_destino:
    message = client.messages.create(
        from = twilio_numero_whats,
        body = (
            'Olá,\n'
            'Este é seu código de verificação: ' + str(numero_aleatorio) + '\n'
            'Válido por uma hora'
            ),
            to = numero
    )
    print(f'Menssagem enviada para {numero} com sucesso')

    message_sid = message.sid
    message_status = client.messages(message_sid).fetch().status
    print(f'Status da mensagem: {message_status}')
    