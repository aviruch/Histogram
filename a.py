import pandas as pd


#var arrA= [['Length'],[12.2],[9.1],[12.2],[22.9],[0.9],[30.5],[1.8],[3.2]];

g=open("a.txt",'w')

g.write("var arrA= [['Length'],")
df=pd.read_csv("results.csv")
#print df["energy"]
len_df = len(df.index)

count = 1

for i in df["energy"]:
    count = count +1 
    #print i
    if count <len_df:
        a="["+str(i)+"],"
    else:
         a="["+str(i)+"]"   
    
    g.write(a)
    print a

g.write("];")
g.close()