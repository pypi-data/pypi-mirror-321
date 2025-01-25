import logging

from ..services import send_telegram_message_to_admin, wrap_message_with_project_details


class TelegramErrformerHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        wrapped_message = wrap_message_with_project_details(log_entry)
        send_telegram_message_to_admin(wrapped_message)
