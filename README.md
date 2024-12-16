# SqlSH
_Simple SQLite database access over SSH_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Installation
```sh
pip install setup.py
```

## Usage
```python
import sqlsh

remote_handle = sqlsh.get_remote_sqlite_file_handle(
    host="host",
    username="username",
    password="password",
    remote_file_path="file_path"
)

remote_handle.query("select * from my_query;")
```

## Error Handling
```python
import sqlsh

try:
    remote_handle = sqlsh.get_remote_sqlite_file_handle(
        host="host",
        username="username",
        password="password",
        remote_file_path="file_path"
    )
except sqlsh.ConnectionFailed:
    # Raised when failed to connect to the remote machine via SSH
    
except sqlsh.SqliteNotInstalled:
    # Raised when sqlite is not installed on the remote machine
    
except sqlsh.RemoteFileNotExists:
    # Raised when the specified file doesn't exist on the remote machine
    
except sqlsh.FileNotDatabase:
    # Raised when the specified file isn't an sqlite database
```

## Documentation
TBD