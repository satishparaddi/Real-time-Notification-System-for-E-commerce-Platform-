from kafka import KafkaConsumer
from notification_sender import send_email

def start_consumer():
    consumer = KafkaConsumer('notifications', bootstrap_servers='localhost:9092')
    for message in consumer:
        event_data = message.value.decode('utf-8')
        # Process the event (e.g., order confirmation)
        send_email(event_data)
