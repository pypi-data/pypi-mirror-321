from .torsion import TorsionAnalysis

class FlexureAnalysis:
    pass 

class PlaneModel:
    def __init__(self, nodes, elems, offset=None):
        self.nodes = nodes 
        self.elems = elems
        self.offset = offset

    def cells(self):
        return [
            elem.nodes for elem in self.elems
        ]

    def translate(self, offset):
        return type(self)(self.nodes-offset, self.elems, self.offset)

class TriangleModel(PlaneModel):

    def rotate(self, angle):
        nodes = self.nodes.copy()
        # nodes[:,0] = 
        return TriangleModel()

    def cell_area(self, tag=None)->float:
        if tag is None:
            return sum(self.cell_area(i) for i in range(len(self.elems)))

        y, z = self.nodes[self.elems[tag].nodes].T
        z1, z2, z3 = z
        y1, y2, y3 = y
        return -float(0.5 * ((y2 - y1) * (z3 - z1) - (y3 - y1) * (z2 - z1)))

#   def integral(self, ua):
#       import numpy as np
#       e = np.ones(ua.shape)
#       return self.inertia(e, ua)

    def inertia(self, va, ua):
        q = 0
        for i,elem in enumerate(self.elems):
            v1, v2, v3 = va[elem.nodes]
            u1, u2, u3 = ua[elem.nodes]
            area = self.cell_area(i)
            # v[nodes].dot(int(N.T@N)@u[nodes])
            q += area/12.0*(u1*(2*v1+v2+v3) + u2*(v1+2*v2+v3) + u3*(v1+v2+2*v3))

        return float(q)

# ------------------------------------------------------------------------
# The following Python code is implemented by Professor Terje Haukaas at
# the University of British Columbia in Vancouver, Canada. It is made
# freely available online at terje.civil.ubc.ca together with notes,
# examples, and additional Python code. Please be cautious when using
# this code; it may contain bugs and comes without warranty of any form.
# ------------------------------------------------------------------------
# https://gist.githubusercontent.com/terjehaukaas/f633c4afc001badb4473d422ccc146e7/raw/2e7d09dbc850dc800c60e1751fb21f2f76615509/SolidCrossSectionAnalysis.py
# https://civil-terje.sites.olt.ubc.ca/files/2020/02/Screenshot-Solid-Cross-section.pdf
#