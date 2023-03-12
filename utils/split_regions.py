import os
import glob
import pandas as pd

def split_helper(file, name, export):
    df_file = pd.read_csv(file)

    #Transient1 separation
    cutoff = 1.65

    l = df_file.vinp[df_file.vinp>cutoff].index.tolist()
    df_transient1 = df_file[0:l[1]]

    #peak1 within transient1
    r1 = df_transient1.xpd[df_transient1.xpd==0].index.tolist()
    df_rise1 = df_file[0:r1[-1]+1]

    print(export)
    print(name)
    csvname = export+"\\rise1\\"+name
    df_rise1.to_csv(csvname)
    #---------------------------------------

    #peak2 within Transient1
    r2 = df_transient1.vinp[df_transient1.vinp>0].index.tolist()
    df_rise2 = df_file[r1[-1]:r2[0]+1]
    csvname = export+"\\rise2\\"+name
    df_rise2.to_csv(csvname)

    #rise3
    df_rise3 = df_file[r2[0]:l[1]]
    csvname = export+"\\rise3\\"+name
    df_rise3.to_csv(csvname)

    #Functional region split
    df_rest = df_file[l[1]:]
    xpd0list = df_rest.pd[df_rest.pd != 0].index.tolist()
    m = xpd0list[0]+1
    df_functional = df_file[l[1]:m]
    csvname = export+"\\functional\\"+name
    df_functional.to_csv(csvname)
    
    #Transient2
    df_t2 = df_file[m:]
    csvname = export+"\\fall\\"+name
    df_t2.to_csv(csvname)

def split(path, export):
    # path = "D:\\Final Year Project\\Play with DWT\\Sine\\dataset\\sine 750 mv\\test\*.csv"
    # export = "D:\\Final Year Project\\Split Defect\\normal\\"

    count = 0
    t1 = glob.glob(path + "\\*.csv")
    for file in t1:
        count = count+1
        print ("\nFile ", count)
        print ("---------------")
        
        name = os.path.basename(file)
        print ("name = ", name)
        
        split_helper(file, name, export)
