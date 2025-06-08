# GitHubアクセストークン作成手順

GitHubは2021年8月13日以降、パスワード認証を廃止しました。
代わりにパーソナルアクセストークン（PAT）を使用する必要があります。

## トークン作成手順

1. **GitHubにログイン**
   - https://github.com にアクセス
   - ユーザー名: dicekitoh
   - パスワードでログイン

2. **アクセストークンページへ**
   - 右上のプロフィールアイコンをクリック
   - Settings → Developer settings → Personal access tokens → Tokens (classic)
   - または直接: https://github.com/settings/tokens

3. **新しいトークンを生成**
   - 「Generate new token」→「Generate new token (classic)」をクリック
   - GitHubパスワードを再入力

4. **トークン設定**
   - **Note**: macmini2014-python-tools
   - **Expiration**: 90 days（または任意）
   - **Select scopes**: 
     - ✅ repo（すべてにチェック）
     - その他は不要

5. **トークン生成**
   - 「Generate token」をクリック
   - **重要**: トークンをコピー（一度しか表示されません！）

## トークンを使用してプッシュ

```bash
# トークンを使用してプッシュ
git push https://dicekitoh:YOUR_TOKEN_HERE@github.com/dicekitoh/macmini2014-python-tools.git main

# または対話式で
git push -u origin main
# Username: dicekitoh
# Password: [トークンを貼り付け]
```

## セキュリティ注意

- トークンはパスワードと同様に扱う
- 他人と共有しない
- 定期的に更新する
- 不要になったら削除する

## トークン例
`ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
（ghp_で始まる40文字の文字列）