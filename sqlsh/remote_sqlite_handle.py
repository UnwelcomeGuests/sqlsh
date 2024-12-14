import paramiko
from paramiko.client import SSHClient

class RemoteSqliteHandle(SSHClient):
    def __init__(self, hostname: str, username: str, password: str, remote_file_path: str):
        super().__init__()
        self._hostname: str = hostname
        self._username: str = username
        self._password: str = password
        self._remote_file_path: str = remote_file_path
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    @classmethod
    def from_ssh_client(cls, ssh_client):
        pass


    def _connect(self):
        try:
            self.connect(hostname=self._hostname, username=self._username, password=self._password)
        except Exception as e:
            print(f"Failed to connect to remote server: {e}")
            raise ConnectionFailed

        print(f"Connected to remote server!")


    def _check_remote_file_existence(self) -> bool:
        pass

    def _check_remote_sqlite3_existence(self) -> bool:
        pass
