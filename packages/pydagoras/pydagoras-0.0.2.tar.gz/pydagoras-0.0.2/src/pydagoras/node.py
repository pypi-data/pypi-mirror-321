# dag_dot3.py

import time
import logging
import pygraphviz as pgv

logger = logging.getLogger()


class Node(object):
    ''' Node '''
    def __init__(self,doc=None, calc=None,usedby=None, nodetype=None):
        self.calc = calc
        self.doc = doc
        self.usedby = usedby
        self.value = None
        self.nodetype = nodetype

    def pp(self):
        if self.usedby:
            print ("= %s, %s, used by, %s" %( self.value , self.doc, [n.doc for n in self.usedby]))
        #else:
        #    print "= %s, %s, 'output node', %s" %( self.value , self.doc,  self.calc.__doc__)

#----------------------------------------------------------
