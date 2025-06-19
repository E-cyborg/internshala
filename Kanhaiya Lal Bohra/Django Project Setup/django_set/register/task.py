from celery import shared_task
from django.core.mail import send_mail
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from .bot import run_bot

@shared_task
def send__email(to_email):
    subject = "Welcome to our site!"
    message = "Thanks for signing up!"
    from_email = "your-email@gmail.com"

    send_mail(subject, message, from_email, [to_email])


@shared_task
def runbot():
    run_bot()

