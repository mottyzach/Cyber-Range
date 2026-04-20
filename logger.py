class Logger:
    def __init__(self, gui_log_callback):
        self.log_callback = gui_log_callback
        self.history = []

    def log(self, message):
        self.history.append(message)
        if self.log_callback:
            self.log_callback(message)