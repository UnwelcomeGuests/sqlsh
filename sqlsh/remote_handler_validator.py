import paramiko
from paramiko.client import SSHClient
from paramiko.ssh_exception import AuthenticationException
from sqlsh.exceptions.exceptions import RemoteFileNotExists, ConnectionFailed, SqliteNotInstalled, FileNotDatabase
from sqlsh.remote_sqlite_handle import RemoteSqliteHandle
from enum import Enum

SQLITE3 = "sqlite3"
COMMAND_NOT_FOUND_ERROR = "command not found"
FILE_IS_NOT_A_DATABASE = "file is not a database"

TEST_FILE_QUERY = "select * from hello_world;"


class SqliteValidationResult(Enum):
    INSTALLED = 0
    NOT_INSTALLED = 1
    FILE_NOT_DATABASE = 2


class RemoteHandlerValidator:
    def validate_and_create_handler(
            self, hostname: str,
            username: str,
            password: str,
            remote_file_path: str
    ) -> RemoteSqliteHandle:

        try:
            remote_connection: SSHClient = self._validate_remote_connection(hostname=hostname, username=username, password=password)
        except Exception as e:
            raise e

        if not self._validate_file_existence(remote_connection, remote_file_path):
            raise RemoteFileNotExists


        validation_result: SqliteValidationResult = self._validate_sqlite3(remote_connection, remote_file_path)
        match validation_result:
            case SqliteValidationResult.NOT_INSTALLED:
                raise SqliteNotInstalled

            case SqliteValidationResult.FILE_NOT_DATABASE:
                raise FileNotDatabase


        return RemoteSqliteHandle.from_ssh_client(remote_connection, remote_file_path)


    @classmethod
    def _validate_remote_connection(cls, hostname: str, username: str, password: str) -> SSHClient:
        client = SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(hostname, username=username, password=password)
            return client
        except AuthenticationException:
            raise ConnectionFailed


    @classmethod
    def _validate_sqlite3(cls, ssh_client: SSHClient, file_path: str) -> SqliteValidationResult:
        stdin, stdout, stderr = ssh_client.exec_command(f"{SQLITE3} {file_path} \"{TEST_FILE_QUERY}\"")

        error_output = stderr.read().decode()

        if COMMAND_NOT_FOUND_ERROR in error_output:
            return SqliteValidationResult.NOT_INSTALLED

        if FILE_IS_NOT_A_DATABASE in error_output:
            return SqliteValidationResult.FILE_NOT_DATABASE


    @classmethod
    def _validate_file_existence(cls, ssh_client: SSHClient, remote_file_path: str) -> bool:
        sftp = ssh_client.open_sftp()

        try:
            sftp.stat(remote_file_path)
            return True
        except FileNotFoundError:
            return False


