
# coding: utf-8

# # My Notebook

# In[1]:


print("My First Jupyter Notebook")


# In[2]:


print("Hello World")
print("You wonderful world!")


# In[3]:


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


# In[4]:


# Clears all the variable values.
get_ipython().run_line_magic('reset', '-f')
# Resets all variables and forces this to happen with the -f option.
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''


# In[5]:


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


# In[6]:


pwd = get_ipython().run_line_magic('pwd', '')
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
print(pwd)
filename = 'test.py' 
import os
if os.path.exists(filename):
    os.remove(filename)
# Remove filename.
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
get_ipython().run_line_magic('save', 'test 1-2 3 4-5')
# Saves commands 1 to 5 to test.py
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''


# In[7]:


get_ipython().run_line_magic('sx', 'python test.py')
# Run something on the underlying operating system
# NB. It is possible to run cells using other languages.


# In[8]:


import time
get_ipython().run_line_magic('timeit', 'time.sleep(10)')
# For timing how long a set of lines takes to run.


# In[4]:


import os
get_ipython().run_line_magic('pwd', '')
# Print present working directory
dirname = 'test'
get_ipython().run_line_magic('mkdir', '$dirname')
# Make a test directory.
# The $ sign is needed for Magic Lines in order to address the variable!
get_ipython().run_line_magic('cd', '$dirname')
# Change to the test directory.
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', '..')
# Move to the directory containing the directory you are in. 
path = os.getcwd()
print(path)
# Store current working directory.
get_ipython().run_line_magic('cd', '~')
# Move to home/user directory.
get_ipython().run_line_magic('pwd', '')
os.chdir(path)
# Move to stored directory.
get_ipython().run_line_magic('cd', '$dirname')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', '..')
os.rmdir(dirname)
# Delete the dirname directory.
os.mkdir(dirname)
# Make the dirname directory.
os.rmdir(dirname)
# Delete the dirname directory.
'''
There are two ways to create and move between directories, one way using Magic 
Lines and another way using os, but seamingly there is no Magic Lines way to 
delete a file or directory!
'''

