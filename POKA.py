import random
def make_choice (x,y,field):
    x_size=len(field)
    y_size=len(field[0])
    l=1000
    r=1000
    d=1000
    u=1000
    if x!=0 and field[x-1][y]!=-1:
     for i in range(x,-1,-1):
        if field[i][y]==1:
            l=abs(x-i)
            break
    if y!=0 and field[x][y-1]!=-1:
     for i in range(y,-1,-1):
        if field[x][i]==1:
            u=abs(y-i)
            break
    if x!=x_size and field[x+1][y]!=-1:
     for i in range(x,x_size+1):
        if field[i][y]==1:
            r=abs(x-i)
            break
    if y!=y_size and field[x][y+1]!=-1:
     for i in range(y,y_size+1):
        if field[x][i]==1:
            d=abs(y-i)
            break
    if min(l,u,r,d,1001)==l:
        return 'go_left'
    elif min(l,u,r,d)==u:
        return "go_up"
    elif min(l,u,r,d)==r:
        return "go_right"
    elif min(l,u,r,d)==d:
        return "go_down"
        else:
         return random.choice(['go_down',"go_right","go_up",'go_left'])
