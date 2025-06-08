#!/usr/bin/env python3
"""
Vehicle Info Scraper BOT - 車両情報スクレイピングBOT
オークションサポートのURLから車両情報を抽出
"""

import requests
import re
from datetime import datetime
import logging
from urllib.parse import urlparse, parse_qs

# BOT設定
BOT_TOKEN = "7550789226:AAHn5q54tpb4LBsvW0EH0_1RtxJyEpK-fuk"
BOT_NAME = "Vehicle Info Scraper"

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/vehicle_bot.log'),
        logging.StreamHandler()
    ]
)

class VehicleInfoBot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.last_update_id = 0
    
    def get_updates(self):
        """メッセージを取得"""
        url = f"{self.base_url}/getUpdates"
        params = {
            'offset': self.last_update_id + 1,
            'timeout': 30
        }
        
        try:
            response = requests.get(url, params=params, timeout=35)
            data = response.json()
            
            if data['ok']:
                return data['result']
            else:
                logging.error(f"API Error: {data}")
                return []
        except Exception as e:
            logging.error(f"Get updates error: {e}")
            return []
    
    def send_message(self, chat_id, text, parse_mode='HTML'):
        """メッセージ送信"""
        url = f"{self.base_url}/sendMessage"
        data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': parse_mode
        }
        
        try:
            response = requests.post(url, data=data, timeout=10)
            result = response.json()
            
            if result['ok']:
                logging.info(f"Message sent to {chat_id}")
                return True
            else:
                logging.error(f"Send error: {result}")
                return False
        except Exception as e:
            logging.error(f"Send message error: {e}")
            return False
    
    def extract_vehicle_info_from_url(self, url):
        """URLから車両情報を抽出"""
        try:
            # URLパラメータを解析
            parsed_url = urlparse(url)
            params = parse_qs(parsed_url.query)
            
            # 基本情報を抽出
            maker = params.get('MAKER', [''])[0]
            car_name = params.get('CARNAME', [''])[0]
            katashiki = params.get('KATASHIKI', [''])[0]
            syear = params.get('SYEAR', [''])[0]
            eyear = params.get('EYEAR', [''])[0]
            skm = params.get('SKM', [''])[0]
            ekm = params.get('EKM', [''])[0]
            
            # URLデコード
            import urllib.parse
            maker = urllib.parse.unquote(maker)
            car_name = urllib.parse.unquote(car_name)
            katashiki = urllib.parse.unquote(katashiki)
            
            # 車両情報フォーマット
            vehicle_info = {
                'url': url,
                'maker': maker or '不明',
                'car_name': car_name or '不明',
                'katashiki': katashiki or '不明',
                'year_start': syear or '不明',
                'year_end': eyear or '不明',
                'km_start': skm or '不明',
                'km_end': ekm or '不明'
            }
            
            return vehicle_info
            
        except Exception as e:
            logging.error(f"URL parsing error: {e}")
            return None
    
    def create_short_url(self, url):
        """URL短縮サービスを使用（is.gd）"""
        try:
            short_api = "https://is.gd/create.php"
            params = {'format': 'simple', 'url': url}
            
            response = requests.get(short_api, params=params, timeout=5)
            if response.status_code == 200 and response.text.startswith('https://'):
                return response.text.strip()
            else:
                return None
        except Exception as e:
            logging.error(f"URL shortening error: {e}")
            return None
    
    def shorten_url_display(self, url):
        """URLを短縮表示（リンク切れ回避）"""
        if len(url) <= 50:
            return url
        
        # まずURL短縮サービスを試行
        short_url = self.create_short_url(url)
        if short_url:
            return f"{short_url} (短縮URL)"
        
        # 短縮サービス失敗時はパラメータ表示
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        # 重要パラメータのみ表示
        maker = params.get('MAKER', [''])[0]
        car_name = params.get('CARNAME', [''])[0]
        
        if maker or car_name:
            import urllib.parse
            maker = urllib.parse.unquote(maker)[:10]
            car_name = urllib.parse.unquote(car_name)[:10]
            return f"aucsupport.com/?{maker}_{car_name}..."
        else:
            return f"{parsed.netloc}/...({len(url)}文字)"
    
    def format_vehicle_message(self, info):
        """車両情報をメッセージ形式に整形"""
        if not info:
            return "❌ 車両情報の抽出に失敗しました"
        
        # URL短縮表示
        short_url = self.shorten_url_display(info['url'])
        
        message = f"""
🚗 <b>車両情報抽出結果</b>

📎 <b>URL:</b> {short_url}

🏭 <b>メーカー:</b> {info['maker']}
🚙 <b>車種:</b> {info['car_name']}
🔧 <b>型式:</b> {info['katashiki']}

📅 <b>年式:</b> {info['year_start']}年 ～ {info['year_end']}年
🛣️ <b>走行距離:</b> {info['km_start']}千km ～ {info['km_end']}千km

⏰ <b>抽出日時:</b> {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}

<i>車両情報を正常に抽出しました</i>
        """.strip()
        
        return message
    
    def handle_start_command(self, chat_id):
        """startコマンドの処理"""
        welcome_message = f"""
🎉 <b>{BOT_NAME} へようこそ!</b>

🚗 このBOTは車両情報を自動抽出します

<b>簡単な使い方:</b>
1. <b>「スクレイピング」</b> と送信
2. URLの入力を求められます
3. オークションサポートのURLを送信
4. 車両情報が自動的に抽出されます

<b>対応URL例:</b>
https://www.aucsupport.com/soubalist.aspx?...

<b>抽出情報:</b>
• メーカー・車種
• 型式・年式
• 走行距離範囲
• その他詳細情報

✨ 「スクレイピング」と送信してお試しください!
        """.strip()
        
        self.send_message(chat_id, welcome_message)
    
    def handle_url_message(self, chat_id, text):
        """URL処理"""
        # オークションサポートURLかチェック
        if 'aucsupport.com' in text and 'soubalist.aspx' in text:
            logging.info(f"Processing auction URL from {chat_id}")
            
            # 車両情報抽出
            vehicle_info = self.extract_vehicle_info_from_url(text)
            response = self.format_vehicle_message(vehicle_info)
            
            self.send_message(chat_id, response)
        else:
            # 不正なURL
            error_message = """
❌ <b>未対応のURLです</b>

対応URL:
• オークションサポート (aucsupport.com)
• soubalist.aspx を含むURL

正しいURLを送信してください。
            """.strip()
            
            self.send_message(chat_id, error_message)
    
    def handle_scraping_command(self, chat_id):
        """スクレイピングコマンドの処理"""
        request_message = """
📎 <b>URLを送信してください</b>

オークションサポートのURLを貼り付けて送信
        """.strip()
        
        self.send_message(chat_id, request_message)
    
    def process_message(self, message):
        """メッセージ処理"""
        chat_id = message['chat']['id']
        text = message.get('text', '').strip()
        
        if text.startswith('/start'):
            self.handle_start_command(chat_id)
        elif text == 'スクレイピング' or text.lower() == 'scraping':
            self.handle_scraping_command(chat_id)
        elif 'http' in text:
            self.handle_url_message(chat_id, text)
        else:
            # ヘルプメッセージ
            help_message = """
🤖 <b>Vehicle Info Scraper BOT</b>

使用方法:
• /start - ヘルプ表示
• <b>スクレイピング</b> - URL入力を開始
• URLを直接送信 - 車両情報抽出

<b>簡単な使い方:</b>
「スクレイピング」と送信 → URLを聞かれる → URL送信

対応サイト:
• オークションサポート
            """.strip()
            
            self.send_message(chat_id, help_message)
    
    def run(self):
        """BOT実行"""
        logging.info(f"{BOT_NAME} 開始")
        
        while True:
            try:
                updates = self.get_updates()
                
                for update in updates:
                    self.last_update_id = update['update_id']
                    
                    if 'message' in update:
                        self.process_message(update['message'])
                
            except KeyboardInterrupt:
                logging.info("BOT停止")
                break
            except Exception as e:
                logging.error(f"Main loop error: {e}")
                continue

def main():
    print(f"🚗 {BOT_NAME} 起動中...")
    print(f"📱 Telegram: @VehicleInfoScraper_bot")
    print(f"📝 ログ: /tmp/vehicle_bot.log")
    print()
    
    bot = VehicleInfoBot(BOT_TOKEN)
    bot.run()

if __name__ == "__main__":
    main()