#
# genDataset
# by Le 202408~
#
import sys, getopt, os
import time
import gc

def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h")
    except getopt.GetoptError:
        print ('python analyze.py')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('python analyze.py')
            sys.exit(2)
        else:
            assert "unhandled option"
    pose_all_file_large="data/pose_keypoints_large.csv"
    pose_all_file_medium="data/pose_keypoints_medium.csv"
    pose_all_file_small="data/pose_keypoints_small.csv"
    nose_file_large="data/nose_keypoints_large.csv"
    nose_file_medium="data/nose_keypoints_medium.csv"
    nose_file_small="data/nose_keypoints_small.csv"

    analyze(pose_all_file_large) 
    gc.collect()
    analyze(nose_file_large) 
    gc.collect() 
    
    analyze(pose_all_file_medium)
    gc.collect()
    analyze(nose_file_medium)
    gc.collect()

    analyze(pose_all_file_small)
    gc.collect()
    analyze(nose_file_small)
    gc.collect()
def analyze(input_file):   
    #check file existed
    if not os.path.isfile(input_file):
        print("input file not found")
        sys.exit(2)
    #start anlyzing
    #start time in nanosecond
    start_time_nanosecond = time.time_ns()
    #nose_x list initilization
    nose_x=[]
    #open file
    openfile = open(input_file,"r")
    #read line by line
    lines = openfile.readlines()
    for line in lines:
        #bypass first line
        if not line.startswith("frame"):
            linestr = line.split(",")
            nose_x_value = float(linestr[1])
            nose_x.append(nose_x_value)
    read_file_end_time_nanosecond = time.time_ns()
    nose_x_min = min(nose_x)
    nose_x_max = max(nose_x)
    nose_x_average = round(sum(nose_x)/len(nose_x),2)
    end_time_nanosecond = time.time_ns()
    readfile_time = round((read_file_end_time_nanosecond-start_time_nanosecond)/1000000.0, 2)
    execution_time = round((end_time_nanosecond-start_time_nanosecond)/1000000.0, 2)
    #end analyzing
    print("***********************************************************")
    print("Analyze results for ", input_file)
    print("Minimum value of nose_x: ", nose_x_min)
    print("Maximum value of nose_x: ", nose_x_max)
    print("Average value of nose_x: ", nose_x_average)
    print("[E]Execution time (ms) ([E]=[R]+[C]): ", execution_time)
    print("[R]Read file time (ms): ", readfile_time)
    print("[C]Calculation time (ms): ", round(execution_time-readfile_time, 2))
    print("***********************************************************")
   

if __name__ == "__main__":
    main(sys.argv[1:])  