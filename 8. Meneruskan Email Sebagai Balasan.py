import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "Reply to Your Email"

body = "Thank you for your message!"
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient
msg['In-Reply-To'] = '<message-id>'  # Tambahkan pengenal pesan jika perlu

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Balasan email berhasil dikirim.")
# Fungsi: Mengirim balasan ke email yang diterima sebelumnya.
# Kondisi: Ketika Anda ingin memberikan respons terhadap email yang diterima.
