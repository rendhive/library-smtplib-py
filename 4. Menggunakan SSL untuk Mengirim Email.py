import smtplib
from email.mime.text import MIMEText
from ssl import create_default_context

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "Secure Email"

msg = MIMEText("This is a secure email.")
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Mengirim email dengan SSL
context = create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Email yang aman berhasil dikirim.")
# Fungsi: Mengirim email dengan menggunakan koneksi SSL.
# Kondisi: Ketika Anda ingin memastikan keamanan saat mengirim data sensitif.
