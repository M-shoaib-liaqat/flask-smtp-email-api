from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

# Replace these with your Gmail credentials
GMAIL_USER = "shoaibliaqat1010@gmail.com"
GMAIL_APP_PASSWORD = "kmob nqkp rrcg qfyz"

@app.route('/send-facility-email/', methods=['POST'])
def send_facility_email():
    try:
        data = request.get_json(force=True)
        print("📨 Received payload:", data)

        to = data.get('to')
        facility = data.get('facility')
        event = data.get('event')

        if not to or not facility or not event:
            return jsonify({'status': 'error', 'message': 'Missing fields'}), 400

        subject = f"Facility Approved for {event}"
        body = f'Your facility "{facility}" for event "{event}" has been approved. Please prepare accordingly.'

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = GMAIL_USER
        msg["To"] = to
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        print("🔥 Exception occurred:", str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500

# For WSGI
application = app
