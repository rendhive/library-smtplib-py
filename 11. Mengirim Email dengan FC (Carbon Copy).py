import smtplib
from email.mime.text import MIMEText

# Menyiapkan informasi email
sender = 'your_email@example.com'
recipient = 'recipient@example.com'
cc = 'cc_recipient@example.com'
subject = "CC Email"

msg = MIMEText("This is an email with CC recipient.")
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient
msg['Cc'] = cc

# Mengirim email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, [recipient, cc], msg.as_string())

print("Email dengan CC berhasil dikirim.")
# Fungsi: Mengirim email dengan salinan ke penerima CC.
# Kondisi: Ketika Anda ingin memberikan informasi yang sama ke beberapa pihak.
