#-*- coding:utf-8 -*-

import sys

from scalalike.actors import actor


def output(msg):

    print >> sys.stderr,  actor.sender(), msg



def test_actor():

    def func():

        print >> sys.stderr, actor.current()


    act = actor.Actor(func)

    act.join()



def test_msg():

    def receiver():

        act = actor.current()
        act.receive(output)


    act = actor.Actor(receiver)

    act.send('hello, actor')

    act.join()



def test_reply():


    def replyto(msg):

        output('message comming')

        actor.reply(msg)


    def receiver():

        cur = actor.current()
        cur.receive(replyto)


    def sender():

        cur = actor.current()
        act.send('helllo')
        msg = cur.receive()
        output('reply comming')
        output(msg)


    act = actor.Actor(receiver)
    act2 = actor.Actor(sender)

    act.join()
    act2.join()



def test_supervisor():

    def supervisor():

        cur = actor.current()

        output(cur)

        output(cur.receive())
        output(cur.receive())


    def erroractor():

        x = 10 / 0

        
    def normalactor():

        return 'Success'


    er = actor.start_child(erroractor)
    nm = actor.Actor(normalactor, actor.current())

    supervisor()




def test_noreceive():


    def receiver():

        cur = actor.current()
        # noreceive が呼ばれるとキューの最後に回される
        cur.receive(lambda x:actor.noreceive())
        output(cur.receive())


    ac = actor.Actor(receiver)
    ac.send('hello, erlang')

    ac.join()



def test_selfmsg():

    cur = actor.current()

    cur.send('self messaging')
    output(cur.receive())


