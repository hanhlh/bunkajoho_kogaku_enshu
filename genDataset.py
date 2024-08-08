#
# genDataset
# by Le 202408~
#
import sys, getopt, os
import pandas as pd
import random

def analyze_input(inputFile):
    global nose_x, nose_y, nose_score
    global eyeL_x, eyeL_y, eyeL_score, eyeR_x, eyeR_y, eyeR_score
    global earL_x, earL_y, earL_score, earR_x, earR_y, earR_score
    global shoulderL_x, shoulderL_y, shoulderL_score, shoulderR_x, shoulderR_y, shoulderR_score
    global elbowL_x, elbowL_y, elbowL_score, elbowR_x, elbowR_y, elbowR_score
    global wristL_x, wristL_y, wristL_score, wristR_x, wristR_y, wristR_score
    global kneeL_x, kneeL_y, kneeL_score, kneeR_x, kneeR_y, kneeR_score
    global hipL_x, hipL_y, hipL_score, hipR_x, hipR_y, hipR_score
    global ankleL_x, ankleL_y, ankleL_score, ankleR_x, ankleR_y, ankleR_score
    
    df=pd.read_csv(inputFile)
   
    nose_x=df['nose_x'].tolist()
    nose_y=df['nose_y'].tolist() 
    nose_score=df['nose_score'].tolist()

    eyeL_x=df['eye(L)_x'].tolist()
    eyeL_y=df['eye(L)_y'].tolist() 
    eyeL_score=df['eye(L)_score'].tolist()
    
    eyeR_x=df['eye(R)_x'].tolist()
    eyeR_y=df['eye(R)_y'].tolist() 
    eyeR_score=df['eye(R)_score'].tolist()
    
    earL_x=df['ear(L)_x'].tolist()
    earL_y=df['ear(L)_y'].tolist() 
    earL_score=df['ear(L)_score'].tolist()
    
    earR_x=df['ear(R)_x'].tolist()
    earR_y=df['ear(R)_y'].tolist() 
    earR_score=df['ear(R)_score'].tolist()
    
    shoulderL_x=df['shoulder(L)_x'].tolist()
    shoulderL_y=df['shoulder(L)_y'].tolist() 
    shoulderL_score=df['shoulder(L)_score'].tolist()
    
    shoulderR_x=df['shoulder(R)_x'].tolist()
    shoulderR_y=df['shoulder(R)_y'].tolist() 
    shoulderR_score=df['shoulder(R)_score'].tolist()
    
    elbowL_x=df['elbow(L)_x'].tolist()
    elbowL_y=df['elbow(L)_y'].tolist() 
    elbowL_score=df['elbow(L)_score'].tolist()
    
    elbowR_x=df['elbow(R)_x'].tolist()
    elbowR_y=df['elbow(R)_y'].tolist() 
    elbowR_score=df['elbow(R)_score'].tolist()
    
    wristL_x=df['wrist(L)_x'].tolist()
    wristL_y=df['wrist(L)_y'].tolist() 
    wristL_score=df['wrist(L)_score'].tolist()
    
    wristR_x=df['wrist(R)_x'].tolist()
    wristR_y=df['wrist(R)_y'].tolist() 
    wristR_score=df['wrist(R)_score'].tolist()
    
    hipL_x=df['hip(L)_x'].tolist()
    hipL_y=df['hip(L)_y'].tolist() 
    hipL_score=df['hip(L)_score'].tolist()
    
    hipR_x=df['hip(R)_x'].tolist()
    hipR_y=df['hip(R)_y'].tolist() 
    hipR_score=df['hip(R)_score'].tolist()
    
    kneeL_x=df['knee(L)_x'].tolist()
    kneeL_y=df['knee(L)_y'].tolist() 
    kneeL_score=df['knee(L)_score'].tolist()
    
    kneeR_x=df['knee(R)_x'].tolist()
    kneeR_y=df['knee(R)_y'].tolist() 
    kneeR_score=df['knee(R)_score'].tolist()
    
    ankleL_x=df['ankle(L)_x'].tolist()
    ankleL_y=df['ankle(L)_y'].tolist() 
    ankleL_score=df['ankle(L)_score'].tolist()
    
    ankleR_x=df['ankle(R)_x'].tolist()
    ankleR_y=df['ankle(R)_y'].tolist() 
    ankleR_score=df['ankle(R)_score'].tolist()
    
def getRandomValue(list):
    #contain min value, max value
    return random.uniform(min(list),max(list))

def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:n:", ["help", "input_file=", "output_file=", "numLines="])
    except getopt.GetoptError:
        print ('python genDataset.py -i <input_file> -o <output_file> -n <#numLines>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('python genDataset.py -i <input_file> -o <output_file> -n <#numLines>')
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
        elif opt in ("-n", " --numLines"):
            numLines = int(arg)
        else:
            assert "unhandled option"
    print ('Input file is "', input_file)
    print ('Output file is "', output_file)
    print ('numLines is "', numLines)
    analyze_input(input_file)
    
    data = {
        'frame': [],
        'nose_x': [],
        'nose_y': [],
        'nose_score': [],
        'eyeL_x': [], 
        'eyeL_y': [], 
        'eyeL_score': [], 
        'eyeR_x': [], 
        'eyeR_y': [], 
        'eyeR_score': [],
        'earL_x': [],
        'earL_y': [], 
        'earL_score': [], 
        'earR_x':[], 
        'earR_y': [], 
        'earR_score': [],
        'shoulderL_x': [], 
        'shoulderL_y': [], 
        'shoulderL_score': [], 
        'shoulderR_x': [], 
        'shoulderR_y': [], 
        'shoulderR_score': [],
        'elbowL_x': [], 
        'elbowL_y': [], 
        'elbowL_score': [], 
        'elbowR_x': [],
        'elbowR_y': [], 
        'elbowR_score': [],
        'wristL_x': [], 
        'wristL_y': [], 
        'wristL_score': [], 
        'wristR_x': [], 
        'wristR_y':[], 
        'wristR_score':[],
        'kneeL_x': [], 
        'kneeL_y': [], 
        'kneeL_score': [], 
        'kneeR_x': [], 
        'kneeR_y': [], 
        'kneeR_score': [],
        'hipL_x': [], 
        'hipL_y': [], 
        'hipL_score': [], 
        'hipR_x': [], 
        'hipR_y': [], 
        'hipR_score':[], 
        'ankleL_x': [], 
        'ankleL_y': [], 
        'ankleL_score': [], 
        'ankleR_x': [], 
        'ankleR_y': [], 
        'ankleR_score':[]
    }
    header_str = "frame"
    nose_str = "nose_x,nose_y,nose_score"
    eye_str = "eyeL_x,eyeL_y,eyeL_score,eyeR_x,eyeR_y,eyeR_score"
    ear_str = "earL_x,earL_y,earL_score,earR_x,earR_y,earR_score"
    shoudler_str= "shoulderL_x,shoulderL_y,shoulderL_score,shoulderR_x,shoulderR_y,shoulderR_score"
    elbow_str= "elbowL_x,elbowL_y,elbowL_score,elbowR_x,elbowR_y,elbowR_score"
    wrist_str="wristL_x,wristL_y,wristL_score,wristR_x,wristR_y,wristR_score"
    knee_str="kneeL_x,kneeL_y,kneeL_score,kneeR_x,kneeR_y,kneeR_score"
    hip_str="hipL_x,hipL_y,hipL_score,hipR_x,hipR_y,hipR_score"
    ankle_str="ankleL_x,ankleL_y,ankleL_score,ankleR_x,ankleR_y,ankleR_score"
    header_str=nose_str+","+eye_str+","+ear_str+","+shoudler_str+","+elbow_str+","+wrist_str+","+knee_str+","+hip_str+","+ankle_str

    line=1
    for _ in range(numLines):
        data['frame'].append(line)
        data['nose_x'].append(round(getRandomValue(nose_x),0))
        data['nose_y'].append(round(getRandomValue(nose_y),0))
        data['nose_score'].append(getRandomValue(nose_score))
        data['eyeL_x'].append(round(getRandomValue(eyeL_x), 0)) 
        data['eyeL_y'].append(round(getRandomValue(eyeL_y), 0))
        data['eyeL_score'].append(getRandomValue(eyeL_score)) 
        data['eyeR_x'].append(round(getRandomValue(eyeR_x), 0)) 
        data['eyeR_y'].append(round(getRandomValue(eyeR_y), 0)) 
        data['eyeR_score'].append(getRandomValue(eyeR_score))
        data['earL_x'].append(round(getRandomValue(earL_x), 0))
        data['earL_y'].append(round(getRandomValue(earL_y), 0)) 
        data['earL_score'].append(getRandomValue(earL_score)) 
        data['earR_x'].append(round(getRandomValue(earR_x), 0)) 
        data['earR_y'].append(round(getRandomValue(earR_y), 0))
        data['earR_score'].append(getRandomValue(earR_score))
        data['shoulderL_x'].append(round(getRandomValue(shoulderL_x), 0)) 
        data['shoulderL_y'].append(round(getRandomValue(shoulderL_y), 0)) 
        data['shoulderL_score'].append(getRandomValue(shoulderL_score))
        data['shoulderR_x'].append(round(getRandomValue(shoulderR_x), 0)) 
        data['shoulderR_y'].append(round(getRandomValue(shoulderR_y), 0)) 
        data['shoulderR_score'].append(getRandomValue(shoulderR_score))
        data['elbowL_x'].append(round(getRandomValue(elbowL_x), 0)) 
        data['elbowL_y'].append(round(getRandomValue(elbowL_y), 0)) 
        data['elbowL_score'].append(getRandomValue(elbowL_score)) 
        data['elbowR_x'].append(round(getRandomValue(elbowR_x), 0))
        data['elbowR_y'].append(round(getRandomValue(elbowR_y), 0)) 
        data['elbowR_score'].append(getRandomValue(elbowR_score))
        data['wristL_x'].append(round(getRandomValue(wristL_x), 0)) 
        data['wristL_y'].append(round(getRandomValue(wristL_y), 0)) 
        data['wristL_score'].append(getRandomValue(wristL_score))
        data['wristR_x'].append(round(getRandomValue(wristR_x), 0)) 
        data['wristR_y'].append(round(getRandomValue(wristR_y), 0)) 
        data['wristR_score'].append(getRandomValue(wristR_score))
        data['kneeL_x'].append(round(getRandomValue(kneeL_x), 0)) 
        data['kneeL_y'].append(round(getRandomValue(kneeL_y), 0))
        data['kneeL_score'].append(getRandomValue(kneeL_score)) 
        data['kneeR_x'].append(round(getRandomValue(kneeR_x), 0)) 
        data['kneeR_y'].append(round(getRandomValue(kneeR_y), 0)) 
        data['kneeR_score'].append(getRandomValue(kneeR_score))
        data['hipL_x'].append(round(getRandomValue(hipL_x), 0))
        data['hipL_y'].append(round(getRandomValue(hipL_y), 0)) 
        data['hipL_score'].append(getRandomValue(hipL_score))
        data['hipR_x'].append(round(getRandomValue(hipR_x), 0)) 
        data['hipR_y'].append(round(getRandomValue(hipR_y), 0)) 
        data['hipR_score'].append(getRandomValue(hipR_score)) 
        data['ankleL_x'].append(round(getRandomValue(ankleL_x), 0)) 
        data['ankleL_y'].append(round(getRandomValue(ankleL_y), 0)) 
        data['ankleL_score'].append(getRandomValue(ankleL_score))
        data['ankleR_x'].append(round(getRandomValue(ankleR_x), 0)) 
        data['ankleR_y'].append(round(getRandomValue(ankleR_y), 0)) 
        data['ankleR_score'].append(getRandomValue(ankleR_score))
        line+=1
    pd.DataFrame(data).to_csv(output_file, header=header_str, index=False)
   
if __name__ == "__main__":
    main(sys.argv[1:])  