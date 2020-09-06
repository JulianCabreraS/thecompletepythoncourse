"""
Multiline comments

    """


class MyCustomError(TypeError):

    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')

