import time
from typing import Callable, Awaitable
from data_analyst import use_data_assistant
from aiogram import types


async def process_query(data_path: str, data_description: str, question: str) -> str:
    return use_data_assistant(
        data_path,
        data_description=data_description,
        question=question,
    )
