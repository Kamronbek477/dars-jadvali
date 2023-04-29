from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat.id
    btn1 = InlineKeyboardButton(text='Seshanba', callback_data="seshanba_data")
    btn2 = InlineKeyboardButton(text='chorshanba', callback_data="chorshanba_data")
    btn3 = InlineKeyboardButton(text='Payshanba', callback_data="payshanba_data")
    btn4 = InlineKeyboardButton(text='Juma', callback_data="juma_data")
    btn5 = InlineKeyboardButton(text='Shanba', callback_data="shanba_data")
    keyboard = InlineKeyboardMarkup([[btn1, btn2], [btn3, btn4], [btn5]])
    first_name = update.message.chat.first_name
    bot.sendMessage(chat_id, f"Assalomu alaykum {first_name}✋! Bizning botimizga xush kelipsiz.\nQuyidagi hafta kunlaridan kerakli tugmani bosing!👇", reply_markup=keyboard)
def menu(update: Update, context: CallbackContext):
    query = update.callback_query
    # chat_id = query.message.chat_id
    data = query.data
    bot = context.bot

    if data == "seshanba_data":
        btn = InlineKeyboardButton(text = "Ortga", callback_data="ortga_data")
        keyboard = InlineKeyboardMarkup([[btn]])
        query.edit_message_reply_markup(reply_markup=keyboard)
        query.edit_message_text(f'Seshanba kunidagi dars jadvali\n 4.Algaritmlarni loyihalash 📚(m). Djumayozov👨‍🏫. 313\n 5.Algaritmlarni loyihalash 📚(a). Djumayozov👨‍🏫. 305\n 6. TOQ hafta: Dasturiy injineringga kirish 📚(m) JUFT hafa: Algaritmlarni loyihalash 📚. 301. ', reply_markup=keyboard)
    elif data == "ortga_data":
        btn1 = InlineKeyboardButton(text='Seshanba🗓', callback_data="seshanba_data")
        btn2 = InlineKeyboardButton(text='chorshanba🗓', callback_data="chorshanba_data")
        btn3 = InlineKeyboardButton(text='Payshanba🗓', callback_data="payshanba_data")
        btn4 = InlineKeyboardButton(text='Juma🗓', callback_data="juma_data")
        btn5 = InlineKeyboardButton(text='Shanba🗓', callback_data="shanba_data")
        keyboard = InlineKeyboardMarkup([[btn1, btn2], [btn3, btn4], [btn5]])
        
        query.edit_message_reply_markup(reply_markup=keyboard)
        query.edit_message_text(" Quyidagi hafta kunlaridan kerakli tugmani bosing!", reply_markup=keyboard)
    elif data == "chorshanba_data":
        btn = InlineKeyboardButton(text = "Ortga", callback_data="ortga_data")
        keyboard = InlineKeyboardMarkup([[btn]])
        query.edit_message_reply_markup(reply_markup=keyboard)
        query.edit_message_text(f'Chorshanba kunidagi dars jadvali\n 3.11-30da Diskret tuzilmalar📚(a). Quchqorov👨‍🏫. 202\n 4.Dasturiy injineringga kirish 📚(a). Goziyev👨‍🏫. 307 \n 5. Web dasturlashga kirish📚. Shokirov👨‍🏫. 314.', reply_markup=keyboard)
    elif data == "payshanba_data":
        btn = InlineKeyboardButton(text = "Ortga", callback_data="ortga_data")
        keyboard = InlineKeyboardMarkup([[btn]])
        query.edit_message_reply_markup(reply_markup=keyboard)
        query.edit_message_text(f'Payshanba kunidagi dars jadvali\n 4. Kompyuterni tashkil etish  📚(m). Sattorov👨‍🏫. 307\n 5.Kompyuterni tashkil etish 📚(a). Sattorov👨‍🏫. 202. \n 6. Dasturiy injineringga kirish 📚(m). Qayumov👨‍🏫. 301.', reply_markup=keyboard)    
        
    elif data == "juma_data":
        btn = InlineKeyboardButton(text = "Ortga", callback_data="ortga_data")
        keyboard = InlineKeyboardMarkup([[btn]])
        query.edit_message_reply_markup(reply_markup=keyboard)
        query.edit_message_text(f'Juma kunidagi dars jadvali\n 4.Diskret tuzilmalar 📚(m). Abdullayeva👩‍🏫 301.\n 5.Diskret tuzilmalar 📚(m). Abdullayeva👩‍🏫. 317. ', reply_markup=keyboard)
    elif data == "shanba_data":
        btn = InlineKeyboardButton(text = "Ortga", callback_data="ortga_data")
        keyboard = InlineKeyboardMarkup([[btn]])
        query.edit_message_reply_markup(reply_markup=keyboard)
        query.edit_message_text(f'Shanba kunidagi dars jadvali\n 1.Web dasturlashga kirish 📚(m). Djumayev👨‍🏫. 207.\n 3.Toq hafta: Web dasturlashga kirish 📚(m). Djumayev👨‍🏫 317 ', reply_markup=keyboard)
# def text(update: Update, context: CallbackContext):
    


