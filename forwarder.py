def saveToDocs(update, context):
    originalMessage = update.message.reply_to_message
    if not originalMessage:
        update.message.reply_text("faz o comando respondendo alguma coisa...")

    context.bot.forwardMessage("@docs21", update.effective_chat.id, originalMessage.message_id, disable_notification=True)