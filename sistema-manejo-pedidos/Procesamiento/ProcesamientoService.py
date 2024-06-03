from kafka import KafkaConsumer, KafkaProducer
import json
import time

consumer = KafkaConsumer('Pedidos_Ingresados', bootstrap_servers='localhost:9092', group_id='procesamiento-group', value_serializer=lambda v: json.loads(v.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def procesar_pedido(pedido):
    estados = ['recibido', 'preparando', 'entregando', 'finalizado']
    for estado in estados:
        pedido['estado'] = estado
        producer.send('Pedidos_En_Proceso', value=pedido)
        producer.send('Pedidos_Notificaciones', value=pedido)
        time.sleep(10)  # Simulación de procesamiento

for message in consumer:
    pedido = message.value
    procesar_pedido(pedido)
