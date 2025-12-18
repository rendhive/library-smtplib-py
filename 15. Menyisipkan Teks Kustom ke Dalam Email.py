import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "Custom Text Email"

custom_text = "This is a custom text added to the email body."
msg = MIMEText(custom_text)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Email dengan teks kustom berhasil dikirim.")
# Fungsi: Menyisipkan teks kustom ke dalam body email.
# Kondisi: Ketika Anda ingin menambahkan informasi dinamis ke dalam email.
