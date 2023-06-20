import sqlite3

from aiogram import types
from aiogram.types import InputFile, ContentType

from data.config import ADMINS
from handlers.users import show_on_gmaps
from loader import dp,db,bot
from aiogram.dispatcher import FSMContext
from keyboards.default.keyboards import menu_uzb, bosh_menu_keyboard_uzb, kombo_uzb, kombo_3_5, salatlar_uzb_, sonlar, \
   shashliklar_uzb, ikkinchi_taomlar_uzb, birinchi_taomlar_uzb, ichimliklar_uzb, nonlar_uzb, location_uzb, number_uzb, \
   izoh_uzb, last_things, savat_uzb, type_uzb, antiqa_sonlar_uzb
from states.statess import uzb_menu_state
from utils.misc.get_distance import calc_distance


###BOSH BUYRUQLAR
@dp.message_handler(text="🍴 Menyu")
async def bosh_menu(message:types.Message):
   await message.answer("Bo`limlardan birini tanlang:",reply_markup=menu_uzb)

@dp.message_handler(text="⬅️ Ortga")
async def bosh_menuga(message:types.Message):
   await message.answer("Menulardan birini tanlang 👇",reply_markup=bosh_menu_keyboard_uzb)

@dp.message_handler(content_types=ContentType.PHOTO)
async def photo(message:types.Message):
   await message.answer(message.photo[-1].file_id)

###SAVAT
@dp.message_handler(text="🛒 Savat")
async def savat(message:types.Message):
   a = db.savatni_tekshir(message.from_user.id)
   if not a:
      await message.answer("Savatingiz bo`m bo`sh!")
   else:
      await message.answer(a,reply_markup=savat_uzb)
      await uzb_menu_state.savat_main.set()

@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.cola05)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.cola1)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.cola15)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.pepsi05)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.pepsi1)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.pepsi15)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.suv05)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.suv1)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.suv15)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.bliss)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.chortoq)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.turetiskiy)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.qatlama)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.svejiy_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.sezer_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.smak_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.oliviya_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.muskoy_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.gurman_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.grecheski_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.fransuzki_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.gijduvon_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.chiroqchi_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.achichuv_salat)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.tovuq_file)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.qoy_jaz)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.qiyma)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.pomidor)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.moljaz)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.krilishka)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.bonfile)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.baranni)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.qaynatma)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.mastava)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.pelmen)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.balaza)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.gijduvon_jiz)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.vaguri)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.afgan_jiz)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.olot_somsa)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.sudak_file)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.semichka)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.vaguri_spes)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.combo3)
@dp.message_handler(text="🛒 Savat",state=uzb_menu_state.combo5)
async def savat(message:types.Message):
   a = db.savatni_tekshir(message.from_user.id)
   if not a:
      await message.answer("Savatingiz bo`m bo`sh!")
   else:
      await message.answer(a)

@dp.message_handler(text="◀️ Qaytish",state=uzb_menu_state.savat_main)
async def savatdanortga(message:types.Message,state:FSMContext):
   await message.answer("Yana boshqa narsa olasizmi?",reply_markup=menu_uzb)
   await state.finish()

@dp.message_handler(text="♻️ Tozalash", state=uzb_menu_state.savat_main)
async def tozalarsavatni(message:types.Message,state:FSMContext):
   db.clearproducts(mahsulot=None,id=message.from_user.id)
   await message.answer("🛒 Savat tozalandi")
   await message.answer("Nimadan boshlaymiz?",reply_markup=menu_uzb)
   await state.finish()


###Buyurtma sari
@dp.message_handler(text="🚗 Buyurtma qilish")
async def buyurtmaSari(message:types.Message):
   tekshir = db.savatni_tekshir(message.from_user.id)
   if not tekshir:
      await message.answer("<b>Savatingiz bo'm bo'sh.</b>\n"
                           "Buyurtma qilishdan oldin olmoqchi bo`lgan mahsulotlaringizni tanlang!")
   else:
      await message.answer("Buyurtmani yetkazib berishimiz uchun manzilingizni jo'nating \n"
                           "(📍 Turgan joyimni jo'natish. tugmasini bosing)",reply_markup=location_uzb)
      await uzb_menu_state.location.set()

@dp.message_handler(text="◀️ Ortga",state=uzb_menu_state.location)
async def ackgo(message:types.Message,state:FSMContext):
   await message.answer("Yana boshqa narsa olasizmi?",reply_markup=menu_uzb)
   await state.finish()

#
# @dp.message_handler(content_types=ContentType.TEXT,state=uzb_menu_state.location)
# async def back(msg:types.Message):
#     try:
#         db.addlocation(id=msg.from_user.id, location=msg.text)
#     except sqlite3.IntegrityError as err:
#         await bot.send_message(chat_id=ADMINS[0], text=err)
#     await msg.answer("📲 Raqamingizni ulashing:\n"
#                      "('Ulashish 📲' tugmasini bosing:)\n"
#                      "Yoki '+998901234567' ko`rinishida yuboring!", reply_markup=number_uzb)
#     await uzb_menu_state.contact.set()

@dp.message_handler(content_types=types.ContentType.LOCATION,state=uzb_menu_state.location)
async def locat(msg:types.Message):
   location = msg.location
   latitude = location.latitude
   longitude = location.longitude
   distanse = calc_distance(latitude,longitude)
   a = (float(str(distanse).split(".")[0])*2000)
   db.add_delivery(a,msg.from_user.id)

   jonat = db.tekshir(msg.from_user.id)
   jonat+=f"Eltib berish xizmati: {a} so'm"
   db.add_new_product(jonat,msg.from_user.id)
   await msg.answer(f"Yo`lkira haqi taxminan: {a} so`m\n"
                    f"<b>Ushbu narx o'zarishi mumkin!!!</b>")
   locationn=""
   locationn+=str(latitude)
   locationn+="|"
   locationn+=str(longitude)
   try:
      db.addlocation(id=msg.from_user.id,location=locationn)
   except sqlite3.IntegrityError as err:
      await bot.send_message(chat_id=ADMINS[0], text= err)
   await msg.answer("📲 Raqamingizni ulashing:\n"
                     "('Ulashish 📲' tugmasini bosing:)\n"
                     "Yoki '+998901234567' ko`rinishida yuboring!",reply_markup=number_uzb)
   await uzb_menu_state.contact.set()



###contact
@dp.message_handler(text="◀️ Ortga",state=uzb_menu_state.contact)
async def something(message:types.Message):
   await message.answer("Buyurtmani yetkazib berishimiz uchun manzilni kiriting, yoki turgan joyingizni jo'nating \n"
                        "(📍 Turgan joyimni jo'natish. tugmasini bosing)",reply_markup=location_uzb)
   await uzb_menu_state.location.set()

@dp.message_handler(content_types=types.ContentType.TEXT,state=uzb_menu_state.contact)
async def contact(msg:types.Message):
    if 13>=len(msg.text)>=9:
        if msg.text[0]=='+' and len(msg.text)==13 and msg.text[:4]=='+998':
            try:
                db.add_phone(id=msg.from_user.id, number=msg.text)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
            await msg.answer("Buyurtma uchun izoh 📝\n\n"
                             "Buyurtmaga aloqador bo'lgan qo'shimcha tafsilot, yoki operatorlarimiz bog'lanishlari uchun qo'shimcha telefon raqamingizni "
                             "📱 izohda yozib qoldirishingiz mumkin",reply_markup=izoh_uzb)
            await uzb_menu_state.izoh.set()
        elif len(msg.text)==9:
            try:
                db.add_phone(id=msg.from_user.id, number=msg.text)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
            await msg.answer("Buyurtma uchun izoh 📝\n\n"
                             "Buyurtmaga aloqador bo'lgan qo'shimcha tafsilot, yoki operatorlarimiz bog'lanishlari uchun qo'shimcha telefon raqamingizni "
                             "📱 izohda yozib qoldirishingiz mumkin", reply_markup=izoh_uzb)
            await uzb_menu_state.izoh.set()
    else:
        await msg.answer("Qaytadan urunib ko`ring!")



@dp.message_handler(content_types=types.ContentType.CONTACT,state=uzb_menu_state.contact)
async def contact(msg:types.Message):
    try:
        db.add_phone(id=msg.from_user.id,number=msg.contact.phone_number)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text= err)
    await msg.answer("Buyurtma uchun izoh 📝\n\n"
                     "Buyurtmaga aloqador bo'lgan qo'shimcha tafsilot, yoki operatorlarimiz bog'lanishlari uchun qo'shimcha telefon raqamingizni "
                     "📱 izohda yozib qoldirishingiz mumkin", reply_markup=izoh_uzb)
    await uzb_menu_state.izoh.set()


#izoh
@dp.message_handler(text="◀️ Ortga",state=uzb_menu_state.izoh)
async def something(message:types.Message):
   await message.answer("📲 Raqamingizni ulashing:\n"
                    "('Ulashish 📲' tugmasini bosing:)\n"
                    "Yoki '+998901234567' ko`rinishida yuboring!", reply_markup=number_uzb)
   await uzb_menu_state.contact.set()


@dp.message_handler(content_types=types.ContentType.TEXT,state=uzb_menu_state.izoh)
async def izof(message:types.Message):
   try:
      db.add_izoh(izoh=message.text,id=message.from_user.id)
   except sqlite3.IntegrityError as err:
      await bot.send_message(chat_id=ADMINS[0],text=err)

   await message.answer("Buyurtma yetkazib berilsinmi yoki olib ketasizmi?",reply_markup=type_uzb)
   await uzb_menu_state.type.set()


@dp.message_handler(text="◀️ Ortga",state=uzb_menu_state.type)
async def something(message:types.Message):
   await message.answer("Buyurtma uchun izoh 📝\n\n"
                     "Buyurtmaga aloqador bo'lgan qo'shimcha tafsilot, yoki operatorlarimiz bog'lanishlari uchun qo'shimcha telefon raqamingizni "
                     "📱 izohda yozib qoldirishingiz mumkin", reply_markup=izoh_uzb)
   await uzb_menu_state.izoh.set()

@dp.message_handler(text="Yetkazib berilsin",state=uzb_menu_state.type)
async def contact(msg:types.Message):
    try:
        db.add_type(id=msg.from_user.id,type=msg.text)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text= err)

    eski_narx = float(db.narx_tekshir(msg.from_user.id))
    eski_narx += float(db.get_delivery(msg.from_user.id))
    db.add_narx(eski_narx,msg.from_user.id)
    await msg.answer(
       "🧾 Buyurtmangizni tekshiring. Hamma narsa joyida bo'lsa \n'🚗 Buyurtma qilish' tugmasini bosing.")
    xabar = str()
    user = list(db.select_user(id=msg.from_user.id))
    xabar += f"<b>Xizmat turi:</b> {user[-2]}\n" \
             f"<b>Savat 🛒:</b> \n\n" \
             f"{user[4]}\n\n" \
             f"<b>Izoh:</b> {user[3]} \n" \
             f"<b>Umumiy narx 💲:</b> {user[-1]}so`m \n"

    await msg.answer(xabar, reply_markup=last_things)
    await uzb_menu_state.last_thing.set()

@dp.message_handler(text="O`zim olib ketaman",state=uzb_menu_state.type)
async def contact(msg:types.Message):
    try:
        db.add_type(id=msg.from_user.id,type=msg.text)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text= err)

    await msg.answer("🧾 Buyurtmangizni tekshiring. Hamma narsa joyida bo'lsa \n'🚗 Buyurtma qilish' tugmasini bosing.")
    xabar = str()
    user = list(db.select_user(id=msg.from_user.id))
    savatt = user[4].split("\n")
    savatt.pop(-1)
    sava = ''
    for a in savatt:
       sava+=a
       sava+="\n"

    xabar+=f"<b>Xizmat turi:</b> {user[-2]}\n" \
           f"<b>Savat 🛒:</b> \n\n" \
           f"{sava}\n" \
           f"<b>Izoh:</b> {user[3]} \n" \
           f"<b>Umumiy narx 💲:</b> {user[-1]}so`m \n"

    await msg.answer(xabar,reply_markup=last_things)
    await uzb_menu_state.last_thing.set()

###LAST THINGS 
@dp.message_handler(text="🚗 Buyurtma qilish",state=uzb_menu_state.last_thing)
async def lastone(message:types.Message,state:FSMContext):
   xabar = str()
   user = list(db.select_user(id=message.from_user.id))
   await message.answer("Buyurtmangiz qabul qilindi! Tez orada adminlar sizga bog`lanishadi.",reply_markup=bosh_menu_keyboard_uzb)
   xabar += f"Mijoz raqami: {user[5]}\n" \
            f"Mijozning telegrami: @{message.from_user.username}\n" \
            f"<b>Xizmat turi:</b> {user[-2]}\n" \
            f"Savat 🛒:\n\n" \
            f"{user[4]}\n\n" \
            f"Izoh: {user[3]}\n" \
            f"Umumiy narx 💲: {user[-1]} so`m\n"
   prepare = db.select_user(id=message.from_user.id)
   preprepare = prepare[2].split("|")

   await bot.send_message(text=xabar,chat_id="@gijduvon_zakaz_bot")
   await bot.send_location("-1001434053000",preprepare[0],preprepare[1])
   db.clearproducts(mahsulot=None,id=message.from_user.id)
   db.clearnarx(narx=None,id=message.from_user.id)
   await state.finish()

# @dp.message_handler(text="sayyohaka")
# async def aaa(message:types.Message):
#    prepare = db.select_user(id=message.from_user.id)
#    preprepare = prepare[2].split("|")
#    await message.answer_location(preprepare[0],preprepare[1])
#
@dp.message_handler(text="📝 O`zgartirish", state=uzb_menu_state.last_thing)
async def ozgartir(message:types.Message,state:FSMContext):
   await message.answer("Yana boshqa narsa olasizmi?",reply_markup=menu_uzb)
   await state.finish()

@dp.message_handler(text="❌ Bekor qilish",state=uzb_menu_state.last_thing)
async def bekorqi(message:types.Message,state:FSMContext):
   db.clearproducts(mahsulot=None, id=message.from_user.id)
   db.clearnarx(narx=None, id=message.from_user.id)
   await message.answer("Buyurtma beramizmi? ☺️",reply_markup=bosh_menu_keyboard_uzb)
   await state.finish()

@dp.message_handler(text="◀️ Ortga",state=uzb_menu_state.last_thing)
async def backcc(messagre:types.Message):
   type = db.get_type(messagre.from_user.id)
   if type == "Yetkazib berilsin":
      delivery_cost = float(db.get_delivery(messagre.from_user.id))
      narx = float(db.narx_tekshir(messagre.from_user.id))
      db.add_narx(narx-delivery_cost,messagre.from_user.id)

   await messagre.answer("Buyurtma yetkazib berilsinmi yoki olib ketasizmi?",reply_markup=type_uzb)
   await uzb_menu_state.type.set()








###MENU KOMBO
@dp.message_handler(text="Kombo aksiya 🏷")
async def kombo_aksiya(message:types.Message):
   await message.answer("Bo`limlardan birini tanlang!",reply_markup=kombo_uzb)

###KOMBO3
@dp.message_handler(text="GIJDUVON KOMBO 3 kishilik")
async def kombo1(message:types.Message):
   photo = "AgACAgIAAxkBAAISWWR_cImhmCp_QVFeFhprsGx0aHyTAAJ5yDEb7Hj4S9_6kwABRY0TNwEAAwIAA3kAAy8E"
   await message.answer_photo(photo,caption="<b>GIJDUVON KOMBO 3 kishilik</b>\n\n"
                        "<b>Tarkibi</b>\n"
                        "Qiyma 3 ta\n"
                        "Olot somsa 3 ta\n"
                        "Qanotchalar 3 ta\n"
                        "Oyoqchalar 3 ta\n"
                        "Fri\n"
                        "Coca cola 1L\n"
                        "Jami narxi atigi <b>109.900 so`m</b>")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.combo3.set()

@dp.message_handler(state=uzb_menu_state.combo3,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Bo`limlardan birini tanlang:",reply_markup=kombo_uzb)
   await state.finish()


@dp.message_handler(content_types=ContentType.TEXT, state=uzb_menu_state.combo3)
async def combo3ni_buyurt(msg:types.Message,state=FSMContext):
   try:
      jonat = f"GIJDUVON KOMBO 3 kishilik {msg.text}ta\n" \
              f"{msg.text}*109 900={float(msg.text) * 109900} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 109900}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"GIJDUVON KOMBO 3 kishilik {msg.text}ta\n" \
                 f"{msg.text}*109 900={float(msg.text) * 109900}so`m\n\n"
         narx = f"{float(msg.text) * 109900}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")

###KOMBO5
@dp.message_handler(text="GIJDUVON KOMBO 5 kishilik")
async def kombo1(message:types.Message):

   photo = "AgACAgIAAxkBAAISW2R_cNP-QXNLrokZPzRDMMfhINfhAAJ6yDEb7Hj4S2WFg0wWM9eXAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="<b>GIJDUVON KOMBO 5 kishilik</b>\n\n"
                        "<b>Tarkibi</b>\n"
                        "Qiyma 5 ta\n"
                        "Olot somsa 5ta\n"
                        "Qanotchalar 5 ta\n"
                        "Oyoqchalar 5 ta\n"
                        "Fri\n"
                        "Coca cola 1.5L\n"
                        "Jami narxi atigi <b>168.900 so`m</b>")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.combo5.set()

@dp.message_handler(state=uzb_menu_state.combo5,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Bo`limlardan birini tanlang:",reply_markup=kombo_uzb)
   await state.finish()


@dp.message_handler(content_types=ContentType.TEXT, state=uzb_menu_state.combo5)
async def combo3ni_buyurt(msg:types.Message,state=FSMContext):
   try:
      jonat = f"GIJDUVON KOMBO 5 kishilik {msg.text}ta\n" \
              f"{msg.text}*168 900={float(msg.text) * 168900} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 168900}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"GIJDUVON KOMBO 5 kishilik {msg.text}ta\n" \
                 f"{msg.text}*168 900={float(msg.text) * 168900}so`m\n\n"
         narx = f"{float(msg.text) * 168900}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="◀️ Ortga")
async def ortga(message:types.Message):
   await message.answer("Bo`limlardan birini tanlang:",reply_markup=menu_uzb)












###SALATLAR
@dp.message_handler(text="Salatlar 🥗")
async def salatlar_uzb(message:types.Message):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)

@dp.message_handler(text="Svejiy salat")
async def svajiy_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVSWSBtxeTvgjWzU94HZteSAg5UV4KAALnxjEbsagRSGbbzugPpxBUAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Svejiy salat\n"
                                            "Narxi: 25.000 so`m")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.svejiy_salat.set()


@dp.message_handler(state=uzb_menu_state.svejiy_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.svejiy_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Svejiy salat {msg.text}ta\n" \
              f"{msg.text}*25 000={float(msg.text) * 25000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 25000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Svejiy salat {msg.text}ta\n" \
                 f"{msg.text}*25 000={float(msg.text) * 25000}so`m\n"\
                  f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 25000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Sezar salat")
async def sezer_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVS2SBt0LH7yw_CxZRFvfelMcsjb-oAALoxjEbsagRSHMDiaivsQV8AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Sezar salat\n"
                                            "Narxi: 30.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.sezer_salat.set()


@dp.message_handler(state=uzb_menu_state.sezer_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.sezer_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Sezar salat {msg.text}ta\n" \
              f"{msg.text}*30 000={float(msg.text) * 30000} so'm\n"\
               f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 30000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Sezar salat {msg.text}ta\n" \
                 f"{msg.text}*30 000={float(msg.text) * 30000}so`m\n"\
                  f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 30000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Smak salat")
async def smak_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVTWSBt3xN0BxKbdFuxRK6zokqfMvcAALlxjEbsagRSP625mmmp_2EAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Smak salat\n"
                                            "Narxi: 28.000")
   await message.answer("Ushbu mahsulotdan necha dona olomqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.smak_salat.set()

@dp.message_handler(state=uzb_menu_state.smak_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.smak_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Smak salat {msg.text}ta\n" \
              f"{msg.text}*28 000={float(msg.text) * 28000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Smak salat {msg.text}ta\n" \
                 f"{msg.text}*28 000={float(msg.text) * 28000}so`m\n"\
                  f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")

@dp.message_handler(text="Olivya salat")
async def Olivya_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVT2SBt7k9HmCdskrtXmQ5Ny1VUuOMAALqxjEbsagRSKQuVvJK-VvwAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Olivya salat\n"
                                            "Narxi: 28.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.oliviya_salat.set()


@dp.message_handler(state=uzb_menu_state.oliviya_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.oliviya_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Olivya salat {msg.text}ta\n" \
              f"{msg.text}*28 000={float(msg.text) * 28000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Olivya salat {msg.text}ta\n" \
                 f"{msg.text}*28 000={float(msg.text) * 28000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")



@dp.message_handler(text="Muskoy kapriz salat")
async def Muskoy_kapriz_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVUWSBt8-u9UImROqwhE7ZoDZXzQnCAALsxjEbsagRSHEkzfeix4ZlAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Muskoy kapriz salat\n"
                                            "Narxi: 28.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.muskoy_salat.set()


@dp.message_handler(state=uzb_menu_state.muskoy_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.muskoy_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Muskoy kapriz salat {msg.text}ta\n" \
              f"{msg.text}*28 000={float(msg.text) * 28000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Muskoy kapriz salat {msg.text}ta\n" \
                 f"{msg.text}*28 000={float(msg.text) * 28000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Gurman salat")
async def gurman_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVU2SBuA-0Xe1gZRRSQZ_zari6Ira_AALtxjEbsagRSNTTZa-3NwYvAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Gurman salat\n"
                                            "Narxi: 28.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.gurman_salat.set()

@dp.message_handler(state=uzb_menu_state.gurman_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.gurman_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Gurman salat {msg.text}ta\n" \
              f"{msg.text}*28 000={float(msg.text) * 28000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Gurman salat {msg.text}ta\n" \
                 f"{msg.text}*28 000={float(msg.text) * 28000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Grecheski salat")
async def grecheski_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVVWSBuDCnNtvLjOHdswx-0oyVhgM9AALuxjEbsagRSNM03auHfw9iAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Grecheski salat\n"
                                            "Narxi: 28.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.grecheski_salat.set()


@dp.message_handler(state=uzb_menu_state.grecheski_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.grecheski_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Grecheski salat {msg.text}ta\n" \
              f"{msg.text}*28 000={float(msg.text) * 28000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Grecheski salat {msg.text}ta\n" \
                 f"{msg.text}*28 000={float(msg.text) * 28000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Fransuzki salat")
async def fransuzki_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVV2SBuHDg9HT-fmOg7Duzr1LlkqowAALwxjEbsagRSCQgGm68Gj88AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Fransuzki salat\n"
                                            "Narxi: 28.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.fransuzki_salat.set()


@dp.message_handler(state=uzb_menu_state.fransuzki_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.fransuzki_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Fransuzki salat {msg.text}ta\n" \
              f"{msg.text}*28 000={float(msg.text) * 28000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Fransuzki salat {msg.text}ta\n" \
                 f"{msg.text}*28 000={float(msg.text) * 28000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 28000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="G`ijduvon salat")
async def gijduvon_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVWWSBuILX1ixAVCubaLWYLPSGt-RHAALxxjEbsagRSHxH3Ras7QL_AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="G`ijduvon salat\n"
                                            "Narxi: 32.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.gijduvon_salat.set()


@dp.message_handler(state=uzb_menu_state.gijduvon_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.gijduvon_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"G`ijduvon salat {msg.text}ta\n" \
              f"{msg.text}*32 000={float(msg.text) * 32000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 32000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"G`ijduvon salat {msg.text}ta\n" \
                 f"{msg.text}*32 000={float(msg.text) * 32000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 32000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Chiroqchi salat")
async def gijduvon_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVW2SBuKE9vL2KLNVZ-Dz53wvRDsegAALyxjEbsagRSNCgKi6CDJp_AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Chiroqchi salat\n"
                                            "Narxi: 22.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.chiroqchi_salat.set()


@dp.message_handler(state=uzb_menu_state.chiroqchi_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.chiroqchi_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Chiroqchi salat {msg.text}ta\n" \
              f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 22000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Chiroqchi salat {msg.text}ta\n" \
                 f"{msg.text}*22 000={float(msg.text) * 22000}so`m\n"\
                  f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 22000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Achichuv salat")
async def achichuv_salat(message:types.Message):
   photo = "AgACAgIAAxkBAAIVXWSBuNcsscJNR4CZ1-T3cNKQ1Wc9AAL0xjEbsagRSFKaH8uQ62o1AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Achichuv salat\n"
                                            "Narxi: 20.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.achichuv_salat.set()

@dp.message_handler(state=uzb_menu_state.achichuv_salat,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Salatlardan birini tanlang...",reply_markup=salatlar_uzb_)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.achichuv_salat,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Achichuv salat {msg.text}ta\n" \
              f"{msg.text}*20 000={float(msg.text) * 20000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 20000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Achichuv salat {msg.text}ta\n" \
                 f"{msg.text}*20 000={float(msg.text) * 20000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 20000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")











###SHASHLIKLAR
@dp.message_handler(text="Shashliklar 🍢")
async def shashliklarr(message:types.Message):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)

@dp.message_handler(text="Tovuq file")
async def tovuq_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVX2SBuPVETsKBfVYl44PyCICXQWTdAAL1xjEbsagRSOtUZWT359R2AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Tovuq file\n"
                                            "Narxi: 19.000")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.tovuq_file.set()

@dp.message_handler(state=uzb_menu_state.tovuq_file,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.tovuq_file,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if float(msg.text) == 5:
         jonat = f"Tovuq file {msg.text}ta\n" \
                 f"{msg.text}*19 000={float(msg.text) * 19000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
      else:
         jonat = f"Tovuq file {msg.text}ta\n" \
                 f"{msg.text}*19 000={float(msg.text) * 19000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"

      if db.tekshir(msg.from_user.id) == None:
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 19000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 19000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         if float(msg.text) == 5:
            jonat = f"Tovuq file {msg.text}ta\n" \
                    f"{msg.text}*19 000={float(msg.text) * 19000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
         else:
            jonat = f"Tovuq file {msg.text}ta\n" \
                    f"{msg.text}*19 000={float(msg.text) * 19000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 19000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 19000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")



@dp.message_handler(text="Qo`y jaz")
async def qoyjaz_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVYWSBuRZUSsfUEgNQaQOVJ3jHgdEAA_bGMRuxqBFItGvotbXMXrABAAMCAAN5AAMvBA"
   await message.answer_photo(photo,caption="Qo`y jaz\n"
                                            "Narxi: 17.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.qoy_jaz.set()

@dp.message_handler(state=uzb_menu_state.qoy_jaz,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.qoy_jaz,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if float(msg.text) == 5:
         jonat = f"Qo`y jaz {msg.text}ta\n" \
                 f"{msg.text}*17 000={float(msg.text) * 17000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
      else:
         jonat = f"Qo`y jaz {msg.text}ta\n" \
                 f"{msg.text}*17 000={float(msg.text) * 17000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"

      if db.tekshir(msg.from_user.id) == None:
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 17000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 17000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         if float(msg.text) == 5:
            jonat = f"Qo`y jaz {msg.text}ta\n" \
                    f"{msg.text}*17 000={float(msg.text) * 17000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
         else:
            jonat = f"Qo`y jaz {msg.text}ta\n" \
                    f"{msg.text}*17 000={float(msg.text) * 17000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 17000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 17000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Qiyma")
async def qiyma_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVY2SBuT1o7rHp_lOIUFl2xFVIJbv-AAL3xjEbsagRSMnAcRDTH5_xAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Qiyma\n"
                                            "Narxi: 15.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.qiyma.set()


@dp.message_handler(state=uzb_menu_state.qiyma,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.qiyma,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if float(msg.text) == 5:
         jonat = f"Qiyma {msg.text}ta\n" \
                 f"{msg.text}*15 000={float(msg.text) * 15000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
      else:
         jonat = f"Qiyma {msg.text}ta\n" \
                 f"{msg.text}*15 000={float(msg.text) * 15000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"

      if db.tekshir(msg.from_user.id) == None:
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 15000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 15000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         if float(msg.text) == 5:
            jonat = f"Qiyma {msg.text}ta\n" \
                    f"{msg.text}*15 000={float(msg.text) * 15000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
         else:
            jonat = f"Qiyma {msg.text}ta\n" \
                    f"{msg.text}*15 000={float(msg.text) * 15000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 15000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 15000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Pomidor")
async def pomidor_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVZWSBuWVJLyB5Q7QMpkGFKUfRid_LAAL4xjEbsagRSLhBI5Cl-7i_AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Pomidor\n"
                                            "Narxi: 10.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.pomidor.set()


@dp.message_handler(state=uzb_menu_state.pomidor,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.pomidor,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if float(msg.text) == 5:
         jonat = f"Pomidor {msg.text}ta\n" \
                 f"{msg.text}*10 000={float(msg.text) * 10000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
      else:
         jonat = f"Pomidor {msg.text}ta\n" \
                 f"{msg.text}*10 000={float(msg.text) * 10000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"

      if db.tekshir(msg.from_user.id) == None:
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 10000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 10000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         if float(msg.text) == 5:
            jonat = f"Pomidor {msg.text}ta\n" \
                    f"{msg.text}*10 000={float(msg.text) * 10000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
         else:
            jonat = f"Pomidor {msg.text}ta\n" \
                    f"{msg.text}*10 000={float(msg.text) * 10000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 10000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 10000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")



@dp.message_handler(text="Mol Jaz")
async def moljaz_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVZ2SBuYGNeQJ5q_irAptCQkKZbHQtAAL5xjEbsagRSC36aMMtNMOPAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Mol Jaz\n"
                                            "Narxi: 17.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.moljaz.set()

@dp.message_handler(state=uzb_menu_state.moljaz,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.moljaz,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if float(msg.text) == 5:
         jonat = f"Mol Jaz {msg.text}ta\n" \
                 f"{msg.text}*17 000={float(msg.text) * 17000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
      else:
         jonat = f"Mol Jaz {msg.text}ta\n" \
                 f"{msg.text}*17 000={float(msg.text) * 17000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"

      if db.tekshir(msg.from_user.id) == None:
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 17000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 17000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         if float(msg.text) == 5:
            jonat = f"Mol Jaz {msg.text}ta\n" \
                    f"{msg.text}*17 000={float(msg.text) * 17000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
         else:
            jonat = f"Mol Jaz {msg.text}ta\n" \
                    f"{msg.text}*17 000={float(msg.text) * 17000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 17000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 17000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Krilishka")
async def krilishka_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVaWSBuaDUfisiSvn7q7G_Xj5td5avAAL6xjEbsagRSJYN4VMjFWKTAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Krilishka\n"
                                            "Narxi: 22.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.krilishka.set()

@dp.message_handler(state=uzb_menu_state.krilishka,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.krilishka,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if float(msg.text) == 5:
         jonat = f"Krilishka {msg.text}ta\n" \
                 f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
      else:
         jonat = f"Krilishka {msg.text}ta\n" \
                 f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"

      if db.tekshir(msg.from_user.id) == None:
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 22000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 22000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         if float(msg.text) == 5:
            jonat = f"Krilishka {msg.text}ta\n" \
                    f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
         else:
            jonat = f"Krilishka {msg.text}ta\n" \
                    f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 22000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 22000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")



@dp.message_handler(text="Bon file")
async def bonfile_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVa2SBub_C-iVpOPiMJxWL2U04bGBjAAL7xjEbsagRSI-j0xBZS9hdAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Bon file\n"
                                            "Narxi: 22.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.bonfile.set()


@dp.message_handler(state=uzb_menu_state.bonfile,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.bonfile,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if float(msg.text) == 5:
         jonat = f"Bon file {msg.text}ta\n" \
                 f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
      else:
         jonat = f"Bon file {msg.text}ta\n" \
                 f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"

      if db.tekshir(msg.from_user.id) == None:
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 22000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 22000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         if float(msg.text) == 5:
            jonat = f"Bon file {msg.text}ta\n" \
                    f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
         else:
            jonat = f"Bon file {msg.text}ta\n" \
                    f"{msg.text}*22 000={float(msg.text) * 22000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 22000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 22000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Baranni ryabrishka")
async def baranni_ryabrishka_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVbWSBuddGtrNB7VKW8E0cyTQ2FxBxAAL8xjEbsagRSMhoFbASQPfAAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Baranni ryabrishka\n"
                                            "Narxi: 29.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.baranni.set()

@dp.message_handler(state=uzb_menu_state.baranni,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.baranni,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if float(msg.text) == 5:
         jonat = f"Baranni ryabrishka {msg.text}ta\n" \
                 f"{msg.text}*29 000={float(msg.text) * 29000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
      else:
         jonat = f"Baranni ryabrishka {msg.text}ta\n" \
                 f"{msg.text}*29 000={float(msg.text) * 29000} so'm\n" \
                 f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"

      if db.tekshir(msg.from_user.id) == None:
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 29000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 29000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         if float(msg.text) == 5:
            jonat = f"Baranni ryabrishka {msg.text}ta\n" \
                    f"{msg.text}*29 000={float(msg.text) * 29000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi 2000 so'm\n\n"
         else:
            jonat = f"Baranni ryabrishka {msg.text}ta\n" \
                    f"{msg.text}*29 000={float(msg.text) * 29000} so'm\n" \
                    f"Ushbu mahsulot uchun idish narxi {(float(msg.text) // 5 + 1) * 2000} so'm\n\n"
         if float(msg.text) == 5:
            narx = f"{float(msg.text) * 29000 + 2000}\n"
         else:
            narx = f"{float(msg.text) * 29000 + 2000 * (float(msg.text) // 5 + 1)}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")



@dp.message_handler(text="⬅️Qaytish")
async def qaytish_to_salatlar(message:types.Message):
   await message.answer("Shashliklardan birini tanlang...",reply_markup=shashliklar_uzb)










###BIRINCHI TAOMLAR
@dp.message_handler(text="Birinchi taomlar 🍜")
async def birinchi_taomlar(message:types.Message):
   await message.answer("Taomlardan birini tanlang...",reply_markup=birinchi_taomlar_uzb)

@dp.message_handler(text="Qaynatma sho`rva")
async def qaynatma(message:types.Message):
   photo = "AgACAgIAAxkBAAIVb2SBufNI0wmOxUT6DD_zPH3QopooAAL9xjEbsagRSG5y80SoWMdKAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Qaynatma sho`rva\n"
                                            "Narxi: 25.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.qaynatma.set()

@dp.message_handler(state=uzb_menu_state.qaynatma,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=birinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.qaynatma,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Qaynatma sho`rva {msg.text}ta\n" \
              f"{msg.text}*25 000={float(msg.text) * 25000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 25000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Qaynatma sho`rva {msg.text}ta\n" \
                 f"{msg.text}*25 000={float(msg.text) * 25000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 25000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")



@dp.message_handler(text="Mastava")
async def mastava(message:types.Message):
   photo = "AgACAgIAAxkBAAIVcWSBuhCG9KuaBE-kGom0Y_3I2ZK-AAIBxzEbsagRSL2A60PpNAofAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Mastava\n"
                                            "Narxi: 25.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.mastava.set()

@dp.message_handler(state=uzb_menu_state.mastava,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=birinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.mastava,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Mastava {msg.text}ta\n" \
              f"{msg.text}*25 000={float(msg.text) * 25000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 25000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Mastava {msg.text}ta\n" \
                 f"{msg.text}*25 000={float(msg.text) * 25000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 25000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")



@dp.message_handler(text="Pelmen")
async def pelmen(message:types.Message):
   photo = "AgACAgIAAxkBAAIVc2SBujeJQEs49-zSZFUV6nkq8JqvAAIDxzEbsagRSCasYqJ5rwgDAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Pelmen\n"
                                            "Narxi: 25.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.pelmen.set()

@dp.message_handler(state=uzb_menu_state.pelmen,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=birinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.pelmen,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Pelmen {msg.text}ta\n" \
              f"{msg.text}*25 000={float(msg.text) * 25000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 25000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Pelmen {msg.text}ta\n" \
                 f"{msg.text}*25 000={float(msg.text) * 25000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 25000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Balaza")
async def balaza(message:types.Message):
   photo = "AgACAgIAAxkBAAIVdWSBulDCA8ryBPNeyFxgtF_QjtrQAAIExzEbsagRSO-Ws37WKxN0AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Balaza\n"
                                            "Narxi: 23.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.balaza.set()


@dp.message_handler(state=uzb_menu_state.balaza,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=birinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.balaza,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Balaza {msg.text}ta\n" \
              f"{msg.text}*23 000={float(msg.text) * 23000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 23000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Balaza {msg.text}ta\n" \
                 f"{msg.text}*23 000={float(msg.text) * 23000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 23000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Qaytish ⬅️")
async def qayt(message:types.Message):
   await message.answer("Taomlardan birini tanlang...",reply_markup=birinchi_taomlar_uzb)









#####IKKINCHI TAOMLAR
@dp.message_handler(text="Ikkinchi taomlar 🥘")
async def ikkinchi_taomlar(message:types.Message):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)

@dp.message_handler(text="G'ijduvon Jiz")
async def gijduvan_jiz(message:types.Message):
   photo = "AgACAgIAAxkBAAIVd2SBum6tmiUITMb-62rybddAlOqZAAIOxzEbsagRSIUI8k1s0OXxAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="G'ijduvon Jiz\n"
                                            "Narxi: 1 kg - 180.000 so'm")
   await message.answer("Ushbu mahsulotdan necha kilogram olmoqchisiz, tanlang 👇 yoki yozing ",reply_markup=antiqa_sonlar_uzb)
   await uzb_menu_state.gijduvon_jiz.set()


@dp.message_handler(state=uzb_menu_state.gijduvon_jiz,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)
   await state.finish()


@dp.message_handler(state=uzb_menu_state.gijduvon_jiz,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   # try:

   # except ValueError:
   #    await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")
   jonat = f"G'ijduvon Jiz {msg.text}kg\n" \
           f"{msg.text}*180 000={float(msg.text) * 180000} so'm\n" \
           f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
   if db.tekshir(msg.from_user.id) == None:
      narx = f"{float(msg.text) * 180000 + 2000}\n"
      try:
         db.add_new_product(new=jonat, id=msg.from_user.id)
      except sqlite3.IntegrityError as err:
         await bot.send_message(chat_id=ADMINS[0], text=err)

      try:
         db.add_narx(narx=narx, id=msg.from_user.id)
      except sqlite3.IntegrityError as err:
         await bot.send_message(chat_id=ADMINS[0], text=err)
   else:
      matn = db.tekshir(msg.from_user.id)
      jonat = f"G'ijduvon Jiz {msg.text}kg\n" \
              f"{msg.text}*180 000={float(msg.text) * 180000}so`m\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      narx = f"{float(msg.text) * 180000 + 2000}\n"
      matn += jonat
      try:
         db.add_new_product(new=matn, id=msg.from_user.id)
      except sqlite3.IntegrityError as err:
         await bot.send_message(chat_id=ADMINS[0], text=err)

      eski = float(db.narx_tekshir(msg.from_user.id))
      eski += float(narx)
      try:
         db.add_narx(narx=eski, id=msg.from_user.id)
      except sqlite3.IntegrityError as err:
         await bot.send_message(chat_id=ADMINS[0], text=err)
   await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                    "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
   await state.finish()


@dp.message_handler(text="Vaguri 2")
async def vaguri(message:types.Message):
   photo = "AgACAgIAAxkBAAIVeWSBuokRhpJN0lVQ-5CKfd_6_jVXAAIQxzEbsagRSNgjm9ajyguOAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Vaguri 2\n"
                                            "Narxi: 1 kg 180.000 so'm")
   await message.answer("Ushbu mahsulotdan necha kg olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=antiqa_sonlar_uzb)
   await uzb_menu_state.vaguri.set()

@dp.message_handler(state=uzb_menu_state.vaguri,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.vaguri,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Vaguri 2 {msg.text}ta\n" \
              f"{msg.text}*180 000={float(msg.text) * 180000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 180000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Vaguri 2 {msg.text}kg\n" \
                 f"{msg.text}*180 000={float(msg.text) * 180000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 180000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Afgan jiz")
async def afgan_jiz(message:types.Message):
   photo = "AgACAgIAAxkBAAIVe2SBuqMeAhhUuOdQRNPYo3Xi2KWSAAIRxzEbsagRSCtNUKthjidXAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Afgan jiz\n"
                                            "Narxi: 1 kg 180.000 so'm")
   await message.answer("Ushbu mahsulotdan necha kg olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=antiqa_sonlar_uzb)
   await uzb_menu_state.afgan_jiz.set()

@dp.message_handler(state=uzb_menu_state.afgan_jiz,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.afgan_jiz,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Afgan jiz {msg.text}kg\n" \
              f"{msg.text}*180 000={float(msg.text) * 180000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 180000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Afgan jiz {msg.text}kg\n" \
                 f"{msg.text}*180 000={float(msg.text) * 180000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 180000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Olot somsa")
async def olotsonsa(message:types.Message):
   photo = "AgACAgIAAxkBAAIVfWSBur6rOAZDDSWD4M9Yme_ua52sAAIUxzEbsagRSMmnmbmuVa_hAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Olot somsa\n"
                                            "Narxi: 8.000 so'm (minimal zakaz 2ta)")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.olot_somsa.set()

@dp.message_handler(state=uzb_menu_state.olot_somsa,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.olot_somsa,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Olot somsa {msg.text}ta\n" \
              f"{msg.text}*8 000={float(msg.text) * 8000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 8000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Olot somsa {msg.text}ta\n" \
                 f"{msg.text}*8 000={float(msg.text) * 8000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 8000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")

# @dp.message_handler(text="Sazan")
# async def sazan(message:types.Message):
#    photo = "AgACAgIAAxkBAAIFGWR3mQABx3GyIeO6x5EoUK0f2PxRIAACFswxG7uZwUvekdh5Uu0BiwEAAwIAA3kAAy8E"
#    await message.answer_photo(photo,caption="Sazan\n"
#                                             "Narxi: ")
#    await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)


@dp.message_handler(text="Sudaak file")
async def sudak_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVf2SBuuH_w-0V7wFzwbOW8gzLpaNGAAIWxzEbsagRSLy4KSC-TSZzAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Sudaak file\n"
                                            "Narxi: 1 kg 180.000 so'm")
   await message.answer("Ushbu mahsulotdan necha kg olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=antiqa_sonlar_uzb)
   await uzb_menu_state.sudak_file.set()

@dp.message_handler(state=uzb_menu_state.sudak_file,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.sudak_file,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Sudaak file {msg.text}kg\n" \
              f"{msg.text}*180 000={float(msg.text) * 180000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 180000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Sudaak file {msg.text}kg\n" \
                 f"{msg.text}*180 000={float(msg.text) * 180000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 180000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Semichka")
async def sudak_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVgWSBuw232RRaH6vbaQkL1yCD3UMJAAIXxzEbsagRSO7MklJ8tNXfAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Semichka\n"
                                            "Narxi: 1 kg - 180.000 so'm")
   await message.answer("Ushbu mahsulotdan necha kg olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=antiqa_sonlar_uzb)
   await uzb_menu_state.semichka.set()

@dp.message_handler(state=uzb_menu_state.semichka,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.semichka,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Semichka {msg.text}kg\n" \
              f"{msg.text}*180 000={float(msg.text) * 180000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 180000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Semichka {msg.text}kg\n" \
                 f"{msg.text}*180 000={float(msg.text) * 180000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 180000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Vaguri spes")
async def sudak_file(message:types.Message):
   photo = "AgACAgIAAxkBAAIVg2SBuynB1yiwQhG8oyDCm63ni6O-AAIdxzEbsagRSMChthBZkmB0AQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Vaguri spes\n"
                                            "Narxi: 1Kg 200.000 so'm")
   await message.answer("Ushbu mahsulotdan necha kg olmoqchisiz tanlang yoki yozing!!!",reply_markup=antiqa_sonlar_uzb)
   await uzb_menu_state.vaguri_spes.set()

@dp.message_handler(state=uzb_menu_state.vaguri_spes,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.vaguri_spes,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Vaguri spes {msg.text} kg\n" \
              f"{msg.text}*200 000={float(msg.text) * 200000} so'm\n" \
              f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 200000 + 2000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Vaguri spes {msg.text} kg\n" \
                 f"{msg.text}*200 000={float(msg.text) * 200000}so`m\n" \
                 f"Ushbu mahsulot uchun idish narxi 2.000 so'm\n\n"
         narx = f"{float(msg.text) * 200000 + 2000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")

@dp.message_handler(text="Qaytish⬅️")
async def qayt(message:types.Message):
   await message.answer("Taomlardan birini tanlang...",reply_markup=ikkinchi_taomlar_uzb)









###ICHIMLIKLAR
@dp.message_handler(text="Ichimliklar 🍷")
async def ichimliklar(message:types.Message):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)


###Cola 0.5 l
@dp.message_handler(text="Cola 0.5 L")
async def cola05(message:types.Message):
   photo = "https://www.freshandco.at/wp-content/uploads/2017/09/Cola.png"
   await message.answer_photo(photo,caption="Coca Cola 0.5 L\n"
                                            "Narxi: 9.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.cola05.set()

@dp.message_handler(state=uzb_menu_state.cola05,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(content_types=types.ContentType.TEXT,state=uzb_menu_state.cola05)
async def tovuq(msg:types.Message,state=FSMContext):
    try:
        if db.tekshir(msg.from_user.id)==None:
            jonat = f"Coca Cola 0.5 L {msg.text}ta\n" \
                    f"{msg.text}*9 000={float(msg.text) * 9000} so`m\n\n"
            narx = f"{float(msg.text) * 9000}\n"
            try:
                db.add_new_product(new=jonat, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)

            # narxni qoshish
            try:
                db.add_narx(narx=narx, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
        else:
            matn = db.tekshir(msg.from_user.id)
            jonat = f"Coca Cola 0.5 L {msg.text}ta\n" \
                    f"{msg.text}*9 000={float(msg.text) * 9000} so`m\n\n"
            narx = f"{float(msg.text) * 9000}\n"
            matn+=jonat
            try:
                db.add_new_product(new=matn, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)

            eski = float(db.narx_tekshir(msg.from_user.id))
            eski += float(narx)
            try:
                db.add_narx(narx=eski, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
        await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                         "Yana biror narsa olasizmi?",reply_markup=menu_uzb)
        await state.finish()
    except ValueError:
        await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


###Cola 1 l
@dp.message_handler(text="Cola 1 L")
async def cola05(message:types.Message):
   photo = "https://www.londondrugs.com/on/demandware.static/-/Sites-londondrugs-master/default/dwfe7c7814/products/L0082412/large/L0082412.JPG"
   await message.answer_photo(photo,caption="Coca Cola 1 L\n"
                                            "Narxi: 13.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.cola1.set()

@dp.message_handler(state=uzb_menu_state.cola1,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(content_types=types.ContentType.TEXT,state=uzb_menu_state.cola1)
async def tovuq(msg:types.Message,state=FSMContext):
    try:
        if db.tekshir(msg.from_user.id)==None:
            jonat = f"Cola 1 L {msg.text}ta\n" \
                    f"{msg.text}*13 000={float(msg.text) * 13000} so'm\n\n"
            narx = f"{float(msg.text) * 13000}\n"
            try:
                db.add_new_product(new=jonat, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)

            # narxni qoshish
            try:
                db.add_narx(narx=narx, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
        else:
            matn = db.tekshir(msg.from_user.id)
            jonat = f"Cola 1 L {msg.text}ta\n" \
                    f"{msg.text}*13 000={float(msg.text) * 13000} so`m\n\n"
            narx = f"{float(msg.text) * 13000}\n"
            matn+=jonat
            try:
                db.add_new_product(new=matn, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)

            eski = float(db.narx_tekshir(msg.from_user.id))
            eski += float(narx)
            try:
                db.add_narx(narx=eski, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
        await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                         "Yana biror narsa olasizmi?",reply_markup=menu_uzb)
        await state.finish()
    except ValueError:
        await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")




@dp.message_handler(text="Cola 1.5 L")
async def cola05(message:types.Message):
   photo = "AgACAgIAAxkBAAIVhWSBu09WPSEEense2dKlwDStmIQIAAIkxzEbsagRSK5lZxI6NtlYAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Coca Cola 1.5 L\n"
                                            "Narxi: 16.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.cola15.set()

@dp.message_handler(state=uzb_menu_state.cola15,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(content_types=types.ContentType.TEXT,state=uzb_menu_state.cola15)
async def tovuq(msg:types.Message,state=FSMContext):
    try:
        if db.tekshir(msg.from_user.id)==None:
            jonat = f"Cola 1.5 L {msg.text}ta\n" \
                    f"{msg.text}*16 000={float(msg.text) * 16000}so`m\n\n"
            narx = f"{float(msg.text) * 16000}\n"
            try:
                db.add_new_product(new=jonat, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)

            # narxni qoshish
            try:
                db.add_narx(narx=narx, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
        else:
            matn = db.tekshir(msg.from_user.id)
            jonat = f"Cola 1.5 L {msg.text}ta\n" \
                    f"{msg.text}*16 000={float(msg.text) * 16000} so`m\n\n"
            narx = f"{float(msg.text) * 16000}\n"
            matn+=jonat
            try:
                db.add_new_product(new=matn, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)

            eski = float(db.narx_tekshir(msg.from_user.id))
            eski += float(narx)
            try:
                db.add_narx(narx=eski, id=msg.from_user.id)
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
        await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                         "Yana biror narsa olasizmi?",reply_markup=menu_uzb)
        await state.finish()
    except ValueError:
        await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")




@dp.message_handler(text="Pepsi 0.5 L")
async def cola05(message:types.Message):
   photo = "AgACAgIAAxkBAAIVh2SBu20K-n9I4DgMTyJQPj6Z8qw6AAIlxzEbsagRSMtpfOuApccmAQADAgADeAADLwQ"
   await message.answer_photo(photo,caption="Pepsi 0.5 L\n"
                                            "Narxi: 9.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.pepsi05.set()

@dp.message_handler(state=uzb_menu_state.pepsi05,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.pepsi05,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if db.tekshir(msg.from_user.id) == None:
         jonat = f"Pepsi 0.5 L {msg.text}ta\n" \
                 f"{msg.text}*9 000={float(msg.text) * 9000} so'm\n\n"
         narx = f"{float(msg.text) * 9000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Pepsi 0.5 L {msg.text}ta\n" \
                 f"{msg.text}*9 000={float(msg.text) * 9000}so`m\n\n"
         narx = f"{float(msg.text) * 9000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Pepsi 1 L")
async def cola05(message:types.Message):
   photo = "AgACAgIAAxkBAAIVh2SBu20K-n9I4DgMTyJQPj6Z8qw6AAIlxzEbsagRSMtpfOuApccmAQADAgADeAADLwQ"
   await message.answer_photo(photo,caption="Pepsi 1 L\n"
                                            "Narxi: 13.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.pepsi1.set()

@dp.message_handler(state=uzb_menu_state.pepsi1,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.pepsi1,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      if db.tekshir(msg.from_user.id) == None:
         jonat = f"Pepsi 1 L {msg.text}ta\n" \
                 f"{msg.text}*13 000={float(msg.text) * 13000} so'm\n\n"
         narx = f"{float(msg.text) * 13000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Pepsi 1 L {msg.text}ta\n" \
                 f"{msg.text}*13 000={float(msg.text) * 13000}so`m\n\n"
         narx = f"{float(msg.text) * 13000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Pepsi 1.5 L")
async def cola05(message:types.Message):
   # photo = InputFile(path_or_bytesio="./data/photos/IMG_6729.JPG")
   photo = "AgACAgIAAxkBAAIVh2SBu20K-n9I4DgMTyJQPj6Z8qw6AAIlxzEbsagRSMtpfOuApccmAQADAgADeAADLwQ"
   await message.answer_photo(photo,caption="Pepsi 1.5 L\n"
                                            "Narxi: 16.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.pepsi15.set()

@dp.message_handler(state=uzb_menu_state.pepsi15,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.pepsi15,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Pepsi 1.5 L {msg.text}ta\n" \
              f"{msg.text}*16 000={float(msg.text) * 16000} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 16000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Pepsi 1.5 L {msg.text}ta\n" \
                 f"{msg.text}*16 000={float(msg.text) * 16000}so`m\n\n"
         narx = f"{float(msg.text) * 16000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Suv 0.5 L")
async def cola05(message:types.Message):
   # photo = InputFile(path_or_bytesio="./data/photos/IMG_6725.JPG")
   photo = "AgACAgIAAxkBAAIViWSBu6wKJ72YcwbKXEyC-8vVsUeaAAIuxzEbsagRSBRDLAwFz8WfAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Suv 0.5 L\n"
                                            "Narxi: 3.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.suv05.set()

@dp.message_handler(state=uzb_menu_state.suv05,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.suv05,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Suv 0.5 L {msg.text}ta\n" \
              f"{msg.text}*3 000={float(msg.text) * 3000} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 3000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Suv 0.5 L {msg.text}ta\n" \
                 f"{msg.text}*3 000={float(msg.text) * 3000}so`m\n\n"
         narx = f"{float(msg.text) * 3000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Suv 1 L")
async def cola05(message:types.Message):
   # photo = InputFile(path_or_bytesio="./data/photos/IMG_6726.JPG")
   photo = "AgACAgIAAxkBAAIVi2SBu8bFWqNFjOmwsG1P0sMfiFpKAAIvxzEbsagRSIx9CTy5FqbGAQADAgADeAADLwQ"
   await message.answer_photo(photo,caption="Suv 1 L\n"
                                            "Narxi: 4.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.suv1.set()

@dp.message_handler(state=uzb_menu_state.suv1,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.suv1,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Suv 1 L {msg.text}ta\n" \
              f"{msg.text}*4 000={float(msg.text) * 4000} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 4000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Suv 1 L {msg.text}ta\n" \
                 f"{msg.text}*4 000={float(msg.text) * 4000}so`m\n\n"
         narx = f"{float(msg.text) * 4000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")

@dp.message_handler(text="Suv 1.5 L")
async def cola05(message:types.Message):
   photo = "AgACAgIAAxkBAAIVi2SBu8bFWqNFjOmwsG1P0sMfiFpKAAIvxzEbsagRSIx9CTy5FqbGAQADAgADeAADLwQ"
   await message.answer_photo(photo,caption="Pepsi 1.5 L\n"
                                            "Narxi: 5.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.suv15.set()

@dp.message_handler(state=uzb_menu_state.suv15,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.suv15,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Suv 1.5 L {msg.text}ta\n" \
              f"{msg.text}*5 000={float(msg.text) * 5000} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 5000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Suv 1.5 L {msg.text}ta\n" \
                 f"{msg.text}*5 000={float(msg.text) * 5000}so`m\n\n"
         narx = f"{float(msg.text) * 5000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")

@dp.message_handler(text="Bliss sok 1 L")
async def cola05(message:types.Message):
   # photo = InputFile(path_or_bytesio="./data/photos/IMG_6732.JPG")
   photo = "AgACAgIAAxkBAAIVjWSBu-uG7yzez1DbqJDAnD8v3rVfAAI2xzEbsagRSERL5y4eHSKoAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Bliss Sok 1L\n"
                                            "Narxi: 16.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.bliss.set()

@dp.message_handler(state=uzb_menu_state.bliss,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.bliss,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Bliss Sok 1L {msg.text}ta\n" \
              f"{msg.text}*16 000={float(msg.text) * 16000} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 16000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Bliss Sok 1L {msg.text}ta\n" \
                 f"{msg.text}*16 000={float(msg.text) * 16000}so`m\n\n"
         narx = f"{float(msg.text) * 16000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Chortoq")
async def cola05(message:types.Message):
   photo = "AgACAgIAAxkBAAIVj2SBvAABXXysZ-E_2dAGDRG8Mlc0cgACO8cxG7GoEUiqTKrA-0mnBAEAAwIAA3gAAy8E"
   await message.answer_photo(photo,caption="Chortoq\n"
                                            "Narxi: 12.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.chortoq.set()

@dp.message_handler(state=uzb_menu_state.chortoq,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.chortoq,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Chortoq {msg.text}ta\n" \
              f"{msg.text}*12 000={float(msg.text) * 12000} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 12000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Chortoq {msg.text}ta\n" \
                 f"{msg.text}*12 000={float(msg.text) * 12000}so`m\n\n"
         narx = f"{float(msg.text) * 12000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")



@dp.message_handler(text="Qaytish 🔙")
async def ortgaaae(message:types.Message):
   await message.answer("Ichimliklardan birini tanlang...",reply_markup=ichimliklar_uzb)










###NONLAR
@dp.message_handler(text="Nonlar 🥐")
async def nonlar(message:types.Message):
   await message.answer("Nonlardan birini tanlang...",reply_markup=nonlar_uzb)

@dp.message_handler(text="Turetiski non")
async def oddiy_non(message:types.Message):
   photo = "AgACAgIAAxkBAAIVkWSBvBzImxhVb9bKYvmB8FlyCzmLAAI9xzEbsagRSDN9Nwbs5NlOAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Turetiski non\n"
                                            "Narxi: 4.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.turetiskiy.set()

@dp.message_handler(state=uzb_menu_state.turetiskiy,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Nonlardan birini tanlang...",reply_markup=nonlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.turetiskiy,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Turetiski non {msg.text}ta\n" \
              f"{msg.text}*4 000={float(msg.text) * 4000} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 4000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Turetiski non {msg.text}ta\n" \
                 f"{msg.text}*4 000={float(msg.text) * 4000}so`m\n\n"
         narx = f"{float(msg.text) * 4000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")


@dp.message_handler(text="Qatlama - Patir")
async def oddiy_non(message:types.Message):
   photo = "AgACAgIAAxkBAAIVk2SBvEChwaBRi100I1kwtwS_QSltAAJDxzEbsagRSBi9wAvxY70NAQADAgADeQADLwQ"
   await message.answer_photo(photo,caption="Qatlama - Patir\n"
                                            "Narxi: 10.000 so'm")
   await message.answer("Ushbu mahsulotdan necha dona olmoqchisiz, tanlang 👇 yoki yozing",reply_markup=sonlar)
   await uzb_menu_state.qatlama.set()

@dp.message_handler(state=uzb_menu_state.qatlama,text="⬅️ Qaytish")
async def orta(message:types.Message,state=FSMContext):
   await message.answer("Nonlardan birini tanlang...",reply_markup=nonlar_uzb)
   await state.finish()

@dp.message_handler(state=uzb_menu_state.qatlama,content_types=ContentType.TEXT)
async def tovuq(msg: types.Message, state=FSMContext):
   try:
      jonat = f"Qatlama - Patir {msg.text}ta\n" \
              f"{msg.text}*10 000={float(msg.text) * 10000} so'm\n\n"
      if db.tekshir(msg.from_user.id) == None:
         narx = f"{float(msg.text) * 10000}\n"
         try:
            db.add_new_product(new=jonat, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         # narxni qoshish
         try:
            db.add_narx(narx=narx, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      else:
         matn = db.tekshir(msg.from_user.id)
         jonat = f"Qatlama - Patir {msg.text}ta\n" \
                 f"{msg.text}*10 000={float(msg.text) * 10000}so`m\n\n"
         narx = f"{float(msg.text) * 10000}\n"
         matn += jonat
         try:
            db.add_new_product(new=matn, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

         eski = float(db.narx_tekshir(msg.from_user.id))
         eski += float(narx)
         try:
            db.add_narx(narx=eski, id=msg.from_user.id)
         except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
      await msg.answer("Ushbu mahsulot savatingizga qo`shildi!\n"
                       "Yana biror narsa olasizmi?", reply_markup=menu_uzb)
      await state.finish()
   except ValueError:
      await msg.answer("Faqat son kiritishingiz mumkin. Qayta urunib ko`ring.")

@dp.message_handler(text="Qaytish🔙")
async def ortgaaaa(message:types.Message):
   await message.answer("Nonlardan birini tanlang...",reply_markup=nonlar_uzb)