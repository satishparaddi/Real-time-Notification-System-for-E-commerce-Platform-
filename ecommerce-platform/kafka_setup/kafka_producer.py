from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_notification(message):
    producer.send('notifications', value=message.encode('utf-8'))
    producer.flush()

send_notification("Hello, this is a test notification!")
