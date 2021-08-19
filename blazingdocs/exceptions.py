class BlazingException(Exception):
    def __init__(self, http_status_code: int, message: str):
        super(BlazingException, self).__init__(message)

        self.message: str = message
        self.status_code: int = http_status_code

    def __str__(self):
        message = "Message: %s. Status Code: %s" % (self.message, self.status_code)
        return message.strip()
