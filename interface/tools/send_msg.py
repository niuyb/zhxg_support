"""
    发送消息的类，不仅限于企业微信
"""

from interface.tools.WecomtalkApi import WecomApi

class MsgSender(object):

    def send(self, msg):
        pass


class WecomMsgSender(MsgSender):

    def send(self, msg):
        WecomApi().sendMsg(wecomId="10290", msg=msg)
        print('wecom:' + msg)


class DingMsgSender(MsgSender):

    def send(self, msg):
        print('ding:' + msg)


class MsgSenderFactory:

    def __init__(self):
        pass

    @staticmethod
    def create():
        if sender_type == 'wecom':
            return WecomMsgSender()
        else:
            return DingMsgSender()


sender_type = 'wecom'


if __name__ == '__main__':
    ms = MsgSenderFactory.create()
    ms.send("ok!")








