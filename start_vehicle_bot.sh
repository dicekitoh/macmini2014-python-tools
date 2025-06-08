#!/bin/bash
"""
Vehicle Info Scraper BOT 起動スクリプト
"""

echo "🚗 Vehicle Info Scraper BOT 起動"
echo "================================"
echo "BOT名: @VehicleInfoScraper_bot"
echo "機能: 車両情報スクレイピング"
echo "ログ: /tmp/vehicle_bot.log"
echo ""

# Python仮想環境があれば使用
if [ -d "/home/rootmax/telegram_bot_env" ]; then
    echo "📦 仮想環境を使用"
    source /home/rootmax/telegram_bot_env/bin/activate
fi

# BOT起動
python3 /home/rootmax/vehicle_info_scraper_bot.py