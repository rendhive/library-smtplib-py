import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "HTML Email"

# Menggunakan HTML untuk isi body
body = "<h1>Hello</h1><p>This is an email with HTML formatting.</p>"
msg = MIMEText(body, 'html')
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Email dengan format HTML berhasil dikirim.")
# Fungsi: Mengirim email dengan konten HTML.
# Kondisi: Ketika Anda ingin mengirim email dengan format yang lebih menarik.
