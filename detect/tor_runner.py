'''
@TODO
Converting the result of parsing to pyAutoGUI method.
'''
from api.api import AutoGuiWrapper
from parser_script.tor_parser import parse_result, Function


def param_to_str(param):
    return str(param)


class RunScript:

    def __init__(self):
        self.auto = AutoGuiWrapper()

    def traverse(self, f):
        func_or_comment = f[0]
        if isinstance(func_or_comment, Function):
            command = f[0].command
            if hasattr(func_or_comment, 'param'):
                param = f[0].param.name

                if str(command).lower() == 'click':
                    # @TODO
                    self.auto.click(param)
                elif str(command).lower() == 'wait':
                    self.auto.wait(param)
                elif str(command).lower() == 'type':
                    self.auto.type(param_to_str(param))
                elif str(command).lower() == 'press':
                    self.auto.press(param_to_str(param))

                print(command, param)

    def exec_script(self, file_path):
        # Read the data
        with open(file_path, 'r') as source_file:
            data = source_file.read()

            # Attempt to parse it, or throw errors
            for line in data.splitlines():
                f = parse_result(line)
                self.traverse(f)


if __name__ == '__main__':
    filename = '../resource/script.tor'
    run = RunScript()
    run.exec_script(filename)
