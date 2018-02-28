

import numpy as np


def divide_and_conqueer(mat, L, H):
    """
    heyyy
    """
    return 0


def rec(mat, L, h):
    lt = 0
    lm = 0
    h = 0
    mask = np.zeros(mat.shape)
    deb = np.array([0, 0])
    end = np.array([0, 0])
    total = 0
    while np.equal(deb, mat.shape):
	    val, tot, deb, end = add(mat, mask, deb, end + np.array([0, 1]), lm, lt, l, h)
	    if val:
	    	mask[deb[0]:end[0], deb[1]:end[1]] = False
	    	total += tot
	    if deb[0] != mat.shape[0]:
	   		deb += np.array([1, 0])
	   	else :
	   		deb = np.array([0,deb[1]+1])
	return mask, total



def add(mat, mask, deb, end, lm, lt, l, h):
	if mask[end]:
		a = (end + np.array([1, 1])) - deb
		tot = a[0] * a[1]
	    if tot <= h:
        	if i:
                lt += 1
            else:
                lm += 1
            mask[end]=False
            if lt >=l and lm >=l:
            	return True, tot, deb, end
            else :
            	val, tot, deb, end = add(mat, mask, deb, end+np.array([0,1]), lm, lt, l, h)
            	if val: return True, tot, deb, end
            	val, tot, deb, end = add(mat, mask, deb, end+np.array([1,0]), lm, lt, l, h)
            	if val: return True, tot, deb, end
    return False, None, None, None
        
  
