#!/bin/bash
python3 -m app.database.seeder 2>/dev/null || true
python3 -m app.bot.bot
