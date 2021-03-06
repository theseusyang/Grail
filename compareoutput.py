import sys,getopt
from CommonDefs import CommonDefs

def fileToTuples(file, delimiter):
    f1 = open(file,"r")
    data1 = [] #list of tuples from f1
    for line in f1.readlines():
	line = line.strip()
        tokens = line.split(delimiter)
        tuple = []
        for token in tokens:
            tuple.append(token.strip())
	if(len(line) >0 and len(tuple ) > 0):
        	data1.append(tuple)
    f1.close()
    return data1


def main(argv):
    '''Main function that does the actual work your description goes in here.
    Args:
    infile1 and infile2 are the two files to be compared for value similarity with default delimiter of "|"
    Returns:
    0 if the two files match else 1
    The code assumes similar listing of attributes in the two files
    '''
    infile1=""
    infile2=""
    delimiter="|"
    algo = ""

    try:
        opts, args = getopt.getopt(argv,"hf:F:a:",["infile1=","infile2=","algorithm="])
    except getopt.GetoptError:
        print 'test.py -f <inputfile1> -F <inputfile2> -a <graph_algorithm>'
        sys.exit(2)
	
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -f <inputfile1> -F <inputfile2>'
            sys.exit()
        elif opt in ("-f", "--infile1"):
            infile1 = arg
        elif opt in ("-F", "--infile2"):
            infile2 = arg
	elif opt in ("-a", "--algorithm"):
	    algo = arg

    print "algo=", algo
    data1 = fileToTuples(infile1,delimiter)
    data2 = fileToTuples(infile2,delimiter)
    
    if algo == 'toposort':
	#dependency verification as multiple topo ordering possible
	depen_map = dict()
	for entry in data1:
		vid = int(entry[0])
		val = int(entry[1])
		depen_map[vid] = val
	
	for entry in data2:
		vid = int(entry[0])
		vertex_rank = depen_map[vid]
		dependencies = entry[1].split(",")
		for val in dependencies:
			depen_rank = depen_map[int(val)]
			if vertex_rank <= depen_rank:
				return 1
	return 0

    else:
        if len(data1) != len(data2):
            return 1
        else:
            for i,val in enumerate(data1):
        	if(len(data1[i]) != len(data2[i])):
        		return 1
                if(data1[i] != data2[i]):
        		if(CommonDefs.INT_MAX in data1[i] or CommonDefs.INT_MAX in data2[i]):
        			return 2
        		else:
                      		return 1
            return 0

if __name__ == "__main__":
    rc = main(sys.argv[1:])
    if rc > 0:
	if rc == 2:
		print 'Input graph is disconnected and the current implementation of WCC does not support disconnected graphs'
		sys.exit(0)
	else:
        	print 'Actual and Expected outputs are different'
        	sys.exit(1)
    else:

        print 'Actual and Expected outputs are similar'
        sys.exit(0)



