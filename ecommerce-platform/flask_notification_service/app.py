from flask import Flask
from kafka_consumer import start_consumer

app = Flask(__name__)

@app.route('/')
def home():
    return "Real-time Notification Service"

if __name__ == '__main__':
    start_consumer()  # Start Kafka consumer to listen for messages
    app.run(debug=True)
