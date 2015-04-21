'''
Created on 11/11/2013

@author: iMath
'''

import os

def constant(f):
    '''
    Decorator to indicate that a property of a class is a constant, so, cannot be set, only get
    '''
    def fset(self, value):
        raise SyntaxError
    def fget(self):
        return f()
    return property(fget, fset)


def deprecated(package="", instead=""):
    '''
    A decorator to indicate that the function or method called is deprecated. It calls anyway the function, but displays a message 
    in the console indicating it
    
    'package' is the optional package or class name where the deprecated function is called
    'instead' is the optional parameter containing the new function that should be called instead of the deprecated one 
    '''
    
    def wrap(f):
        def newF(*args, **kwargs):
            nameFunc = f.__name__
            part1=""
            part2=""
            if package!="":
                part1 = package + "."
            if instead!="":
                part2 = "Use " + package + "." + instead + " instead."
        
                print "Function " + part1 + nameFunc + " is deprecated. " + part2
            return f(*args, **kwargs)
        
        return newF
    return wrap

class CONS(object):
    '''
    It define the global constants for the Colossus core
    
    '''
    @constant
    def LOCALHOST():
        return "localhost" 
    
    @constant
    def CONFIGFILE():
        return "/etc/colossus/colossus.config/config.properties"
      
    @constant
    def HOSTFILE():
        return "/etc/colossus/colossus.config/host_file.txt"
    
    @constant
    def STARTCLIENTSCRIPT():
        return "/etc/colossus/colossus.config/exec_startClient.py"
       
    @constant
    def BEGINTOKEN():
        return "###---###\n"
    
    @constant
    def ENDTOKEN():
        return "---###---\n"
    
    @constant
    def BEGINTOKEN_MERGE():
        return "###MERGE###\n"
    
    @constant
    def ENDTOKEN_MERGE():
        return "---MERGE---\n"
    
    @constant
    def BEGINTOKEN_PROCESSELEM():
        return "###PROCESSELEM###\n"
    
    @constant
    def ENDTOKEN_PROCESSELEM():
        return "---PROCESSELEM---\n"
    
    @constant
    def ENDPROCESS():
        return "---------\n"
    

        