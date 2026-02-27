local_resource(
    'app',
    serve_cmd='bash -lc "source .venv/bin/activate && uvicorn app.main:app --host {host} --port 8000 --reload"'.format(
        host=os.getenv('MTS_UVICORN_HOST', '127.0.0.1'),
    ),
    deps=[
        'app',
        'templates',
        'requirements.txt',
        '.env.example',
    ],
)
