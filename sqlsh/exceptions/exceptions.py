
class RemoteFileNotExists(BaseException):
    """Raise when specified remote file path doesn't exist"""

class ConnectionFailed(BaseException):
    """Raise when failed to connect to remote server via SSH"""

class SqliteNotInstalled(BaseException):
    """Raise when sqlite3 is not installed on the remote server"""

class FileNotDatabase(BaseException):
    """Raise when the remote file is not a sqlite3 database"""