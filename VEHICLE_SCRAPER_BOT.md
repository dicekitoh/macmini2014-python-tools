# Vehicle Info Scraper BOT

最終更新: 2025年6月9日

## 概要
オークションサポートのURLから車両情報を自動抽出するTelegram BOTです。

## BOT情報
- **BOT名**: Vehicle Info Scraper
- **ユーザー名**: @VehicleInfoScraper_bot
- **URL**: https://t.me/VehicleInfoScraper_bot
- **ID**: 7550789226

## 主要機能

### 1. 簡単操作
```
ユーザー: スクレイピング
BOT: 📎 URLを送信してください
     オークションサポートのURLを貼り付けて送信

ユーザー: [URL送信]
BOT: 🚗 車両情報抽出結果
     🏭 メーカー: トヨタ
     🚙 車種: プリウス
     ...
```

### 2. URL短縮機能
- **is.gd短縮サービス使用**
- **リンク切れ回避**
- **Telegram表示最適化**

### 3. 抽出可能情報
- メーカー・車種
- 型式・年式
- 走行距離範囲
- URL短縮表示

## 使用方法

### 基本操作
1. **Telegramで @VehicleInfoScraper_bot を開く**
2. **「スクレイピング」と送信**
3. **オークションサポートのURLを送信**
4. **車両情報が自動抽出される**

### コマンド一覧
| コマンド | 説明 |
|---------|------|
| `/start` | ヘルプ表示 |
| `スクレイピング` | URL入力開始 |
| `scraping` | URL入力開始（英語） |
| URL直接送信 | 車両情報抽出 |

## ファイル構成

### メインファイル
- `vehicle_info_scraper_bot.py` - メインBOTスクリプト
- `start_vehicle_bot.sh` - 起動スクリプト
- `vehicle_scraper_bot_test.py` - テストスクリプト

### 設定ファイル
- `vehicle_scraper_bot_config.txt` - BOT設定
- BOTトークン: 7550789226:AAHn5q54tpb4LBsvW0EH0_1RtxJyEpK-fuk

## 起動方法

### 手動起動
```bash
# 起動スクリプト使用
./start_vehicle_bot.sh

# 直接実行
python3 vehicle_info_scraper_bot.py

# バックグラウンド実行
nohup python3 vehicle_info_scraper_bot.py > /tmp/vehicle_bot_output.log 2>&1 &
```

### プロセス管理
```bash
# プロセス確認
ps aux | grep vehicle_info_scraper_bot

# プロセス停止
pkill -f vehicle_info_scraper_bot
```

## 技術仕様

### URL解析
```python
# URLパラメータ抽出
parsed_url = urlparse(url)
params = parse_qs(parsed_url.query)

# 車両情報抽出
maker = params.get('MAKER', [''])[0]
car_name = params.get('CARNAME', [''])[0]
katashiki = params.get('KATASHIKI', [''])[0]
```

### URL短縮
```python
# is.gd短縮サービス
short_api = "https://is.gd/create.php"
params = {'format': 'simple', 'url': url}
response = requests.get(short_api, params=params)
```

### エラーハンドリング
- ネットワークエラー対応
- URL解析エラー処理
- Telegram API エラー処理
- ログ記録機能

## ログ管理

### ログファイル
- `/tmp/vehicle_bot.log` - メインログ
- `/tmp/vehicle_bot_output.log` - 出力ログ

### ログ確認
```bash
# リアルタイムログ
tail -f /tmp/vehicle_bot.log

# 最新ログ
tail -20 /tmp/vehicle_bot.log
```

## 対応サイト
- **オークションサポート** (aucsupport.com)
- soubalist.aspx を含むURL

## テスト用URL
```
https://www.aucsupport.com/soubalist.aspx?MAKER=%E3%83%88%E3%83%A8%E3%82%BF&CARNAME=%E3%83%97%E3%83%AA%E3%82%A6%E3%82%B9&KATASHIKI=ZVW30&SYEAR=2016&EYEAR=2020&SKM=50&EKM=100
```

## 返信例
```
🚗 車両情報抽出結果

📎 URL: https://is.gd/abc123 (短縮URL)

🏭 メーカー: トヨタ
🚙 車種: プリウス
🔧 型式: ZVW30

📅 年式: 2016年 ～ 2020年
🛣️ 走行距離: 50千km ～ 100千km

⏰ 抽出日時: 2025年06月09日 07:43:02

車両情報を正常に抽出しました
```

## トラブルシューティング

### BOTが応答しない
1. プロセス確認: `ps aux | grep vehicle_info_scraper_bot`
2. ログ確認: `tail -f /tmp/vehicle_bot.log`
3. 再起動: `./start_vehicle_bot.sh`

### URL短縮エラー
- is.gdサービス障害時は自動でパラメータ表示に切り替え
- ネットワーク接続確認

### 情報抽出エラー
- URLフォーマット確認
- オークションサポートサイト構造変更の可能性

## 更新履歴

### 2025年6月9日
- ✅ BOT作成・基本機能実装
- ✅ 「スクレイピング」コマンド追加
- ✅ URL短縮機能追加（is.gd）
- ✅ シンプルなURL要求メッセージ
- ✅ リンク切れ回避機能