from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from lineuzinho import Lineuzinho

def main():
    logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO)

    lineuzinho = Lineuzinho()
    updater = Updater(lineuzinho.API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", lineuzinho.start))
    dp.add_handler(CommandHandler("links", lineuzinho.links))
    dp.add_handler(CommandHandler("lives", lineuzinho.lives))
    dp.add_handler(CommandHandler("repo", lineuzinho.getRepo))
    dp.add_handler(CommandHandler("contatinhos", lineuzinho.getContatinhos))
    dp.add_handler(CommandHandler("feijao", lineuzinho.getBeanFlavor))
    dp.add_handler(CommandHandler("docs", lineuzinho.getDocsChannel))
    dp.add_handler(CommandHandler("save", lineuzinho.save))
    dp.add_handler(CommandHandler("help", lineuzinho.help))
    dp.add_handler(CommandHandler("pi_rank", lineuzinho.getPiRanking))
    dp.add_handler(CommandHandler("pi_index", lineuzinho.generateUserPiRanking))
    dp.add_handler(CommandHandler("birthday", lineuzinho.birthday))
    dp.add_handler(MessageHandler(Filters.text, lineuzinho.agiotar))

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, lineuzinho.greet))

    updater.start_polling()
    logging.info("=== Lineuzinho up&running! ===")
    updater.idle()
    logging.info("=== Lineuzinho shutting down :( ===")

if __name__ == "__main__":
    main()
