from app import app

groups = {
    'linux-server': 'query.list-linux-servers',
}


@app.task(name='common.get-information', ignore_result=True)
def get_information(task_group):
    try:
        task_name = groups[task_group]
        print(task_name)
    except KeyError as ex:
        print('No corresponding task with group {}'.format(task_group))


# @app.task('common.schedule')
# def schedule(task_name, identity):
#     signature = app.signature(task_name, args=[identity])
#     return None
