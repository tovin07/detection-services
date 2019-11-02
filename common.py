from app import app

groups = {
    'linux': 'linux.main',
}


@app.task(name='common.get-information')
def get_information(task_group):
    try:
        app.signature(groups[task_group]).delay()
    except KeyError as ex:
        print('No corresponding task with group {}'.format(task_group))
        raise
