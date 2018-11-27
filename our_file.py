"""

made by jeremie kalfon and ...
2nd march 2018
"""
import numpy as np
import utlis as ut


def jerem_fun(mat, rows, columns, vehicles, rides, bonus, steps):

    mat = ut.sort_rides(mat)
    vrid = []
    for i in range(vehicles):
        ve = [[0, 0], []]  # vehicle posx,y, (ridex,y , timeb,e)
        vrid.append(ve)
    ok = False
    vehiok = np.ones(vehicles)
    while vehiok.any() and mat.size != 0:  # check
        for v in range(vehicles):
        	if vehiok[v]:
	            for irid in range(rides):
	                btimu = mat[irid, 2, 0]
	                brid = mat[irid, 0, :]
	                erid = mat[irid, 1, :]
	                etimu = mat[irid, 2, 1]
	                timv = vrid[v][-1][1][1]
	                distbe = dist(brid, vrid[v][0])
	                distrout = dist(brid, erid)
	                num = mat[irid, 3, 0]
	                if distbe + timv == beg:
	                	vrid[v][1].append([brid, [distbe + timv, distbe + timv + distrout], num])
	                	vrid[v][0] = erid
					    mat = np.delete(mat, i)  # bonne dim ?
					    ok = True
	                	break

	            if not ok:
		            for irid in range(rides):
		            	btimu = mat[irid, 2, 0]
		                brid = mat[irid, 0, :]
		                erid = mat[irid, 1, :]
		                etimu = mat[irid, 2, 1]
		                timv = vrid[v][-1][1][1]
		                distbe = dist(brid, vrid[v][0])
		                distrout = dist(brid, erid)
		                num = mat[irid, 3, 0]
		                if distbe + timv == beg:
		                	vrid[v][1].append([brid, [distbe + timv, distbe + timv + distrout], num])
		                	vrid[v][0] = erid
						    mat = np.delete(mat, i)
						    ok = True
		                	break

		        if not ok : 
	            	for irid in range(rides):
	                	btimu = mat[irid, 2, 0]
		                brid = mat[irid, 0, :]
		                erid = mat[irid, 1, :]
		                etimu = mat[irid, 2, 1]
		                timv = vrid[v][-1][1][1]
		                distbe = dist(brid, vrid[v][0])
		                distrout = dist(brid, erid)
		                num = mat[irid, 3, 0]
		                if distbe + timv == beg:
		                	vrid[v][1].append([brid, [distbe + timv, distbe + timv + distrout],num])
		                	vrid[v][0] = erid
						    mat = np.delete(mat, i)
						    ok = True
	                		break
	            if not ok:
	            	vehiok[v] = 0
	            else :
	            	ok = False


def dist(a,b):
	return (b[0]-a[0]) + (b[1]- a[1])
