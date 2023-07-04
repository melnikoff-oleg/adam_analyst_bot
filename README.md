# adam_analyst_bot
Bot that can analyse tabular data and come up with business insights.

How to use:
- create .env file and paste write your tokens there: TELEGRAM_BOT_TOKEN=..., OPENAI_API_TOKEN=...
- docker build --tag adam_analyst_bot .
- docker run adam_analyst_bot python3 bot.py