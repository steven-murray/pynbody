import pynbody
import numpy as np

def setup() :
    global f, h
    f = pynbody.load("testdata/g15784.lr.01024")
    h = f.halos()
    

def teardown() :
    global f
    del f


def test_get() :
    current =  f['pos'][0:100:10]
    print current

    correct = np.array([[ 0.01070931, -0.03619793, -0.16635996],
                        [ 0.01066598, -0.0328698 , -0.16544016],
                        [ 0.0080902 , -0.03409814, -0.15953901],
                        [ 0.01125323, -0.03251356, -0.14957215],
                        [ 0.01872441, -0.03908035, -0.16008312],
                        [ 0.01330984, -0.03552091, -0.14454767],
                        [ 0.01438289, -0.03428916, -0.13781759],
                        [ 0.01499815, -0.03602122, -0.13986239],
                        [ 0.0155305 , -0.0332876 , -0.14802328],
                        [ 0.01534095, -0.03525123, -0.14457548]])
    
    print "Position error of ",np.abs(current-correct).sum()
    assert (np.abs(current-correct).sum()<1.e-7)

def test_standard_arrays() :
    # just check all standard arrays are there
    with f.lazy_off :
        f['x']
        f['y']
        f['z']
        f['pos']
        f['vel']
        f['vx']
        f['vy']
        f['vz']
        f['eps']
        f['phi']
        f['mass']
        f.gas['rho']
        f.gas['temp']
        f.gas['metals']
        f.star['tform']
        f.star['metals']
    
    
def test_halo() :
    print "Length=",len(h[1])
    assert len(h[1])==502300

    

def test_loadable_array() :
    assert 'HI' in f.loadable_keys()
    f['HI']
    assert 'HI' in f.keys()

    