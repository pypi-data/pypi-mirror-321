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
    _data_path: list[str]
    _data_iexclude: list[str]
    _restore_path: str
    _restic_path: str
    
    # ctor
    def __init__(self, repository: str, repository_password: str, aws_access_key_id: str, aws_secret_access_key: str, data_base_path: str, data_path: str, data_iexclude: list[str], restore_path: str, restic_path: str = ""):
        self._repository = repository
        self._repository_password = repository_password
        self._aws_access_key_id = aws_access_key_id
        self._aws_secret_access_key = aws_secret_access_key

        self._data_base_path = data_base_path
        if self._data_base_path == "":
            self._data_base_path = os.getcwd()

        self._data_path = data_path
        self._data_iexclude = data_iexclude

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
    @command("Stats repository")
    def init_stats(self):
        return self._runRestic("stats --mode raw-data")
    
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

    @command("Check repository integrity ")
    def snapshots_check(self):
        return self._runRestic("check")
    
    @command("Restore ")
    def snapshots_restore(self, 
            id: Annotated[str, "ID"],
            path: Annotated[str, "Path to restore"] = "",
            host: Annotated[str, "Host"] = "",
            include: Annotated[str, "Include"] = "",
            verify = False,
            no_same_owner = False,
            no_same_permissions = False
        ):
        command = "restore {0} --target {1} --verbose".format(id, self._restore_path)
        if path != "":
            command += " --path \"{0}\"".format(path)
        if host != "":
            command += " --host \"{0}\"".format(host)
        if include != "":
            command += " --include \"{0}\"".format(include)
        if no_same_owner:
            command += " --no-same-owner"
        if no_same_permissions:
            command += " --no-same-permissions"
        if verify:
            command += " --verify"
        for data_iexclude in self._data_iexclude:
            command += " --iexclude " + data_iexclude
        return self._runRestic(command)

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
    


