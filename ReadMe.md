# MTS - Google Login (Python + FastAPI)

Googleアカウントでログインする最小実装です。永続化には PostgreSQL を利用できます。

## 1. venv の作成

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 2. 環境変数

```bash
cp .env.example .env
```

`.env` の以下を必ず設定してください。

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `SESSION_SECRET`
- `DATABASE_URL`（PostgreSQL 接続文字列）
- `APP_BASE_URL`（ローカルは `http://127.0.0.1:8000`）

Google Cloud Console 側で、OAuth のリダイレクトURIに
`http://127.0.0.1:8000/auth/google/callback` を登録します。

## 3. 起動

```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

`http://127.0.0.1:8000` を開いてログインを試してください。

## 4. テスト

```bash
source .venv/bin/activate
pytest -q
```
