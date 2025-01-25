from .colors import Colors
from .warnings import EmailWarnings
from .server import Server

import email as _email, smtplib as _smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailMe:

    def __init__(self, username, password, location: str = 'smtp.gmail.com', port: int = 587) -> None:
        """init

        Args:
            username (str, callable): example callable -> lambda: os.getenv('USERNAME')
            password (str, callable): example callable -> lambda: os.getenv('PASSWORD')
        """        

        self.username = username
        self.password = password
        self.server = Server(self.username, self.password, location, port)

        return

    def update(self, email, message, subject: str = 'Update from EmailMe') -> None:

        with self.server as s:

            mail = MIMEMultipart()

            mail['From'] = s.get_username()
            mail['To'] = email
            mail['Subject'] = subject

            mail.attach(
                MIMEText(
                    message,
                    'html'
                )
            )

            s.send(mail)