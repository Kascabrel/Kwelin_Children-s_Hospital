import os

class Config:
    # Flask secret key
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")

    # Contact infos

    # Mail config (exemple avec Gmail SMTP)
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "kascabrel@gmail.com")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "votre_mot_de_passe_app")  # utiliser un mot de passe d’application
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "kascabrel@gmail.com")

    PAYPAL_DONATION_URL = os.getenv("PAYPAL_DONATION_URL", "https://www.paypal.com/donate")
    MTN_MOMO = os.getenv("MTN_MOMO", "+237 XXX XXX XXX")
    ORANGE_MONEY = os.getenv("ORANGE_MONEY", "+237 XXX XXX XX1")
    EMAIL_CONTACT = os.getenv("EMAIL_CONTACT", "kascabrel@gmail.com")