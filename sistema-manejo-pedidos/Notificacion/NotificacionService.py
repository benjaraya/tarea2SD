from kafka import KafkaConsumer
import smtplib
import json

consumer = KafkaConsumer('Pedidos_Notificaciones', bootstrap_servers='localhost:9092', group_id='notificacion-group', value_serializer=lambda v: json.loads(v.decode('utf-8')))

def enviar_correo(pedido):
    server = smtplib.SMTP('localhost')
    server.sendmail('from@example.com', 'to@example.com', f"Estado del pedido {pedido['id']}: {pedido['estado']}")
    server.quit()

for message in consumer:
    pedido = message.value
    enviar_correo(pedido)
