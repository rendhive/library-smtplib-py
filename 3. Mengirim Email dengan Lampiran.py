import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
subject = "Email with Attachment"

# Membuat objek MIMEMultipart
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject

# Menambahkan body email
body = "Please see the attached file."
msg.attach(MIMEText(body, 'plain'))

# Menambahkan lampiran
filename = "file.txt"
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(part)

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

attachment.close()
print("Email dengan lampiran berhasil dikirim.")
# Fungsi: Mengirim email dengan lampiran.
# Kondisi: Ketika Anda perlu mengirim dokumen atau file dengan email.
