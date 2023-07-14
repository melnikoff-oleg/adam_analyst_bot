from aiogram import Dispatcher, types


async def set_bot_commands(dp: Dispatcher) -> None:
    commands = [
        types.BotCommand(command="start", description="Запустить бота"),
        types.BotCommand(command="cancel", description="Отмена"),
        types.BotCommand(command="change", description="Изменить набор данных"),
    ]

    await dp.bot.set_my_commands(commands)
