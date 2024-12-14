import paramiko
from paramiko.client import SSHClient

from sqlsh.remote_sqlite_handle import RemoteSqliteHandle
from sqlsh.remote_handler_validator import RemoteHandlerValidator

validator = RemoteHandlerValidator()

def get_remote_sqlite_file_handle(host, username, password, file_path) -> RemoteSqliteHandle:
    remote_handler = None

    try:
        remote_handler = validator.validate_and_create_handler(

        )
    except Exception as e:
        pass

    return remote_handler

