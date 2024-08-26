from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

status_user = 'Мыслитель' #TODO delete when us DB

class Old_User(StatesGroup):
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


user_old_router = Router()

@user_old_router.message(Command('second'))
async def start(message: Message):
    # TODO connect to search id user in DB
    if message.from_user.id == 5852798350:
        # TODO search status_user in DB
        await message.answer(f'Привет, {status_user}')
    else:
        await message.answer('Вы не зарегистрированы в нашей системе. Если у вас есть реферальная ссылки выберете в меню "/first')



