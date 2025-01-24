import os
import subprocess
from typing import Annotated
from ..commands import command, CommandsManager

class Restic:

    # vars
    _repository: str
    _repository_password: str
    _aws_access_key_id: str
    _aws_secret_access_key: str
    _data_base_path: str
    _data_path: str
    _restore_path: str
    _restic_path: str
    
    # ctor
    def __init__(self, repository: str, repository_password: str, aws_access_key_id: str, aws_secret_access_key: str, data_base_path: str, data_path: str, restore_path: str, restic_path: str = ""):
        self._repository = repository
        self._repository_password = repository_password
        self._aws_access_key_id = aws_access_key_id
        self._aws_secret_access_key = aws_secret_access_key

        self._data_base_path = data_base_path
        if self._data_base_path == "":
            self._data_base_path = os.getcwd()

        self._data_path = data_path

        self._restore_path = restore_path

        if restic_path == "":
            self._restic_path = "restic"
        else:
            self._restic_path = os.path.abspath(restic_path)

        print(self._data_base_path)
        print(self._restic_path)

    # commands
    @command("Init repository", index = 1)
    def init(self):
        return self._runRestic("init")

    @command("Backup ", index = 10)
    def backup(self):
        return self._runRestic("backup {0} --verbose".format(" ".join(self._data_path)))

    @command("List snapshots ", index = 20)
    def snapshots_list(self):
        return self._runRestic("snapshots")
    
    @command("List snapshot contents")
    def snapshots_contents(self, 
            id: Annotated[str, "ID"]
        ):
        return self._runRestic("ls {0}".format(id))

    @command("Restore ")
    def snapshots_restore(self, 
            id: Annotated[str, "ID"]
        ):
        return self._runRestic("restore {0} --target {1} --verbose".format(id, self._restore_path))

    # methods
    def exec(self, argv):
        commandsManager = CommandsManager()
        commandsManager.register(self)
        return commandsManager.execute(argv)
    
    # utils
    def _runRestic(self, command):
        myenv = os.environ.copy()
        myenv['RESTIC_REPOSITORY'] = self._repository
        myenv['RESTIC_PASSWORD'] = self._repository_password
        myenv["AWS_ACCESS_KEY_ID"] = self._aws_access_key_id
        myenv['AWS_SECRET_ACCESS_KEY'] = self._aws_secret_access_key

        return subprocess.run(self._restic_path + " " + command, env = myenv, cwd = self._data_base_path)
    


