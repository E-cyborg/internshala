from django.apps import AppConfig
import threading,os

class RegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'register'
    def ready(self):
        # Only start the bot if this is the main process, not the auto-reloader
        if os.environ.get('RUN_MAIN') == 'true':
            from .bot import run_bot
            threading.Thread(target=run_bot, daemon=True).start()