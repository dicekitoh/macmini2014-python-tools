# MacMini2014 Python環境一覧

最終更新: 2025年6月9日

## システム情報
- **ホスト名**: macmini2014
- **OS**: Ubuntu 24.04.2 LTS
- **Python**: 3.12.3
- **pip**: 24.0

## インストール済みPythonツール一覧

### 1. 通信・メッセージングツール
| ファイル名 | 説明 | 用途 |
|-----------|------|-----|
| `telegram_working_bot.py` | Telegram BOT | メッセージ送受信、コマンド処理 |
| `telegram_chatgpt_bot.py` | ChatGPT連携BOT | AI対話機能 |
| `ssh_telegram_notifier.py` | SSH接続通知 | SSH接続時の自動通知 |
| `final_fax_system.py` | FAX送信システム | efax連携でFAX送信 |

### 2. 気象情報システム
| ファイル名 | 説明 | 用途 |
|-----------|------|-----|
| `weather_alert_ishikari_sorachi.py` | 石狩・空知地方気象警報 | 毎朝5:30に自動メール送信 |
| `improved_weather_alerts.py` | 改良版気象情報 | 詳細な気象情報取得 |
| `get_weather_alerts.py` | 基本気象情報 | シンプルな気象情報取得 |

### 3. メール・ブログシステム
| ファイル名 | 説明 | 用途 |
|-----------|------|-----|
| `email_blog/manual_blog_update.py` | メール→ブログ変換 | メール送信でブログ投稿 |
| `email_blog/blog_generator.py` | HTML生成 | ブログページ生成 |
| `email_blog/email_receiver.py` | メール受信処理 | Gmail IMAP連携 |
| `create_mail_draft.py` | メール下書き作成 | HTMLメール作成支援 |

### 4. 連絡先・データ管理
| ファイル名 | 説明 | 用途 |
|-----------|------|-----|
| `icloud_contacts_test.py` | iCloud連絡先連携 | 連絡先情報取得 |
| `get_uenishi_contact.py` | 特定連絡先検索 | 連絡先詳細取得 |
| `organize_gmail_afax.py` | Gmail整理 | メール自動整理 |
| `onedrive_organizer.py` | OneDriveファイル整理 | クラウドストレージ管理 |

### 5. システム管理・監視
| ファイル名 | 説明 | 用途 |
|-----------|------|-----|
| `get_full_system_status.py` | システム状態確認 | CPU/メモリ/ディスク監視 |
| `get_ip_info.py` | IPアドレス情報取得 | ネットワーク情報表示 |
| `mcp_todo_server_fixed.py` | MCP ToDoサーバー | タスク管理API |

## 主要Pythonライブラリ

### 通信・ネットワーク
- `boto3` - AWS SDK (S3, EC2等)
- `requests` - HTTP通信
- `urllib3` - HTTP通信（低レベル）
- `dnspython` - DNS操作

### セキュリティ・認証
- `cryptography` - 暗号化処理
- `PyJWT` - JWT認証
- `oauthlib` - OAuth認証
- `pyOpenSSL` - SSL/TLS処理

### データ処理
- `python-dateutil` - 日付処理
- `pytz` - タイムゾーン処理
- `PyYAML` - YAML処理
- `Markdown` - Markdown→HTML変換
- `Jinja2` - テンプレートエンジン
- `jsonschema` - JSONスキーマ検証

### 表示・UI
- `rich` - リッチテキスト表示
- `colorama` - ターミナル色表示
- `Pygments` - シンタックスハイライト
- `Babel` - 国際化・地域化

### ハードウェア・システム
- `pyserial` - シリアル通信（FAXモデム）
- `systemd-python` - systemd連携
- `dbus-python` - D-Bus通信

### その他
- `fail2ban` - セキュリティ（SSH保護）
- `cloud-init` - クラウドインスタンス初期化
- `unattended-upgrades` - 自動アップデート

## 仮想環境
- `/home/fujinosuke/onedrive_organizer/venv` - OneDrive整理ツール用
- `/home/fujinosuke/google_drive/venv` - Google Drive連携用

## 自動実行設定 (cron)
```cron
# 気象警報メール送信（毎朝5:30）
30 5 * * * /usr/bin/python3 /home/fujinosuke/weather_alert/weather_alert_ishikari_sorachi.py

# その他のcronジョブはCLAUDE.mdを参照
```

## 使用方法例

### メールでブログ投稿
```bash
# Claudeに「ブログ更新して」と伝える
python3 /home/fujinosuke/email_blog/manual_blog_update.py
```

### FAX送信
```bash
# Claudeに「FAXを送信して」と伝える
python3 /home/fujinosuke/final_fax_system.py <FAX番号> <ファイル>
```

### システム状態確認
```bash
python3 /home/fujinosuke/get_full_system_status.py
```

## 関連ドキュメント
- `/home/rootmax/CLAUDE.md` - Claude Code使用履歴と詳細記録
- 各プロジェクトのREADME.mdファイル

## 注意事項
- すべてのツールはMacMini2014 (Ubuntu 24.04.2 LTS) 上で動作
- 外部接続: SSH -p 2222 fujinosuke@126.217.45.148
- ローカル接続: SSH fujinosuke@192.168.3.43