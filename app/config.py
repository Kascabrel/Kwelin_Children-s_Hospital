import os

class Config:
    # Flask secret key
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")

    # Contact infos
    CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "yourclinic@email.com")
    CONTACT_PHONE = os.environ.get("CONTACT_PHONE", "+237 600 000 000")

    # Donation configs
    PAYPAL_DONATION_URL = os.environ.get(
        "PAYPAL_DONATION_URL",
        "https://www.paypal.com/donate/?hosted_button_id=XXXXXXXX"
    )
    MTN_MOMO = os.environ.get("MTN_MOMO", "+237 67X XXX XXX")
    ORANGE_MONEY = os.environ.get("ORANGE_MONEY", "+237 69X XXX XXX")
