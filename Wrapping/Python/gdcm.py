""" This module loads all the classes from the GDCM library into
its namespace.  This is a required module."""

import os

if os.name == 'posix':
  # extremely important !
  # http://gcc.gnu.org/faq.html#dso
  # http://mail.python.org/pipermail/python-dev/2002-May/023923.html
  # http://wiki.python.org/moin/boost.python/CrossExtensionModuleDependencies
  import sys
  orig_dlopen_flags = sys.getdlopenflags()
  try:
    import dl
  except ImportError:
    # are we on AMD64 ?
    try:
      import DLFCN as dl
    except ImportError:
      print "Could not import dl"
      dl = None
  if dl:
    #print "dl was imported"
    #sys.setdlopenflags(dl.RTLD_LAZY|dl.RTLD_GLOBAL)    
    sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)    
  from gdcmswig import *
  # revert:
  sys.setdlopenflags(orig_dlopen_flags)
  del sys, dl
  del orig_dlopen_flags
else:
  from gdcmswig import *

# bye bye
del os