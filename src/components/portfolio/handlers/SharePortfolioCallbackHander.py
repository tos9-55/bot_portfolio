from aiogram.types import CallbackQuery


class SharePortfolioCallbackHandler:

    async def __call__(self, call: CallbackQuery):
        await call.answer()

        portfolio_id = int(call.data.split("_")[-1])

        bot_username = (await call.bot.get_me()).username
        start_param = f"portfolio_{portfolio_id}"
        deep_link = f"https://t.me/{bot_username}?start={start_param}"

        await call.message.answer(f"🔗 Вот ссылка для вашего портфолио:\n{deep_link}")