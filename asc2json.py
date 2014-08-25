#! /bin/python
#--------------------------------
# Converts ascii GIS grid to JSON
# Ok, so it's not real json quite yet.
#--------------------------------
import string, sys, os

def asc2json(inFile, outFile):
  try:
    # reader header info
    ascFile = open(inFile, 'U')
    outJson = open(outFile, 'w')
    cols = str(ascFile.readline()[6:][:-1])+',\n'
    rows = str(ascFile.readline()[6:][:-1])+',\n'
    xllCorner = str(ascFile.readline()[10:][:-1])+',\n'
    yllCorner = str(ascFile.readline()[10:][:-1])+',\n'    
    cellSize = str(ascFile.readline()[9:][:-1])+',\n'
    noDataVal = str(ascFile.readline()[13:][:-1])+',\n'
    
    # write header info
    outJson.write('{\n' +'cols:'+cols +'rows:'+rows +'xllCorner:'+xllCorner +
                  'yllCorner:'+yllCorner +'cellSize:'+cellSize +'noDataVal:'+noDataVal +'directionData: [\n')
    # write cell data
    gridData = ascFile.read().split(' ')
    for pxl in gridData:
      print pxl
      if pxl == '-9999\r':
        print 'taco'
        outJson.write('0, ')
      elif pxl == '-9999\n':
        print 'burrito'
        outJson.write('0, ')
      elif pxl == '\n-9999':
        print 'shiiiit'
        outJson.write('0, ')
      elif pxl == '9999 ':
        print 'nachos'
        outJson.write('0, ')      
      elif pxl == '-9999':
        print 'boo'
        outJson.write('0, ')
      else:
        outJson.write(str(pxl[:6])+', ')
    # close out file
    outJson.write('\n]\n}')
    outJson.close()
    print 'whoomp, there it is.'
  except:
    print 'oh no. problems'

# arguments
#inFile = sys.argv[0]
#inFile = sys.argv[1]
inFile = '../birds_direction.asc'
outFile = '../birds_direction.js'
#inFile = 'K:/spatial/projects/faunal_movement/movementVectorsGeo/birds_direction.asc'
#outFile = 'K:/spatial/projects/faunal_movement/movementVectorsGeo/birds_direction.json'

# call function
asc2json(inFile,outFile)
