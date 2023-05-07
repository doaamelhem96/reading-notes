# with statement in Python:
*****
The with statment in py is used when working with **external resources** such as ***files***. It provides ***an automatically*** way to manage resources by handling the setup and teardown of the resource, ensuring that it is properly closed or released after use. When opening a file,**the with statement helps in automatically closing the file, even if an exception occurs within the block of code.**
*****
Here's an example of using the with statement to open a file and read its contents:

***with open('readme.md', 'r') as reader:
    print (reader.read())
    #H1***
In the above code, the file is **automatically** closed when the block of code inside the **with statement is finished**, ***regardless*** of whether an exception occurs or not. This helps in managing resources efficiently and avoiding resource leaks.
*****
# things I want to learn:


Notes that :
-------
 File is set of byte transfer to zeros and ones  until computer's process read it then using Unicode(utf-8) and ASCII code to encoding file and reading 

the  ASCII code is subset from UTF_8 Unicode 
so you must use appropriate encoding for encoding all the fills