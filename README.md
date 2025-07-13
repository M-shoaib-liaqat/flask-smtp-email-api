# Flask SMTP Email API

This Flask app sends approval emails using Gmail SMTP.

## Setup

1. Replace `GMAIL_USER` and `GMAIL_APP_PASSWORD` in `app.py` with your Gmail email and app password.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```

## API Endpoint

### POST `/send-facility-email/`

**JSON Payload:**
```json
{
  "to": "recipient@example.com",
  "facility": "multimedia",
  "event": "Annual Day"
}
```

**Response:**
- `200 OK` with `{ "status": "success" }` on success
- `400 Bad Request` if fields are missing
- `500 Internal Server Error` on failure
