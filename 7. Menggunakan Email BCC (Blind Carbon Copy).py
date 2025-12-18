import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipients = ['recipient1@example.com']
bcc_recipients = ['bcc_recipient@example.com']
subject = "BCC Email"

msg = MIMEText("This is an email with BCC recipients.")
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = ", ".join(recipients)

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipients + bcc_recipients, msg.as_string())

print("Email berhasil dikirim dengan BCC.")
# Fungsi: Mengirim email dengan penerima BCC.
# Kondisi: Ketika Anda ingin mengirimkan salinan tanpa penerima lain mengetahui siapa yang menerima.
