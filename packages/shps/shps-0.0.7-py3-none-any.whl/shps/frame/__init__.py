from dataclasses import dataclass

from ._patch import (
      _patch as patch,
      layer,
      SectionGeometry
)

class Mesh:
    nodes: list
    elems: list

class Material:
    pass 

@dataclass
class _Fiber:
    # material: Material
    location: tuple
    area:     float
    warp_mode: list
    warp_grad: list

@dataclass
class _Gauss:
    loc: tuple # of float
    wgt: float
    mat: Material

@dataclass
class _Element:
    nodes: tuple # of int
  # gauss: tuple # of Gauss
    shape: str
    model: dict = None

@dataclass
class BasicSection:
    iczy: float
    icyy: float 
    iczz: float
    area: float


    def centroid(self):
        pass

    def translate(self, location):
        pass

def create_mesh(patches: list, mesh_size: list=None):
    from .solvers import TriangleModel 
    from .mesh import sect2gmsh
    mesh = sect2gmsh(patches, mesh_size)
    # meshio object, all tri3s
    GaussT3 = None
    nodes = mesh.points
    elems = [
        _Element(nodes=cell, shape="T3") for cell in mesh.cells[1].data
    ]
    return TriangleModel(nodes, elems) 

def _extract_model(geometry, size)->tuple:
    from .mesh import sect2gmsh
    nodes = {}
    elems = []

    mesh = sect2gmsh(geometry, size)
    # meshio object, all tri3s
    GaussT3 = None
    nodes = mesh.points
    elems = [
        _Element(nodes=cell, gauss=GaussT3, shape="T3") for cell in mesh.cells[1].data
    ]

    return nodes, elems, mesh

def _extract_fibers(geometry, nwarp:int = 0)->list:
    fibers = []
    if isinstance(geometry, list):
        for item in geometry:
            if True:
                fibers.append(_Fiber())

    return fibers

class GeneralSection:
    _point_fibers: "list" # of Fiber

    def __init__(self, geometry,
                 warp_twist=True, 
                 warp_shear=True,
                 eccentricity=None # ey, ez
        ):
        from .solvers import PlaneModel, TriangleModel, TorsionAnalysis, FlexureAnalysis

        if isinstance(geometry, PlaneModel):
            self.model = geometry
        else:
            nodes, elems, _ = _extract_model(geometry)
            self.model = TriangleModel(nodes, elems)

        self._warp_shear = warp_shear 
        self._warp_twist = warp_twist

        nwarp = 0
        if warp_twist:
            nwarp += 1
            self.torsion = TorsionAnalysis(self.model)
            # Update fibers
        else:
            self.torsion = None

        if warp_shear:
            nwarp += 2
            self.flexure = FlexureAnalysis(self.model)
            # Update fibers
        else:
            self.flexure = None

        self._point_fibers = _extract_fibers(geometry, nwarp=nwarp)

    def summary(self, symbols=False):
        s = ""
        tol=1e-13
        cx, cy = self.torsion.centroid()
        cx, cy = map(lambda i: i if abs(i)>tol else 0.0, (cx, cy))

        I = self.torsion.cmm()

        sx, sy = self.torsion.shear_center()
        sx, sy = map(lambda i: i if abs(i)>tol else 0.0, (sx, sy))

        s += f"""
  [nn]  Area                 {self.torsion.model.cell_area()  :>10.4}
        Centroid             {cx :>10.4},{cy :>10.4}
  [mm]  Flexural moments  yy {I[1,1] :>10.4}
                          zz {I[2,2] :>10.4}
                          yz {I[1,2] :>10.4}
        Shear center         {sx :>10.4},{sy :>10.4}
  [ww]  Warping constant     {self.torsion.warping_constant() :>10.4}
        Torsion constant     {self.torsion.torsion_constant() :>10.4}

  [nm]  
        """

        return s


    def add_to(self, model, tag):
        pass

    def translate(self, offset):
        # TODO: translate fibers
        return GeneralSection(self.model.translate(offset),
                              warp_shear=self._warp_shear,
                              warp_twist=self._warp_twist,
                              ) 

    def rotate(self, angle, vector=None):
        pass

    def linearize(self)->BasicSection:
        import numpy as np
        y, z = self.model.nodes.T
        e = np.ones(y.shape)
        return BasicSection(
            area=self.model.inertia(e, e),
            iczy=self.model.inertia(y, z),
            icyy=self.model.inertia(z, z),
            iczz=self.model.inertia(y, y)
        )

    def integrate(self, f: callable):
        pass


    def fibers(self):
        for fiber in self._point_fibers:
            yield fiber

        model = self.model
        for i,elem in enumerate(self.model.elems):
            # TODO: Assumes TriangleModel
            yield _Fiber(
                location=sum(model.nodes[elem.nodes])/3,
                area=model.cell_area(i),
                warp_mode=[

                ],
                warp_grad=[

                ]
            )

