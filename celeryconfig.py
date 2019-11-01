broker_url = 'redis://127.0.0.1:6379'
result_backend = 'redis://127.0.0.1:6379'

imports = [
    'common',
    'query.tasks',
    'hello.tasks',
]

beat_schedule = {
    'auto-get-linux-server-information': {
        'task': 'common.get-information',
        'schedule': 10,
        'args': ('linux-server',)
    }
}
