############################################################################
#
#  Program: GDCM (Grass Root DICOM). A DICOM library
#  Module:  $URL$
#
#  Copyright (c) 2006-2008 Mathieu Malaterre
#  All rights reserved.
#  See Copyright.txt or http://gdcm.sourceforge.net/Copyright.html for details.
#
#     This software is distributed WITHOUT ANY WARRANTY; without even
#     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the above copyright notice for more information.
#
############################################################################

"""
Hello World !
"""

import gdcm
import sys

if __name__ == "__main__":

  # Get the filename from the command line
  filename = sys.argv[1]

  # Instanciate a gdcm.Reader
  # This is the main class to handle any type of DICOM object
  # You should check for gdcm.ImageReader for reading specifically DICOM Image file
  r = gdcm.Reader()
  r.SetFileName( filename )
  # If the reader fails to read the file, we should stop !
  if not r.Read():
    print "Not a valid DICOM file"
    sys.exit(1)

  # Get the DICOM File structure
  file = r.GetFile()

  # Get the DataSet part of the file
  dataset = file.GetDataSet()

  # Ok let's print it !
  print dataset
