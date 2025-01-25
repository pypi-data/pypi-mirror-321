import email as _email, smtplib as _smtplib
from .colors import Colors
from .warnings import EmailWarnings

class Server:

    def __init__(self, username, password, location: str = 'smtp.gmail.com', port: int = 587) -> None:

        self.login(username, password)

        self.location = location
        self.port = port

        return
    
    def login(self, username, password) -> None:
        """Save username and password or callables to get them

        Args:
            username (str, callable): example callable -> lambda: os.getenv('USERNAME')
            password (str, callable): example callable -> lambda: os.getenv('PASSWORD')
            server (str, optional):. Defaults to 'smtp.gmail.com'.
            port (int, optional):. Defaults to 587.
        """             

        self.username = username
        self.password = password

        self.login_sucsess = True

        return
    
    def get_username(self) -> str:

        return self.username if isinstance(self.username, str) else self.username()
    
    def get_password(self) -> str:

        return self.password if isinstance(self.password, str) else self.password()
    
    def send(self, msg) -> None:

        self.server.send_message(msg)
    
    def __enter__(self):

        self.server = _smtplib.SMTP(self.location, self.port)

        self.server.starttls()

        u = self.get_username()
        pw = self.get_password()

        self.server.login(u, pw)

        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:

        self.server.quit()

        del self.server

        return
    
