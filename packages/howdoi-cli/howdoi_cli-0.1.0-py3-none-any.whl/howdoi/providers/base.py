class BaseProvider:
    def __init__(self, config):
        self.config = config

    def get_command(self, query, shell):
        raise NotImplementedError
