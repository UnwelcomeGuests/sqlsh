from paramiko.client import SSHClient
from sqlsh.remote_sqlite_handle import RemoteSqliteHandle
from enum import Enum

class RemoteHandlerValidatorError(Enum):
    CONNECTION_FAILED = 1
    FILE_NOT_EXISTS = 2


class RemoteHandlerValidator:
    def validate_and_create_handler(
            self, hostname: str,
            username: str,
            password: str,
            remote_file_path: str
    ) -> RemoteSqliteHandle | RemoteHandlerValidatorError:
        # validate...

        try:
            remote_connection: SSHClient = self._validate_remote_connection(hostname=hostname, username=username, password=password)
        except Exception as e:
            return RemoteHandlerValidatorError.CONNECTION_FAILED

        if self._validate_file_existence(remote_connection, remote_file_path):
            return RemoteSqliteHandle.from_ssh_client(remote_connection)

        else:
            return RemoteHandlerValidatorError.FILE_NOT_EXISTS


    @classmethod
    def _validate_remote_connection(cls, hostname: str, username: str, password: str) -> SSHClient:
        pass

    @classmethod
    def _validate_file_existence(cls, ssh_client: SSHClient, remote_file_path: str) -> bool:
        return True
