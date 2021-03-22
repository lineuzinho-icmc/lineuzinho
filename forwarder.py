class Forwarder:
    def __init__(self):
        self.docsChannel = "@docs21"

    def saveToDocs(self, update, context):
        originalMessage = update.message.reply_to_message
        if not originalMessage:
            update.message.reply_text("faz o comando respondendo alguma coisa...")

        context.bot.forwardMessage(self.docsChannel, update.effective_chat.id, originalMessage.message_id, disable_notification=True)