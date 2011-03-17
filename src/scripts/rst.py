'''
Created on 16 mars 2011

@author: Robin Jarry
'''

import os, os.path, sys
import docutils
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives import _directive_registry
import inspect



def main():
    if len(sys.argv) < 2:
        print >>sys.stderr, "Please provide the output type (html, xml, latex, man, word, ...)"
        print >>sys.stderr, "usage: rst <output type> options"
        exit(1)
    output_type = sys.argv[1]
    del sys.argv[1]
    dir = os.path.abspath(os.path.dirname(__file__))
    script_name = os.path.join(dir, "rst2%s.py" % output_type)
    if not os.path.exists(script_name):
        print >>sys.stderr, "Output type '%s' unknown" % output_type
        exit(1) 
    ext_dir = get_extension_directory()
    if os.path.exists(ext_dir):
        register_extensions(ext_dir)
    
    execfile(script_name)
    
    
def register_extensions(extension_directory):
    sys.path.append(extension_directory)
    for file in os.listdir(extension_directory):
        if file.endswith(".py"):
            module_name = file[:-3]
            __import__(module_name)
            module = sys.modules[module_name]
            register_directives(module)
  
def register_directives(module):
    classes = inspect.getmembers(module, inspect.isclass)   
    for name, classObj in classes:
        if not name.lower() in _directive_registry.keys() and issubclass(classObj, Directive):
            directives.register_directive(name.lower(), classObj)
            
def get_extension_directory():
    import docutilsextensions
    return os.path.abspath(os.path.dirname(docutilsextensions.__file__))

if __name__ == "__main__":
    main()
