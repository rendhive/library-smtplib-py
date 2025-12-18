import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
username = "John Doe"
subject = "Template Email"

body = f"Hello {username},\n\nThis is a template email."
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Template email berhasil dikirim.")
# Fungsi: Mengirim email menggunakan template untuk personalisasi.
# Kondisi: Ketika Anda ingin menyesuaikan pesan untuk penerima.
