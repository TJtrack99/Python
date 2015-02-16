print 'bowling program'
throw1 = zeros(11)
throw2 = zeros(11)
extra = zeros(11)
game = [throw1, throw2, extra]
i = 0
j = 0
throw = 0
while(i<len(throw1)):
    while(j<len(throw2):
      throw = input('Input throw:')
      if(throw==10):
          game[i][j] = 10
          if(j==0):
              game[i][j+1]=0
              game[i][j+2]=2
              j=2
              
        j++      
      i++
