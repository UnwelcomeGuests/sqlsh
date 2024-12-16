from sqlsh.remote_sqlite_handle import RemoteSqliteHandle
from sqlsh.remote_handler_validator import RemoteHandlerValidator

validator = RemoteHandlerValidator()

def get_remote_sqlite_file_handle(host, username, password, file_path) -> RemoteSqliteHandle:
    try:
        remote_handler = validator.validate_and_create_handler(
            hostname=host,
            username=username,
            password=password,
            remote_file_path=file_path
        )

        return remote_handler

    except Exception as e:
        raise e


