import smtplib
from email.mime.text import MIMEText

def configure_test_email():
    sender = 'your_email@example.com'
    recipient = 'test@example.com'
    subject = "Test Configuration"

    body = "This is a test email to check configuration."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Mengirim email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, 'your_password')
            server.sendmail(sender, recipient, msg.as_string())
        print("Test email sent successfully.")
    except Exception as e:
        print("Failed to send test email:", e)

configure_test_email()
# Fungsi: Mengonfigurasi dan mengirim email untuk menguji pengaturan.
# Kondisi: Ketika Anda ingin memverifikasi bahwa semua pengaturan berfungsi dengan baik.
