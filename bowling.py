print "Bowling Program"
throw1 = zeros(11)
throw2 = zeros(11)
extra = zeros(11)
game = [throw1, throw2, extra]
i = 0
j = 0
throw = 0
while(i<len(throw1)):
    while(j<2):
        throw = input("Input throw (Frame " + (i+1) + " throw " + (j+1) + "):")
        if(throw==10):
            if(j==0):
                game[i][j]=10
                game[i][j+1]=0
                game[i][j+2]=2
                j=1
            if(j==1):
                game[i][j]=10
                game[i][j+1]=1
        if(j==1 AND game[i][j]+game[i][j-1]==10):
            game[i][j+1]=1
        j=j+1
        if(i==10):
            j=j+1
    if(j>=2):
        j=0
    i=i+1
    if(i==10 AND (game[i-1][0]+game[i-1][1])<10):
        i=11
#now add up scores
