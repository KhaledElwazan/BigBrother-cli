import threading
from json.encoder import JSONEncoder
import threading

class Mother(JSONEncoder):
    def toJSON(self):
        return self.__dict__
    def run_in_background(self):
        thread = threading.Thread(target=self.publish)
        thread.daemon = True                            # Daemonize thread
        thread.start() 
        return thread    