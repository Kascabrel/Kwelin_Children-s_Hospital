from flask import Blueprint, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    return render_template('home.html', current_page='home')


@main_bp.route('/services')
def services():
    return render_template('service.html', current_page='services')


@main_bp.route('/about')
def about():
    return render_template('about.html', current_page='about')


@main_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Ici tu pourrais envoyer un email réel
        print(f" Message from {name} ({email}): {message}")

        flash("✅ Thank you for contacting us! We’ll get back to you soon.", "success")
        return redirect(url_for("main.contact"))

    return render_template(
        "contact.html",
        paypal_url=os.getenv("PAYPAL_DONATION_URL", "https://www.paypal.com/donate"),
        mtn=os.getenv("MTN_MOMO", "+237 XXX XXX XXX"),
        orange=os.getenv("ORANGE_MONEY", "+237 XXX XXX XX1"),
        email_contact=(os.getenv("EMAIL_CONTACT", "kascabrel@gmail.com")),
    )
