import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "Test Email"
body = "Hello, this is a test email."

# Membuat objek MIMEText untuk email
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, [recipient], msg.as_string())

print("Email berhasil dikirim.")
# Fungsi: Mengirim email sederhana menggunakan SMTP.
# Kondisi: Ketika Anda ingin mengirim email notifikasi atau pemberitahuan.
