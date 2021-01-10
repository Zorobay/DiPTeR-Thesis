from pygments.lexers.python import Python3Lexer
from pygments.
from pygments.style import Style
from pygments.token import *


class CustomLexer(Python3Lexer):
    name = "CustomLexer"
    aliases = "customlexer"
    filenames = ["*.py"]

    EXTRA_KEYWORDS = ["Tensor", "mul", "pow", "gradient"]

    def get_tokens_unprocessed(self, text, stack=('root',)):
        for index, token, value in Python3Lexer.get_tokens_unprocessed(self, text):
            if token in Name and value in self.EXTRA_KEYWORDS:
                yield index, Name.Function, value
            else:
                yield index, token, value

class GLSLLexer(GLSLLexer):



