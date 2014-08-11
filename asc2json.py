#--------------------------------
# Converts ascii GIS grid to JSON
# Ok, so it's not real json quite yet.
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
    gridData = ascFile.read().split(' ')
    for pxl in gridData:
      if pxl == '-9999' or '-9999\n':
        outJson.write('0, ')
      else:
        outJson.write(str(pxl[:5])+', ')
    # close out file
    outJson.write('\n]\n}')
    outJson.close()
    print 'whoomp, there it is.'
  except:
    print 'oh no. problems'

# arguments
inFile = 'K:/spatial/projects/faunal_movement/movementVectors/birds_direction.asc'
outFile = 'K:/spatial/projects/faunal_movement/movementVectors/birds_direction.json'

# call function
asc2json(inFile,outFile)
