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

# Loop over all .h file, extract the name since by convention this is the name
# of the class, and then try to load that name in the python shell

import sys,os,stat
import gdcm

blacklist = (
# DataStructureAndEncodingDefinition
"ByteBuffer" # WTF ?
"ExplicitDataElement"
"CP246ExplicitDataElement"
"ImplicitDataElement"
"Element"
"ValueIO"
"ParseException"
"ByteSwapFilter"
"ExplicitImplicitDataElement"
"UNExplicitDataElement"
"Attribute"
"VR16ExplicitDataElement"
"LO" # stupid swig
"String"
"Parser"

# DataDict:
"TagToType"
"GroupDict"
"DictConverter"
# Information thingy :

"XMLDictReader"
"TableReader"
"Table"
"XMLPrivateDictReader"
# Common
"Swapper"
"SmartPointer"
"Win32"
"StaticAssert"
"DeflateStream"
"Types"
"Exception"
"ByteSwap"
"Terminal"
# MediaStorageAndFileFormat
"ConstCharWrapper"
"ImageConverter"
# Do not expose low level jpeg implementation detail
"JPEG8Codec"
"JPEG12Codec"
"JPEG16Codec" 
"JPEG2000Codec"
# For now remove the codec part:
"ImageCodec"
"RLECodec"
"RAWCodec"
"AudioCodec"
"EncapsulatedDocument"
"JPEGCodec"
"PDFCodec"
"Decoder"
"ImageValue" # yeah this one should disapear real soon
"SpacingHelper"
"Coder"
)

def processonedir(dirname):
  gdcmclasses = dir(gdcm)
  subtotal = 0
  for file in os.listdir(dirname):
    #print file[-2:]
    if file[-2:] != '.h': continue
    #print file[4:-2]
    gdcmclass = file[4:-2]
    if gdcmclass in gdcmclasses:
      print "ok:", gdcmclass
    else:
      if not gdcmclass in blacklist:
        print "not wrapped:",gdcmclass
        subtotal += 1
  return subtotal

if __name__ == "__main__":
  dirname = os.sys.argv[1]

  total = 0
  for d in os.listdir(dirname):
    if d == '.svn': continue
    pathname = os.path.join(dirname, d)
    #print "pathname:",pathname
    #print os.stat(pathname)
    mode = os.stat(pathname)[stat.ST_MODE]
    if stat.S_ISDIR(mode):
      print "processing directory:", pathname
      total += processonedir(pathname)

  print "number of class not wrap:%d"%total
  sys.exit(total)
