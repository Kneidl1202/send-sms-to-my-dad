import imaplib
import email

FROM_EMAIL = "auermichaelgts@gmail.com"
FROM_PWD = "Johannes16."
SMTP_SERVER = "imap.gmail.com"

latest_EMAIL = [[], []]

is_gts_mail = True


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')

        mail_ids = data[0]

        id_list = mail_ids.split()
        latest_email_id = int(id_list[-1])

        email_from_return = []
        email_subject_return = []
        email_content_return = ""

        i = str(latest_email_id)
        typ, data = mail.fetch(i, str('(RFC822)'))

        for response_part in data:

            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode())
                email_subject = msg['subject']
                email_from = msg['from']

                email_subject_return.append(email_subject)
                email_from_return.append(email_from)
                email_content_return = msg

        return email_from_return, email_subject_return, email_content_return

    except:
        return 0