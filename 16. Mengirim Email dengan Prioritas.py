import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "Important Email"

msg = MIMEText("This is an important message.")
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient
msg['X-Priority'] = '1'  # Highest priority

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Email dengan prioritas tinggi berhasil dikirim.")
# Fungsi: Mengirim email dengan pengaturan prioritas untuk menarik perhatian penerima.
# Kondisi: Ketika Anda ingin menandakan email penting.
