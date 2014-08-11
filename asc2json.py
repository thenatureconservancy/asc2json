#--------------------------------
# Converts ascii GIS grid to JSON
#--------------------------------
import string, sys, os

def asc2json(inFile, outFile):
  try:
    # reader header info
    ascFile = open(inFile, 'r')
    outJson = open(outFile, 'w')
    cols = str(ascFile.readline()[6:][:-2])+',\n'
    rows = str(ascFile.readline()[6:][:-2])+',\n'
    xllCorner = str(ascFile.readline()[10:][:-2])+',\n'
    yllCorner = str(ascFile.readline()[10:][:-2])+',\n'    
    cellSize = str(ascFile.readline()[9:][:-2])+',\n'
    noDataVal = str(ascFile.readline()[13:][:-2])+',\n'
    
    # write header info
    outJson.write('{\n' +'cols:'+cols +'rows:'+rows +'xllCorner:'+xllCorner +
                  'yllCorner:'+yllCorner +'cellSize:'+cellSize +'noDataVal:'+noDataVal +'directionData: [\n')
    # write cell data
    lines = ascFile.readlines()
    print lines
    # close out file
    outJson.write(']\n}')
    outJson.close()
  except:
    print 'oh no. problems'

# arguments
inFile = 'K:/spatial/projects/faunal_movement/movementVectors/birds_direction.asc'
outFile = 'K:/spatial/projects/faunal_movement/movementVectors/birds_direction.json'

# call function
asc2json(inFile,outFile)
