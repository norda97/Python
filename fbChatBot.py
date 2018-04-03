from fbchat import Client, log
from fbchat.models import *




class Jarvis(Client):
    first = True
    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        self.markAsRead(author_id)

        # Print info on console
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))

        # Message Text
        msgText = message_object.text

         # Send message
        if author_id!=self.uid:
            self.send(Message(text=msgText), thread_id=thread_id, thread_type=thread_type)

        # Mark message as delivered
        self.markAsDelivered(author_id, thread_id)


client = Jarvis("adrian-nordin@hotmail.com", "adrian123")
client.listen()
