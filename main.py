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
    dp.add_handler(CommandHandler("links", lineuzinho.getGeneralRelevantLinks))
    dp.add_handler(CommandHandler("lives", lineuzinho.getLivesLinks))
    dp.add_handler(CommandHandler("repo", lineuzinho.getRepo))
    dp.add_handler(CommandHandler("contatinhos", lineuzinho.getContatinhosLink))
    dp.add_handler(CommandHandler("feijao", lineuzinho.getBeanFlavor))
    dp.add_handler(CommandHandler("docs", lineuzinho.getDocsChannel))
    dp.add_handler(CommandHandler("save", lineuzinho.saveMessage))
    dp.add_handler(CommandHandler("help", lineuzinho.getHelpText))
    dp.add_handler(CommandHandler("pi_rank", lineuzinho.getPiRanking))
    dp.add_handler(CommandHandler("pi_index", lineuzinho.publishUserPiRanking))
    dp.add_handler(CommandHandler("birthday", lineuzinho.getBirthdaySongAudio))
    dp.add_handler(CommandHandler("beni", lineuzinho.getBeniSongAudio))
    dp.add_handler(CommandHandler("grupos", lineuzinho.getSubjectsGroupsLinks))
    dp.add_handler(MessageHandler(Filters.text, lineuzinho.agiotar))

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, lineuzinho.greet))

    updater.start_polling()
    logging.info("=== Lineuzinho up&running! ===")
    updater.idle()
    logging.info("=== Lineuzinho shutting down :( ===")

if __name__ == "__main__":
    main()
