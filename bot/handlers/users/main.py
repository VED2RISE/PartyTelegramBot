import random

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from bot.keyboards.default import ticket_type_keyboard, amount_keyboard, exact_amount_keyboard, discount_keyboard
from bot.states import Steps

STANDARD_PRICE = 4000
INSTAGRAM = 'https://www.instagram.com/p/Cof-TgerdyH/?igshid=YmMyMTA2M2Y='
CONTACT_LINK = '@BrilliantmindI'
CARD_NUMBERS = [
    '<b>5559 4941 7264 8858</b> Иван [Альфа-Банк]',
    '<b>5536 9140 4928 9188</b> Николай [Тинькофф]',
    '<b>4377 7237 6033 0484</b> Кирилл [Тинькофф]',
    '<b>5469 3800 5460 0423</b> Кирилл [Сбербанк]',
    '<b>2202 2017 2695 4593</b> Иван [Сбербанк]'
]


async def start(message: types.Message):
    await message.bot.send_message(message.from_id,
                                   f'Элитный нетворк. Все включено\n\n{CONTACT_LINK} - поддержка 24/7')
    await message.bot.send_message(message.from_id,
                                   'Сколько вас?',
                                   reply_markup=amount_keyboard)
    await Steps.amount.set()


async def amount(message: types.Message, state: FSMContext):
    await state.update_data(amount=message.text)
    if message.text == '1':
        await message.bot.send_message(message.from_id,
                                       f'С репостом вечеринки и подпиской скидка 10% - {int(STANDARD_PRICE * 0.9)}₽:\n'
                                       f'{INSTAGRAM}\n\n'
                                       'Билет Standard – безлимитный алкоголь и еда.\n\nХотите скидку?',
                                       reply_markup=discount_keyboard)
        await Steps.discount.set()
    else:
        await message.bot.send_message(message.from_id,
                                       f'Скидка по умолчанию 10% - {int(STANDARD_PRICE * 0.9)}₽. '
                                       f'Скидка с репостом вечеринки в сторис '
                                       f'у каждого гостя и подпиской на нас 15% – {int(STANDARD_PRICE * 0.85)}₽.\n'
                                       f'Пройдите по ссылке и сделайте репост в сторис:'
                                       f'\n{INSTAGRAM}\n\n'
                                       'Билет Standard – безлимитный алкоголь и еда. \n\nСделали репост?',
                                       reply_markup=discount_keyboard)
        await Steps.discount.set()


async def discount(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    if message.text == 'В начало':
        await state.reset_data()
        await state.finish()
        await start(message)
    elif message.text == 'Да':
        card_number = random.choice(CARD_NUMBERS)
        if state_data['amount'] == '1':
            await message.bot.send_message(message.from_id,
                                           f'Стоимость вашего билета {int(STANDARD_PRICE * 0.9)}₽.\n\n'
                                           f'Переведите, пожалуйста, по номеру карты: {card_number}\n\n'
                                           f'После оплаты напишите {CONTACT_LINK}, прикрепите скрин оплаты, свой инстаграмм и напишите свое ФИО. Вас внесут в список и узнаю предпочтения. Спасибо!\n\n'
                                           f'ВНИМАНИЕ! Не забудьте паспорт!',
                                           reply_markup=types.ReplyKeyboardRemove())
            await state.finish()
        else:
            await message.bot.send_message(message.from_id,
                                           f'Стоимость ваших билетов {int(STANDARD_PRICE * int(state_data["amount"]) * 0.85)}₽.\n\n'
                                           f'Переведите, пожалуйста, по номеру карты: {card_number}\n\n'
                                           f'После оплаты напишите {CONTACT_LINK}, прикрепите скрин оплаты, свои инстаграммы и напишите свои ФИО. Вас внесут в список и узнают предпочтения. Спасибо!\n\n'
                                           f'ВНИМАНИЕ! Не забудьте паспорт!',
                                           reply_markup=types.ReplyKeyboardRemove())
            await state.finish()
    elif message.text == 'Нет':
        card_number = random.choice(CARD_NUMBERS)
        if state_data['amount'] == '1':
            await message.bot.send_message(message.from_id,
                                           f'Стоимость вашего билета {int(STANDARD_PRICE)}₽.\n\n'
                                           f'Переведите, пожалуйста, по номеру карты: {card_number}\n\n'
                                           f'После оплаты напишите {CONTACT_LINK}, прикрепите скрин оплаты и напишите свое ФИО. Вас внесут в список и узнают предпочтения. Спасибо!\n\n'
                                           f'ВНИМАНИЕ! Не забудьте паспорт!',
                                           reply_markup=types.ReplyKeyboardRemove())
            await state.finish()
        else:
            await message.bot.send_message(message.from_id,
                                           f'Стоимость ваших билетов {int(STANDARD_PRICE * int(state_data["amount"]) * 0.9)}₽.\n\n'
                                           f'Переведите, пожалуйста, по номеру карты: {card_number}\n\n'
                                           f'После оплаты напишите {CONTACT_LINK}, прикрепите скрин оплаты и напишите ФИО всех гостей. Вас внесут в список и узнаю предпочтения. Спасибо!\n\n'
                                           f'ВНИМАНИЕ! Не забудьте паспорт!',
                                           reply_markup=types.ReplyKeyboardRemove())
            await state.finish()


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start, lambda message: message.text in ('/start', 'Выход', 'В начало'))
    dp.register_message_handler(amount, lambda message: message.text in ('1', '2', '3', '4', '5', '6', '7'),
                                state=Steps.amount)
    dp.register_message_handler(discount, lambda message: message.text in ('Да', 'Нет', 'В начало'),
                                state=Steps.discount)
