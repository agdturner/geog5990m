
# My Notebook


```python
print("My First Jupyter Notebook")
```

    My First Jupyter Notebook
    


```python
print("Hello World")
print("You wonderful world!")
```

    Hello World
    You wonderful world!
    


```python
var = "test"
print(var)
%reset
# Clears all the variable values.
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
print(var)
'''
Expecting a NameError as var has been reset!
'''
```

    test
    Once deleted, variables cannot be recovered. Proceed (y/[n])? y
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-fd64898d0c60> in <module>()
          7 but will work in a Jupyter Notebook!
          8 '''
    ----> 9 print(var)
         10 '''
         11 Expecting a NameError as var has been reset!
    

    NameError: name 'var' is not defined



```python
# Clears all the variable values.
%reset -f
# Resets all variables and forces this to happen with the -f option.
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
```




    '\nThe preceding Magic Line will not work in a normal Python REPL environment,\nbut will work in a Jupyter Notebook!\n'




```python
var = "test"
print(var)
%reset_selective var
# resets the var variable
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
print(var)
'''
Expecting a NameError as var has been reset!
'''
%run model
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''
```

    test
    Once deleted, variables cannot be recovered. Proceed (y/[n])?  y
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-0e364a83e058> in <module>()
          7 but will work in a Jupyter Notebook!
          8 '''
    ----> 9 print(var)
         10 '''
         11 Expecting a NameError as var has been reset!
    

    NameError: name 'var' is not defined



```python
pwd = %pwd
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
%save test 1-2 3 4-5
# Saves commands 1 to 5 to test.py
'''
The preceding Magic Line will not work in a normal Python REPL environment,
but will work in a Jupyter Notebook!
'''

```

    C:\Users\geoagdt\src\python\geog5990m\src\unpackaged\abm\AgentBasedModelling
    The following commands were written to file `test.py`:
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
    




    '\nThe preceding Magic Line will not work in a normal Python REPL environment,\nbut will work in a Jupyter Notebook!\n'




```python
%sx python test.py
# Run something on the underlying operating system
# NB. It is possible to run cells using other languages.
```




    ['My First Jupyter Notebook',
     'Hello World',
     'You wonderful world!',
     'test',
     'Traceback (most recent call last):',
     '  File "test.py", line 7, in <module>',
     "    get_ipython().run_line_magic('reset', '')",
     "NameError: name 'get_ipython' is not defined"]




```python
import time
%timeit time.sleep(10)
# For timing how long a set of lines takes to run.
```

    10 s ± 1.37 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    


```python
import os
%pwd
# Print present working directory
dirname = 'test'
%mkdir $dirname
# Make a test directory.
# The $ sign is needed for Magic Lines in order to address the variable!
%cd $dirname
# Change to the test directory.
%pwd
%cd ..
# Move to the directory containing the directory you are in. 
path = os.getcwd()
print(path)
# Store current working directory.
%cd ~
# Move to home/user directory.
%pwd
os.chdir(path)
# Move to stored directory.
%cd $dirname
%pwd
%cd ..
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
```

    C:\Users\geoagdt\src\python\geog5990m\src\unpackaged\abm\AgentBasedModelling\test
    C:\Users\geoagdt\src\python\geog5990m\src\unpackaged\abm\AgentBasedModelling
    C:\Users\geoagdt\src\python\geog5990m\src\unpackaged\abm\AgentBasedModelling
    C:\Users\geoagdt
    C:\Users\geoagdt\src\python\geog5990m\src\unpackaged\abm\AgentBasedModelling\test
    C:\Users\geoagdt\src\python\geog5990m\src\unpackaged\abm\AgentBasedModelling
    




    '\nThere are two ways to create and move between directories, one way using Magic \nLines and another way using os.\n'


