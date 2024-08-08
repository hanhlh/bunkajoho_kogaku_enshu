#
# genDataset
# by Le 202408~
#
import sys, getopt, os
import pandas as pd

def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:", ["help", "input_file=", "output_file="])
    except getopt.GetoptError:
        print ('python genDataset_nose.py -i <input_file> -o <output_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('python genDataset_nose.py -i <input_file> -o <output_file>')
            sys.exit(2)
        elif opt in ("-i", "--input_file"):
            input_file = arg
            print(input_file)
            if not input_file.endswith(".csv"):
                print("input file should be .csv file")
                sys.exit(2)
            if not os.path.isfile(input_file):
                print("input file not found")
                sys.exit(2)
        elif opt in ("-o", " --output_file"):
            output_file = arg
            if not output_file.endswith(".csv"):
                print("output file should be .csv file")
                sys.exit(2)
        else:
            assert "unhandled option"
    print ('Input file is "', input_file)
    print ('Output file is "', output_file)
    pd.read_csv(input_file, usecols=[0,1,2,3]).to_csv(output_file, index=False)
   
if __name__ == "__main__":
    main(sys.argv[1:])  