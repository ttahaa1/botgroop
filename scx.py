# ⤷ Dev by : @J_A_C_K_9
import telebot
from telebot import types
import random
bot = telebot.TeleBot("7089038343:AAFAQhRICHA0DbD7Lu3FbdfuQ2Shq0G_fDs") 

donkey = []
mute = []
lista = [

"من هو مطور الواجهة الأمامية ؟",

"ما هي بايثون ؟",

"هل بتكراش ع حد في حياتك ؟",

"ممكن توريني صوره بتحبها ؟",

"عندك كام اكس في حياتك ؟",

"قولي علي اكبر غلطه ندمان عليها ؟",

"عامل بلوك لكام واحد عندك ولي ؟",

"لونك المفضل اي ؟",

"أجمل شيء حصل معاك في هذا اليوم ؟ ",

"سؤال ينرفزك ؟ ",

"اكثر ممثل تحبه ؟ ",

"اي رايك في مصر  ؟ ",

"كم مره حبيت ؟ ",

"أكثر حيوان تخاف منه ؟ ",

"أكثر حاجه عايز تغيرها في نفسك ؟ ",

"اي رايك في الدنيا دي ؟ ",

"ما هو أفضل حافز لك ؟ ",

"ما الذي يشغل بالك في الفترة الحالية ؟",

"شاركني صورة احترافية من تصويرك ؟ ",

"كتاب أو رواية تقرأها هذه الأيام ؟ ",

"شعورك الحالي في جملة ؟ ",

"كلمة لشخص بعيد ؟ ",

"موقف غير حياتك ؟ ",

"اكثر مشروب تحبه ؟ ", 

"ما هو أول شخص يدخل باب الجنة ؟ ",

"لماذا خلقنا الله تعالى ؟",

"لما أرسل الله على عباده الرسل ؟",

"ماذا تعني جملة لا إله إلا الله ؟",

"من هو أول الخلق ؟",

"ما هو أول مسجد تم افتتاحه ؟",

"تاريخ ميلادك ؟ ",

"قهوه و لا شاي ؟ ",

"كم عدد الرسل الذي أرسلهم الله لينشروا الإسلام ؟",

"ما القواعد الرئيسية لرياضة كمال الأجسام ؟",

"من محبّين الليل أو الصبح ؟ ",

"حيوانك المفضل ؟ ",

"هل تحب مطوري جاك ؟",
]

@bot.message_handler(commands=['users'])
def user_bot(message):
    file = open('userss.txt','r')
    count = len(file.readlines())
    bot.send_message(message.chat.id, f"عدد مستخدمين البوت : {count}")

def ex_id(id):
    result = False
    file = open('userss.txt','r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

# ⤷ Dev by : @GNA_I

@bot.message_handler(commands=['orders'])
def order(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"""<strong>
اوامر الحماية :
                      
-------------------------------------------------
استخدم امر "طرد" لطرد العضو من المجموعة

استخدم امر "الحظر" ل حظر العضو من المجموعة            
                     
استخدم امر "الغاء الحظر" ل الغاء حظر العضو من المجموعة                  
                     
استخدم امر "كتم" لكتم العضو من المجموعة

استخدم امر "الغاء الكتم" ل الغاء كتم العضو من المجموعة                                 

-------------------------------------------------

الالعاب التي موجودة بالبوت : 
                     
-------------------------------------------------
                     
1 - لعبة بولينغ
                     
2 - لعبة كرة القدم
                     
3 - لعبة كرة سلة
                     
4 - لعبة قمار
                     
5 - لعبة تصويب
                     
6 - لعبه اسئله
                     
-------------------------------------------------
</strong>""", parse_mode='html', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['start'])
def start(message):
    comm = types.InlineKeyboardMarkup(row_width=1)
    private = types.InlineKeyboardButton(url='https://t.me/J_A_C_K_9', text='Developer 🧑‍💻') 
    chaanel = types.InlineKeyboardButton(url='https://t.me/J_A_C_K_T_E_A_M', text='Chaanel Developer 🧑‍💻')
    comm.add(private,chaanel)
    m = message.chat.id
    if message.chat.type == 'private':
        idu = message.from_user.id
        f = open('userss.txt', 'a')
        if (not ex_id(str(idu))):
            f.write("{}\n".format(idu))
            f.close()
            name = message.from_user.first_name
            user = message.from_user.username
            ph = f'https://t.me/{user}'
            bot.send_photo(m, ph, f"""            
ارفعني ادمن وسيب الباقي عليا                      
                       
ارسل امر /users : لمعرفة عدد مستخدمين البوت
                       
ارسل امر /orders : لمعرفة اوامر البوت
                       
""", parse_mode='Markdown', reply_to_message_id=message.message_id, reply_markup=comm)
        else:
            name = message.from_user.first_name
            user = message.from_user.username
            ph = f'https://t.me/{user}'
            bot.send_photo(m, ph, f"""   
ارفعني ادمن وسيب الباقي عليا                      
                       
ارسل امر /users : لمعرفة عدد مستخدمين البوت
                       
ارسل امر /orders : لمعرفة اوامر البوت
                         
                        """, parse_mode='Markdown', reply_to_message_id=message.message_id, reply_markup=comm)
    else:
        username = message.from_user.username
        ph = f'https://t.me/{username}'
        bot.send_photo(m, ph, f""" 
ارفعني ادمن وسيب الباقي عليا                      
                       
ارسل امر /users : لمعرفة عدد مستخدمين البوت
                       
ارسل امر /orders : لمعرفة اوامر البوت
                       
                                """, parse_mode='Markdown', reply_to_message_id=message.message_id, reply_markup=comm)

# ⤷ Dev by : @GNA_I

@bot.message_handler(func=lambda message:True)
def boting(message):
    chat_id = message.chat.id
    adcon = ['creator', 'administrator']
    messag = message.text
    if messag =='طرد':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.reply_to_message.from_user.first_name
            bot.kick_chat_member(chat_id, message.reply_to_message.from_user.id)
            user = message.reply_to_message.from_user.username
            idd = message.reply_to_message.from_user.id
            id_user = str('-> @' + str(user) + ' - ' + '( <code>' + str(idd) + '</code> )')
            open(f'{chat_id}-kick.txt', 'a').write(f'{id_user}\n')
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
تم طرده من المجموعة .
''', parse_mode='markdown', disable_web_page_preview=True, reply_to_message_id=message.message_id)
        else:
            bot.send_message(chat_id, 'هذا الامر يخص الادمن او المالك .', reply_to_message_id=message.message_id)
    if messag =='المطرودين':
        kicks = open(f'{chat_id}-kick.txt','r').read()
        bot.send_message(chat_id, f'''
ملاحضة : لا يمكنك التعديل على هذه القائمة لانها تشمل كل الاعضاء الذي تم طردهم من المجموعة

{kicks}             

''', reply_to_message_id=message.message_id, parse_mode='html')
    if messag == 'كتم':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.json['reply_to_message']['from']['first_name']
            username = message.json['reply_to_message']['from']['username']
            id = message.json['reply_to_message']['from']['id']
            if id in mute:
                bot.reply_to(message, f'''**
العضو : [{name}](t.me/{username})
مكتوم سابقا .
            **''', parse_mode='markdown', disable_web_page_preview=True)
            else:
                name = message.json['reply_to_message']['from']['first_name']
                username = message.json['reply_to_message']['from']['username']
                id = message.json['reply_to_message']['from']['id']
                mute.append(id)
                user = message.reply_to_message.from_user.username
                idd = message.reply_to_message.from_user.id
                id_user = str('-> @' + str(user) + ' - ' + '( <code>' + str(idd) + '</code> )')
                open(f'{chat_id}-mute.txt', 'a').write(f'{id_user}\n')
                bot.reply_to(message, f'''**
العضو : [{name}](t.me/{username})
تم كتمه في المجموعة .
                        **''', parse_mode='markdown', disable_web_page_preview=True)
                print(mute)
        else:
            bot.reply_to(message, '<strong>هذا الامر يخص الادمن او المالك</strong>', parse_mode='html')

    if message.json['from']['id'] in mute:
        bot.delete_message(message.chat.id, message_id=message.message_id)
    if messag == 'الغاء الكتم':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.json['reply_to_message']['from']['first_name']
            username = message.json['reply_to_message']['from']['username']
            id = message.json['reply_to_message']['from']['id']
            mute.remove(id)
            bot.reply_to(message, f'''**
العضو : [{name}](t.me/{username})
تم الغاء كتمه في المجموعة .
                    **''', parse_mode='markdown', disable_web_page_preview=True)
            print(mute)
        else:
            bot.reply_to(message, '<strong>هذا الامر يخص الادمن او المالك</strong>', parse_mode='html')
    if messag=="المكتومين":
        mutes = open(f'{chat_id}-mute.txt','r').read()
        bot.send_message(chat_id, f'''
ملاحضة : لا يمكنك التعديل على هذه القائمة لانها تشمل كل الاعضاء الذي تم كتمهم في المجموعة

{mutes}             

''', reply_to_message_id=message.message_id, parse_mode='html')
    if messag=='حظر':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.reply_to_message.from_user.first_name
            bot.ban_chat_member(chat_id, message.reply_to_message.from_user.id)
            user = message.reply_to_message.from_user.username
            idd = message.reply_to_message.from_user.id
            id_user = str('-> @' + str(user) + ' - ' + '( <code>' + str(idd) + '</code> )')
            open(f'{chat_id}-ban.txt', 'a').write(f'{id_user}\n')
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
تم حظره من المجموعة .
        ''', parse_mode='markdown', disable_web_page_preview=True, reply_to_message_id=message.message_id)
        else:
            bot.send_message(chat_id, 'هذا الامر يخص الادمن او المالك .', reply_to_message_id=message.message_id)
    if message=='الغاء الحظر':
        if bot.get_chat_member(chat_id, message.from_user.id).status in adcon:
            name = message.reply_to_message.from_user.first_name
            bot.unban_chat_member(chat_id, message.reply_to_message.from_user.id)
            user = message.reply_to_message.from_user.username
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
تم الغاء حظره من المجموعة .
''', parse_mode='markdown', disable_web_page_preview=True, reply_to_message_id=message.message_id)
        else:
            bot.send_message(chat_id, 'هذا الامر يخص الادمن او المالك .', reply_to_message_id=message.message_id)
    if messag=='المحظورين':
        bans = open(f'{chat_id}-ban.txt', 'r').read()
        bot.send_message(chat_id, f'''
ملاحضة : لا يمكنك التعديل على هذه القائمة لانها تشمل كل الاعضاء الذي تم حظرهم في المجموعة

{bans}             

''', reply_to_message_id=message.message_id, parse_mode='html')
    if messag=='اسئله':
        bot.send_message(chat_id, f'<strong>{random.choice(lista)}</strong>', parse_mode='html', reply_to_message_id=message.message_id)

    if messag =='رفع حمار'  :
        user = message.reply_to_message.from_user.username
        name = message.reply_to_message.from_user.first_name
        idd = message.reply_to_message.from_user.id
        id_user = str('-> @' + str(user) + ' - ' + '( <code>' + str(idd) + '</code> )')
        open(f'{chat_id}-donkey.txt', 'a').write(f'{id_user}\n')
        donkey.append(idd)
        bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
رفعته حمار في المجموعة .
''', parse_mode='markdown', reply_to_message_id=message.message_id)
    if messag=='تنزيل حمار' :
        if message.reply_to_message.from_user.id in donkey:
            user = message.reply_to_message.from_user.username
            name = message.reply_to_message.from_user.first_name
            donkey.remove(message.reply_to_message.from_user.id)
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
نزلته من قائمة الحمير في المجموعة .
''', parse_mode='markdown', reply_to_message_id=message.message_id)
        else:
            user = message.reply_to_message.from_user.username
            name = message.reply_to_message.from_user.first_name
            bot.send_message(chat_id, f'''
المستخدم : [{name}](t.me/{user})
ليس حمار في المجموعة .
''', parse_mode='markdown', reply_to_message_id=message.message_id)
    if messag=='الحمير':
        donkeys = open(f'{chat_id}-donkey.txt', 'r').read()
        bot.send_message(chat_id, f'''
{donkeys}
''', parse_mode='html', reply_to_message_id=message.message_id)
    if messag=='بولينغ':
        bot.send_dice(chat_id, emoji='🎳', disable_notification=True)
    if messag=='تصويب':
        bot.send_dice(chat_id, emoji='🎯', disable_notification=True)
    if messag=='كرة قدم':
        bot.send_dice(chat_id, emoji='⚽', disable_notification=True)
    if messag=='قمار':
        bot.send_dice(chat_id, emoji='🎰', disable_notification=True)
    if messag=='كرة سلة':
        bot.send_dice(chat_id, emoji='🏀', disable_notification=True)
@bot.message_handler(content_types=['left_chat_member'])
def dele(message):
    bot.delete_message(message.chat.id, message_id=message.message_id)
bot.infinity_polling()
# ⤷ Dev by : @GNA_I
