from setuptools import setup, find_packages

setup(
    name='customlexer',
    version='0.2',
    packages=find_packages(),
    entry_points=
    """
    [pygments.lexers]
    customlexer = customlexer:CustomLexer
    """
)
