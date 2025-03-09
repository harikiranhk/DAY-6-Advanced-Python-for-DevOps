# 🔹 Challenge 9: Implement a Python script that monitors Docker containers and sends alerts if a container crashes.

import docker
import time
import smtplib
import requests
from email.mime.text import MIMEText

# Docker client
client = docker.from_env()

# Email alert configuration
SMTP_SERVER = "smtp.gmail.com"  # Change this to your SMTP server
SMTP_PORT = 587
EMAIL_FROM = "your-email@gmail.com"
EMAIL_TO = "alert-recipient@gmail.com"
EMAIL_PASSWORD = "your-email-password"

# Slack alert configuration
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"  # Replace with your Slack webhook

def send_email_alert(container_name):
    """Sends an email alert when a container crashes."""
    subject = f"🚨 ALERT: Docker Container {container_name} Stopped!"
    body = f"The container '{container_name}' has stopped unexpectedly."
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print(f"📧 Email alert sent for {container_name}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def send_slack_alert(container_name):
    """Sends a Slack alert when a container crashes."""
    message = {
        "text": f"🚨 *ALERT:* Docker Container `{container_name}` has stopped unexpectedly!"
    }
    
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=message)
        if response.status_code == 200:
            print(f"💬 Slack alert sent for {container_name}")
        else:
            print(f"❌ Failed to send Slack alert: {response.text}")
    except Exception as e:
        print(f"❌ Slack request failed: {e}")

def monitor_containers():
    """Monitors Docker containers and alerts if any crash."""
    print("🔍 Monitoring Docker containers...")
    known_containers = {container.name: container.status for container in client.containers.list(all=True)}

    while True:
        for container in client.containers.list(all=True):
            if container.name in known_containers and container.status != "running":
                print(f"⚠️ {container.name} has stopped!")
                send_email_alert(container.name)
                send_slack_alert(container.name)
                known_containers[container.name] = container.status

        time.sleep(10)  # Check every 10 seconds

# Start monitoring
monitor_containers()