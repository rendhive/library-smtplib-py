import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "Email with Link"

body = "Click this link to visit: https://www.example.com"
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Email dengan tautan berhasil dikirim.")
# Fungsi: Mengirim email yang berisi tautan.
# Kondisi: Ketika Anda ingin mengarahkan penerima ke situs web atau dokumen lain.
