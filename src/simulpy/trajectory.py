import numpy as np
from simulpy import kin


# create the matrix to plot the robot arm
def calctrajectorymat(thetamat, robobj):

    i = 0
    nopoints = len(thetamat)
    trajectorymat = np.zeros((nopoints, robobj.jointno + 1, 3))

    while i < nopoints:
        trajectorymat[i] = kin.fwd(robobj, thetamat[i])
        i = i + 1

    return trajectorymat


# create list of joint angles from initial to final position of the robot
def calctrac(robobj, thetainit, thetafinal, nopoints):

    thetamat = np.zeros((nopoints + 2, robobj.jointno))
    thetamat[0] = thetainit

    i = 1
    while i < nopoints + 2:
        j = 0
        while j < robobj.jointno:
            thetamat[i][j] = thetainit[j] + i*thetafinal[j]/(nopoints+1)
            j = j + 1
        i = i + 1

    return calctrajectorymat(thetamat, robobj)


def linetrac(robobj, pt1, pt2):
    x = np.linspace(pt1[0], pt2[0])
    y = np.linspace(pt1[1], pt2[1])
    z = np.linspace(pt1[2], pt2[2])

    i = 0
    thetamat = np.zeros((len(x), 3))

    while i < len(x):
        thetamat[i] = kin.inv(robobj, [x[i], y[i], z[i]])
        i = i + 1

    return calctrajectorymat(thetamat, robobj)