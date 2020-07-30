from __future__ import unicode_literals, print_function
from pypeg2 import *

# A Symbol can be an arbitrary word or one word of an Enum.
# In this easy example there is an Enum.
from pypeg2.xmlast import thing2xml


class Type(Keyword):
    grammar = Enum(K("Click"), K("Wait"), K("Type"), K("Press"))


# Parsing attributes adds them to the resulting thing.
# blank is a callback function. Callback functions are being executed by
# compose(). parse() ignores callback functions. blank inserts " ".
# name() generates a name attribute.

class Parameter(object):
    grammar = blank, name()


# If a thing is a List, then parsed things are being put into.
class Function(List):
    grammar = attr("typing", Type), "(", maybe_some(attr("param", Parameter)), ")", endl


class FunctionOrComment(List):
    comment = re.compile(r"#.*")
    grammar = maybe_some(Function), maybe_some(comment)


'''
if __name__ == '__main__':
    filename = '../resource/script.tor'
    # Read the data
    with open(filename, 'r') as source_file:
        data = source_file.read()

        # Attempt to parse it, or throw errors
        for line in data.splitlines():
            try:
                results = parse(line, FunctionOrComment)
                print(thing2xml(results, pretty=True).decode())
            except GrammarTypeError as e:
                print("GrammarTypeError: " + str(e))
            except GrammarValueError as e2:
                print("GrammarValueError" + str(e2))
'''
