import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipients = ['recipient1@example.com', 'recipient2@example.com']
subject = "Group Email"

msg = MIMEText("Hello, this is a group email.")
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = ", ".join(recipients)

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipients, msg.as_string())

print("Email berhasil dikirim ke beberapa penerima.")
# Fungsi: Mengirim email ke beberapa penerima sekaligus.
# Kondisi: Ketika Anda perlu mengirim informasi ke grup orang.
