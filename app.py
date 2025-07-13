from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

# Replace with your Gmail credentials (App Password recommended)
GMAIL_USER = "shoaibliaqat1010@gmail.com"
GMAIL_APP_PASSWORD = "kmob nqkp rrcg qfyz"  # Replace with your real app password

@app.route('/send-facility-email/', methods=['POST'])
def send_facility_email():
    try:
        data = request.get_json(force=True)
        print("📨 Received payload:", data)

        recipients = data.get('recipients')  # Expecting a list of emails
        facility = data.get('facility')
        event = data.get('event')

        if not recipients or not isinstance(recipients, list) or not facility or not event:
            return jsonify({'status': 'error', 'message': 'Missing or invalid fields'}), 400

        subject = f"Facility Approved for {event}"
        body = f'Your facility "{facility}" for event "{event}" has been approved. Please prepare accordingly.'

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = GMAIL_USER
        msg["To"] = ", ".join(recipients)
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)

        print(f"✅ Email sent to {', '.join(recipients)}")
        return jsonify({'status': 'success'}), 200

    except Exception as e:
        print("🔥 Exception occurred:", str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500

# For WSGI deployment (e.g., on Render)
application = app
