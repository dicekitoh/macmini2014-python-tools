#!/usr/bin/env python3
"""
Vehicle Info Scraper BOT テストスクリプト
"""

import requests
import sys

# 新しいBOTトークン
BOT_TOKEN = "7550789226:AAHn5q54tpb4LBsvW0EH0_1RtxJyEpK-fuk"

def test_bot_token():
    """BOTトークンの有効性テスト"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
    
    try:
        response = requests.get(url, timeout=5)
        result = response.json()
        
        if result['ok']:
            bot_info = result['result']
            print(f"✅ BOT作成成功!")
            print(f"   ID: {bot_info['id']}")
            print(f"   ユーザー名: @{bot_info['username']}")
            print(f"   名前: {bot_info['first_name']}")
            print(f"   URL: https://t.me/{bot_info['username']}")
            return bot_info
        else:
            print(f"❌ BOTトークンエラー: {result}")
            return None
            
    except Exception as e:
        print(f"❌ 接続エラー: {e}")
        return None

def send_test_message(chat_id):
    """テストメッセージ送信"""
    message = """
🎉 <b>Vehicle Info Scraper BOT 稼働開始!</b>

🚗 車両情報スクレイピングBOT
📅 作成日時: 2025年6月9日
🖥️ 送信元: rootmax環境
✨ ステータス: 正常動作中

<i>オークションサポートのURLから車両情報を自動抽出します!</i>
    """.strip()
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    
    try:
        response = requests.post(url, data=data, timeout=10)
        result = response.json()
        
        if result['ok']:
            print(f"✅ メッセージ送信成功!")
            return True
        else:
            print(f"❌ 送信エラー: {result.get('description')}")
            return False
            
    except Exception as e:
        print(f"❌ 送信エラー: {e}")
        return False

def main():
    print("🚗 Vehicle Info Scraper BOT テスト")
    print("=" * 50)
    
    # BOT情報テスト
    bot_info = test_bot_token()
    if not bot_info:
        return
    
    print(f"\n🎯 BOT準備完了")
    print(f"   次のステップ:")
    print(f"   1. Telegramで @{bot_info['username']} を開く")
    print(f"   2. /start コマンドを送信")
    print(f"   3. チャットIDを取得してテスト送信")
    
    # 設定を保存
    with open('/home/rootmax/vehicle_scraper_bot_config.txt', 'w') as f:
        f.write(f"BOT_TOKEN={BOT_TOKEN}\n")
        f.write(f"BOT_ID={bot_info['id']}\n")
        f.write(f"BOT_USERNAME=@{bot_info['username']}\n")
        f.write(f"BOT_NAME={bot_info['first_name']}\n")
        f.write(f"STATUS=configured\n")
    
    print(f"\n📋 設定保存完了: vehicle_scraper_bot_config.txt")

if __name__ == "__main__":
    main()