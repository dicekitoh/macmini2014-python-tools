# GitHubへのプッシュ手順

## 1. GitHubでリポジトリ作成
1. https://github.com にアクセス
2. 右上の「+」→「New repository」
3. Repository name: `macmini2014-python-tools`
4. Description: `MacMini2014 Python環境一覧とツール管理`
5. Public/Private を選択
6. 「Create repository」をクリック（README追加はしない）

## 2. GitHubアクセストークン作成
1. GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 「Generate new token」→「Generate new token (classic)」
3. Note: `macmini2014-python-tools`
4. Expiration: 任意
5. Select scopes: `repo` にチェック
6. 「Generate token」をクリック
7. トークンをコピー（一度しか表示されない）

## 3. リモートリポジトリ追加とプッシュ
```bash
# リモートリポジトリを追加（YOUR_USERNAMEは自分のGitHubユーザー名）
git remote add origin https://github.com/YOUR_USERNAME/macmini2014-python-tools.git

# ブランチ名をmainに変更
git branch -M main

# プッシュ（ユーザー名とトークンを入力）
git push -u origin main
# Username: YOUR_USERNAME
# Password: YOUR_TOKEN（パスワードではなくトークン）
```

## 4. 今後の更新
```bash
# 変更をコミット
git add .
git commit -m "Update Python tools list"

# プッシュ
git push
```

## セキュリティ注意事項
- アクセストークンは絶対に共有しない
- トークンは環境変数や.envファイルで管理
- 不要になったトークンは削除する

## トークンを保存する場合（オプション）
```bash
# Git credentialヘルパーを設定
git config --global credential.helper store

# 初回プッシュ時に認証情報が保存される
git push -u origin main
```