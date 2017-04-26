import vrep, math
import sys
# child threaded script: 
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
#啟動模擬
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
 
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
errorCode,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint1',vrep.simx_opmode_oneshot_wait)
 
deg = math.pi/180
 
if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
 
#errorCode=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint_handle,2, vrep.simx_opmode_oneshot_wait)
 
def setJointPosition(incAngle, steps):
    for i  in range(steps):
        errorCode=vrep.simxSetJointPosition(clientID, Revolute_joint_handle, i*incAngle*deg, vrep.simx_opmode_oneshot_wait)
    #終止模擬
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
 
# 每步 10 度, 轉兩圈
setJointPosition(10, 72)