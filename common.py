from app import app
from celery.canvas import chain
from celery.canvas import group

groups = {
    'linux-server': 'query.list-linux-servers',
}


@app.task(name='common.just-print')
def just_print(something):
    print(something)


@app.task(name='common.get-information')
def get_information(task_group):
    try:
        task_name = groups[task_group]
        pipeline = chain(
            app.signature(task_name),  # Query list of objects
            create_task.s(task_name),
        )
        pipeline()
    except KeyError as ex:
        print('No corresponding task with group {}'.format(task_group))


@app.task(name='common.create-task')
def create_task(ids, task_name):
    try:
        for id in ids:
            app.signature('common.just-print', args=[id]).delay()
    except TypeError as ex:
        print('Input "{}" is not a list'.format(ids))
