from .services import generate_message, send_telegram_message_to_admin


class ErrformerMiddleware:
    def __init__(self, get_response):
        """
        Initialize middleware.
        get_response — is the next middleware or view that will process the request.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        This method is called for each request.
        """
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        """
        This method is called if an exception occurs during request processing.
        """

        error_message = generate_message(request, exception)
        send_telegram_message_to_admin(error_message)
