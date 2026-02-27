# MTS - Google Login (Python + FastAPI)

Google アカウントでログインする最小構成の FastAPI アプリです。認証は Google OpenID Connect、セッション管理は Starlette、ユーザー情報の永続化は SQLAlchemy を使います。

## セットアップ

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

## 必須環境変数

`.env` に以下を設定します。

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `SESSION_SECRET`
- `DATABASE_URL`
- `APP_BASE_URL`

ローカルでまず動かすだけなら、`DATABASE_URL=sqlite+pysqlite:///./app.db` でも構いません。PostgreSQL を使う場合は `.env.example` の接続文字列をベースにしてください。

## Google Cloud Console の設定

1. Google Cloud でプロジェクトを作成します。
2. `APIs & Services` で OAuth 同意画面を設定します。
3. `Credentials` で `OAuth client ID` を作成します。
4. アプリ種別は `Web application` を選びます。
5. Authorized redirect URI に `http://127.0.0.1:8000/auth/google/callback` を登録します。
6. 発行された Client ID / Client Secret を `.env` に入れます。

## 起動

```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

ブラウザで `http://127.0.0.1:8000` を開き、`Googleでログイン` を押して動作確認します。

## テスト

```bash
source .venv/bin/activate
pytest -q
```

## リポジトリ構成

- `app/main.py`: FastAPI アプリとミドルウェアの設定
- `app/auth/google.py`: Google OAuth2.0 / OIDC のログイン処理
- `app/routes/web.py`: トップ画面と `/me`
- `app/models/`: `users` と `oauth_accounts`
- `templates/index.html`: 最小 UI
- `Tiltfile`: ローカル開発用の起動設定
