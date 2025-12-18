import smtplib
from email.mime.text import MIMEText

try:
    sender = 'your_email@example.com'
    recipient = 'recipient@example.com'
    subject = "Test Email With Error Handling"

    body = "This email includes error handling example."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Mengirim email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, 'your_password')
        server.sendmail(sender, recipient, msg.as_string())
    print("Email berhasil dikirim.")
except Exception as e:
    print("Gagal mengirim email:", e)
# Fungsi: Menangani kesalahan yang mungkin terjadi saat mengirim email.
# Kondisi: Ketika Anda ingin menjaga aplikasi tetap berjalan meskipun ada kendala saat mengirim email.
