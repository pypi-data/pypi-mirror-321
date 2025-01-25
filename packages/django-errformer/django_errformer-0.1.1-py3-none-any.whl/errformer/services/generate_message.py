import traceback

from django.conf import settings


INCLUDE_TRACEBACK = getattr(settings, "ERRFORMER_INCLUDE_TRACEBACK", False)
PROJECT_NAME = getattr(settings, "ERRFORMER_PROJECT_NAME")


def generate_message(request, exception) -> str:
    """
    Generate error message.
    """
    error_message = f"We have an error\n\n"
    if PROJECT_NAME:
        error_message += f"Project: {PROJECT_NAME}\n\n"

    error_message += (
        f"URL: {request.build_absolute_uri()}\n"
        f"Method: {request.method}\n"
        f"User: {request.user}\n"
        f"Error: <code>{exception}</code>\n\n"
    )

    if INCLUDE_TRACEBACK:
        error_message += f"Traceback:\n<pre><code>{traceback.format_exc()}</code></pre>"

    return error_message


def wrap_message_with_project_details(message: str) -> str:
    """
    Wrap message with project name.
    """
    wrapped_message = ""
    if PROJECT_NAME:
        wrapped_message += f"Project: {PROJECT_NAME}\n\n"
    wrapped_message += message
    return wrapped_message
