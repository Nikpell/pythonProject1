
from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

user_id = 0

class Registration(StatesGroup):
    #Шаги состояний
    name = State()
    link = State()
    old = State()
    job = State()
    kind_job = State()

    texts = {
        'Registration:name': 'Как к вам обращаться(введите пожалуйста имя, фамилию):',
        'Registration:link': 'Как с Вами связаться? (телефон/почта)',
        'Registration:old': 'Укажите Ваш возраст:',
        'Registration:job': 'Укажите Вашу занятость: (Не работаю, Работаю, Предприниматель)',
        'Registration:kind_job': 'Укажите сферу вашей деятельности: ',
    }


user_new_router = Router()

@user_new_router.message(Command('first'))
async def cmd_start(message: Message):
    # TODO connect to search id user in DB
    if message.from_user.id != 5852798351:
        user_id = message.from_user.id
        await message.answer(f"{message.from_user.full_name}. Вас приветствует БОТ-Ассистент Разговорников!"
                         "Данное пространство - ваша точка соприкосновения "
                         "с загадочной игрой, которая уже началась в Разговорниках. "
                         "Чтобы пройти дальше, отправьте реферальный код от члена разговорников,"
                         " который Вас пригласил")

@user_new_router.message(StateFilter(None), F.text.contains('inv')) #Префикс для обнаружение ссылки
async def refferal_cod(message: Message, state: FSMContext):
    # TODO from DB search refferal code,  invite name
    invite_name = 'Имя Фамилия'
    if message.text == 'inv123':  # TODO and user_id == message.from_user.id:
        await message.answer(f"Отлично! Вас пригласил {invite_name}, поздравляю с входом в наше сообщество! "
                             f"После регистрации Вы сможете добавить другие социальные связи в Разговорниках!")
        await message.answer('Как к вам обращаться(введите пожалуйста имя, фамилию через пробел): ')
        await state.set_state(Registration.name)
    else:
        await message.answer('Такого реферельного кода не существует')

@user_new_router.message(Registration.name, F.text)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        text="Спасибо. Как с Вами связаться? (введите телефон/почту): "
    )
    await state.set_state(Registration.link)

@user_new_router.message(Registration.link, F.text)
async def old(message: Message, state: FSMContext):
    await state.update_data(link=message.text)
    await message.answer(
        text="Спасибо. Укажите Ваш возраст: "
    )
    await state.set_state(Registration.old)

@user_new_router.message(Registration.old, F.text)
async def old(message: Message, state: FSMContext):
    await state.update_data(old=message.text)
    await message.answer(
        text="Спасибо. Укажите Вашу занятость: (Не работаю, Работаю, Предприниматель)"
    )
    await state.set_state(Registration.job)

@user_new_router.message(Registration.job, F.text)
async def old(message: Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer(
        text="Спасибо. Укажите сферу вашей деятельности: "
    )
    await state.set_state(Registration.kind_job)


@user_new_router.message(Registration.kind_job, F.text)
async def old(message: Message, state: FSMContext):
    await state.update_data(kind_job=message.text)
    await message.answer(
        text="Спасибо. Вы завершили регистрацию. Для в кнопке меню выберете '/second'"
    )
    user_data = await state.get_data()
    user_data.update({'user_id': message.from_user.id})
    #  TODO Transfer user_data to DB
    await state.clear()
