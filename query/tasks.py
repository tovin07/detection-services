from app import app


@app.task(name='query.list-linux-servers')
def list_linux_servers(offset=0, limit=100):
    return list(range(10))
