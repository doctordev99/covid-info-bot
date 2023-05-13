from telegram import Update
import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
from covid19 import Covid19

buttons = ReplyKeyboardMarkup([['Statistika'], ['Dunyo']], resize_keyboard=True)
async def start(update, context):
    await update.message.reply_text(
        'Salom {}'.format(update.effective_user.first_name), reply_markup=buttons)
    return 1
async def stats(update, context):

    await update.message.reply_html(
        '<b>Yuqtirganlar:</b> {}\n <b>Vafot etganlar:</b> {}\n'.format(
            "{:,}".format(253287),
            "{:,}".format(1637)
        ),
        reply_markup=buttons)

async def world(update, context):
    await update.message.reply_html(
        '<b>Yuqtirganlar:</b> {}\n <b>Vafot etganlar:</b> {}\n'.format(
            "{:,}".format(765903278),
            "{:,}".format(6927378)
        ),
        reply_markup=buttons)

app = ApplicationBuilder().token("6074371660:AAHmx9h7Cow8vZEfrbbtQuMcL-ccOoq_scc").build()


conv_handler = ConversationHandler(
    entry_points= [CommandHandler('Start', start)],
    states ={
        1:[
            MessageHandler(filters.Text(['Statistika']), stats),
            MessageHandler(filters.Text(['Dunyo']), world)
        ]
    },
    fallbacks= [MessageHandler(filters.TEXT, start)])

app.add_handler(conv_handler)

app.run_polling()