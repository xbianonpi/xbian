import threading

class Updater(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._stopevent = threading.Event( )
        self.queue = queue
        
    def run(self):
        while not self._stopevent.isSet():
            setting = self.queue.get()
            if setting != "stop" :
				setting[0].ThreadSetXbianValue(setting[1])
				setting[0].updatingSetting = False
            
            
    def stop(self):
        self._stopevent.set()
        self.queue.put("stop")
         
