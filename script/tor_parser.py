from __future__ import unicode_literals, print_function
from pypeg2 import *
from pypeg2.xmlast import thing2xml

# A Symbol can be an arbitrary word or one word of an Enum.
# In this easy example there is an Enum.


class Command(Keyword):
    grammar = Enum(K("Click"), K("Wait"), K("Type"), K("Press"))


# Parsing attributes adds them to the resulting thing.
# blank is a callback function. Callback functions are being executed by
# compose(). parse() ignores callback functions. blank inserts " ".
# name() generates a name attribute.

class Parameter(object):
    grammar = blank, name()


# If a thing is a List, then parsed things are being put into.
class Function(List):
    grammar = attr("command", Command), "(", maybe_some(attr("param", Parameter)), ")", endl


class FunctionOrComment(List):
    comment = re.compile(r"#.*")
    grammar = maybe_some(Function), maybe_some(comment)


def call_parser(line):
    results = parse(line, FunctionOrComment)
    return results


def parse_result(line):
    try:
        results = call_parser(line)
        print(thing2xml(results, pretty=True).decode())
    except GrammarTypeError as e:
        print("GrammarTypeError: " + str(e))
    except GrammarValueError as e2:
        print("GrammarValueError" + str(e2))

    return results

