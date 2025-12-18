import smtplib
from email.mime.text import MIMEText

def send_error_notification(error_message):
    sender = 'your_email@example.com'
    recipient = 'recipient@example.com'
    subject = "Error Notification"

    msg = MIMEText(f"An error occurred:\n\n{error_message}")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Mengirim email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, 'your_password')
            server.sendmail(sender, recipient, msg.as_string())
        print("Error notification sent successfully.")
    except Exception as e:
        print("Failed to send error notification:", e)

# Simulasi pengiriman Notifikasi kesalahan
send_error_notification("Failed to connect to the database.")
# Fungsi: Mengirim pemberitahuan ketika terjadi kesalahan dalam program.
# Kondisi: Ketika Anda perlu mendeteksi dan menginformasikan kesalahan.
