from twilio.rest import Client


account_sid = 'colocar_hash'
auth_token = 'colocar_hash'
twilio_numero_whats = 'whatsapp:+14155238886'
client = Client(account_sid, auth_token)

whats_numeros_destino = [] # numero de destino

def send_whatsapp_message(numero_destino, codigo):
    try:
        message = client.messages.create(
            from_=twilio_numero_whats,
            body=f'Seu código de ativação é: {codigo}. Válido por 1 hora.',
            to=f'whatsapp:{numero_destino}'
        )
        print(f'Mensagem enviada para {numero_destino}, SID: {message.sid}')
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")


    