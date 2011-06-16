#-*- coding:utf-8 -*-

import threading
import abc

try:
    import queue
except:
    import Queue as queue



class ok:
    pass



class error:
    pass



class NoReceive(Exception):
    pass



def noreceive():
    raise NoReceive()



class ActorBase(object):

    def __init__(self, supervisor=None):

        self.supervisor = supervisor

        self.__queue = queue.Queue()
        self.__sender = None


    def send(self, msg):

        self.__queue.put((current(), msg))


    def set_supervisor(self, sv):

        self.supervisor = sv


    def receive(self, func=lambda x:x):

        sender, msg = self.__queue.get()

        self.__sender = sender

        try:
            return func(msg)
        except NoReceive, e:
            self.__queue.put((sender, msg))


    def get_sender(self):
        return self.__sender



    def start_child(self, func):
        act = Actor(func, self)
        
        return act




class Actor(ActorBase, threading.Thread):
    

    def __init__(self, entry, supervisor=None, *argl, **argd):
        
        threading.Thread.__init__(self, *argl, **argd)
        ActorBase.__init__(self, supervisor)

        self.entry = entry

        self.setDaemon(True)

        self.start()


    def run(self):
            
        def sendto(code, msg):
            if self.supervisor:
                self.supervisor.send((code, msg))
        
        try:
            result = self.entry()
            sendto(ok, result)
        except Exception, reason:
            sendto(error, reason)
            raise



class MainActor(ActorBase):
    pass



MAIN_ACTOR = MainActor()


def current():

    cur = threading.current_thread()

    if isinstance(cur, threading._MainThread):
        return MAIN_ACTOR

    return cur



def sender():

    return current().get_sender()



def reply(msg):

    return sender().send(msg)



def receive(f=lambda x:x):

    return current().receive(f)



def start_child(f):

    return current().start_child(f)

