# Real-time-Notification-System-for-E-commerce-Platform-# E-commerce Platform

## Overview
This is a scalable e-commerce platform with Django as the backend, Flask for notification services, and Kafka for message streaming.

## Project Structure
- **django_backend**: Contains the Django application for managing products and orders.
- **flask_notification_service**: A Flask application that handles email notifications.
- **kafka_setup**: Contains the Kafka setup using Docker.
- **aws**: Contains AWS configuration for sending emails and uploading files.

## Setup
1. Clone the repository.
2. Navigate to `django_backend` and install dependencies.
3. Run migrations and start the server.
4. Start the Flask notification service.
5. Set up Kafka using Docker.

## Technologies Used
- Django
- Flask
- Kafka
- AWS (SES, S3)

### Instructions to Run the Project

1. **Set Up Django Backend**:
   - Navigate to the `django_backend` folder.
   - Run the commands:
     ```bash
     python3 manage.py migrate
     python3 manage.py runserver
     ```

2. **Set Up Flask Notification Service**:
   - Navigate to the `flask_notification_service` folder.
   - Run:
     ```bash
     python3 app.py
     ```

3. **Set Up Kafka**:
   - Navigate to the `kafka_setup` folder.
   - Run:
     ```bash
     docker-compose up -d
     ```

4. **Interact with the AWS Services**:
   - Ensure that your AWS credentials are configured to use SES and S3.

### Notes:
- Make sure to install all necessary Python packages using `pip install <package_name>`, including `Django`, `Flask`, `kafka-python`, and `boto3`.
- Update your AWS configurations and secrets in the relevant files.

Feel free to modify the code as needed for your specific requirements! Let me know if you need any additional features or further explanations.
