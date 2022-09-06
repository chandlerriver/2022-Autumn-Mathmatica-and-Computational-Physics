import numpy as np
import random
import math

num_floor = 16
height_floor = 3.5
floormax = 64
elevator_max = 13
locmin = 0
locmax = height_floor * num_floor
accmax = 1
droom = np.zeros((num_floor,3))
elevator = {loc:0,verb:0,acc:0,dire:1,runtime:0,tar:0,room:np.zeros()}

random_floor = 5
random_start = [20,40]


def cal_acc():
    global accmax
    global elevator
    global locmin
    global locmax
    
    assert(locmin<elevator[loc]<locmax)
    if elevator[dire] == 1:
        c = math.ceil(loc/height)-1
        for i in range(c,num_floor):
            if droom[i][1] > 0:
                distance = height_floor * i - elevator[loc]
                if elevator[verb]**2/2/distance < accmax:
                    elevator[acc] = elevator[verb]**2/2/distance
                    elevator[tar] = i
        
    elif elevator[dire] == -1:
        c = math.floor(loc/height)-1
        for i in range(0,c):
            if droom[i][2] > 0:
                distance = height_floor * i - elevator[loc]
                if elevator[verb]**2/2/distance < accmax:
                    elevator[acc] = elevator[verb]**2/2/distance
                    elevator[tar] = i
                    
def init_droom():
    global droom
    global num_floor
    if droom == np.zeros((16,2)):
        for i in range(num_floor):
            droom[i][1] = random.randrange(0,random_floor)
            droom[i][0] = random.randrange(random_start[0],random_start[1])
    else:
        for i in range(num_floor):
            #droom[i][0] += random.randrange(0,floormax - droom[i][0])
            k = random.randrange(0,random_floor)
            droom[i][0] -= min(k,droom[i][0])
            droom[i][1] += min(k,droom[i][0])
            k = random.randrange(0,random_floor)
            droom[i][0] -= min(k,droom[i][0])
            droom[i][2] += min(k,droom[i][0])
    return droom

def run_ele():
    global elevator
    if elevator[dire] == 1:
        assert(elevator[tar]*height_floor > elevator[loc])
        elevator[rumtime] += elevator[verb]/elevator[acc]
        elevator[room] += min(elevator_max,droom[elevator[tar]][1])


    
if __name__ == "__main__":
count_time = 0
count = 10
while count:
    droom = init_droom()
    cal_acc()
    run_ele()
    count -= 1
    
