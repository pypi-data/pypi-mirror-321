import subprocess

from ...executors.executor import BaseExecutor
from ...task_templates.task_template import BaseTaskTemplate
from ...task_templates.system_command import SystemCommandTaskTemplate


class SystemCommandExecutor(BaseExecutor):
    """
    Runs a system command with provided arguments
    """
    def supports_task_template(tpl: BaseTaskTemplate) -> bool:
        return isinstance(tpl, SystemCommandTaskTemplate)

    def execute(self, tpl: BaseTaskTemplate):
        tpl: SystemCommandTaskTemplate = tpl
        # returned_value = subprocess.check_output(tpl.cmd, env=tpl.env, shell=True).decode("utf-8")



        # print(returned_value)

        proc=subprocess.run(tpl.cmd, stdin=subprocess.PIPE, env=tpl.env, capture_output=True)
        print(proc.stdout)
        # proc.stdin.write("connect\n") #send "connect"
        # proc.stdin.write("exit\n") #send "exit"
        # proc.stdin.close() #close stdin (like hitting Ctrl+D in the terminal)
        # proc.wait() #wait until process terminates
