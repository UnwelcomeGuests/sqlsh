from paramiko.client import SSHClient

SQLITE3 = "sqlite3"

class RemoteSqliteHandle(SSHClient):
    @classmethod
    def from_ssh_client(cls, ssh_client, remote_file_path):
        handle = cls.__new__(cls)
        handle.__dict__ = ssh_client.__dict__
        handle._remote_file_path = remote_file_path

        return handle

    def query(self, query) -> str:
        stdin, stdout, stderr = self.exec_command(f"{SQLITE3} {self._remote_file_path} \"{query}\"")
        output = stdout.read().decode()
        error = stderr.read().decode()

        if error: return error
        return output
