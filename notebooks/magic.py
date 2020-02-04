""" My custom magic! """

from IPython.core.magic import Magics, magics_class, line_magic


@magics_class
class MyMagics(Magics):

    @line_magic
    def my_magic(self, line):
        try:
            number = float(line)
            print("Hey, this is a number!")
        except:
            return
        return number * 2.5

    
def load_ipython_extension(ipython):
    ipython.register_magics(MyMagics)
    
