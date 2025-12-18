import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "Notification"

msg = MIMEText("This is a notification email.")
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Notifikasi email berhasil dikirim.")
# Fungsi: Mengirim email untuk memberikan notifikasi kepada pengguna.
# Kondisi: Ketika Anda membutuhkan pengingat atau informasi penting yang perlu diperhatikan.
