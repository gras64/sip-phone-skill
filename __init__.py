from mycroft import MycroftSkill, intent_file_handler
from pyrogram import Client
from tgvoip_pyrogram import VoIPFileStreamService, VoIPIncomingFileStreamCall

class SipPhone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('phone.sip.intent')
    def handle_phone_sip(self, message):
        self.speak_dialog('phone.sip')


def create_skill():
    return SipPhone()

