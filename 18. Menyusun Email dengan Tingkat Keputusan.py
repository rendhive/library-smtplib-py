import smtplib
from email.mime.text import MIMEText

def decision_email(decision):
    sender = 'your_email@example.com'
    recipient = 'recipient@example.com'
    subject = "Decision Email"

    if decision == "Approve":
        body = "Your request has been approved."
    else:
        body = "Your request has been denied."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Mengirim email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, 'your_password')
        server.sendmail(sender, recipient, msg.as_string())

    print("Decision email sent successfully.")

# Simulasi pengiriman email
decision_email("Approve")
# Fungsi: Mengirim email berdasarkan keputusan yang diambil.
# Kondisi: Ketika Anda ingin memberi tahu penerima tentang hasil keputusan.
