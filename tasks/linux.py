from celery.canvas import chain

from app import app


@app.task(name='linux.main')
def main():
    chain(
        get_list_of_servers.s(),
        get_connection_information.s(),
        gather_server_information.s(),
        # transform.s(),
        # update_server_information.s(),
    )()


@app.task(name='linux.get-list-of-servers')
def get_list_of_servers():
    return [1, 2, 3, 4]


@app.task(name='linux.get-connection-information')
def get_connection_information(server_id):
    return {
        'ip': '10.240.232.22',
        'user': 'centos',
        'password': 'devops@Cloud2019'
    }


@app.task(name='linux.gather-server-information')
def gather_server_information(connection_info):
    return {'result': 'something'}


@app.task(name='linux.transform')
def transform(server_info):
    return {'result': 'something after transform'}


@app.task(name='linux.update-server-information')
def update_server_information(result):
    print('Result is "{}"'.format(result['result']))
