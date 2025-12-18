import smtplib
from email.mime.text import MIMEText

def request_email():
    sender = 'your_email@example.com'
    recipient = 'recipient@example.com'
    subject = "Email Request"

    body = "Can you confirm receipt of this request?"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Mengirim email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, 'your_password')
        server.sendmail(sender, recipient, msg.as_string())

    print("Request email sent successfully.")

# Simulasi pengiriman permintaan
request_email()
# Fungsi: Mengirim suatu permintaan melalui email.
# Kondisi: Ketika Anda ingin meminta konfirmasi atau jawaban dari kapan saja.
