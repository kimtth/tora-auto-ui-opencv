'''
@TODO
Converting the result of parsing to pyAutoGUI method.
'''
from api.api import AutoGuiWrapper
from script.tor_parser import parse_result, Function

from detect import img_detector


def param_to_str(param):
    return str(param)


def param_to_int(param):
    return int(param)


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
                    root_path = 'C:/Users/IEUser/code/tora/resource/'
                    filename = param
                    file_extension = '.png'

                    target_img_path = root_path + filename + file_extension
                    coord = img_detector.img_coord_detector_by_target(target_img_path)

                    self.auto.click(coord)
                elif str(command).lower() == 'wait':
                    self.auto.wait(param_to_int(param))
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


def run():
    filename = 'C:/Users/IEUser/code/tora/resource/script.tor'
    run = RunScript()
    run.exec_script(filename)


if __name__ == '__main__':
    run()
