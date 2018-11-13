# coding: utf-8
print("My First Jupyter Notebook")
print("Hello World")
print("You wonderful world!")
var = "test"
print(var)
get_ipython().run_line_magic('reset', '')
# Clears all the variable values.
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
print(var)
'''
Expecting a NameError as var has been reset!
'''
# Clears all the variable values.
get_ipython().run_line_magic('reset', '-f')
# Resets all variables and forces this to happen with the -f option.
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
var = "test"
print(var)
get_ipython().run_line_magic('reset_selective', 'var')
# resets the var variable
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
print(var)
'''
Expecting a NameError as var has been reset!
'''
get_ipython().run_line_magic('run', 'model')
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
