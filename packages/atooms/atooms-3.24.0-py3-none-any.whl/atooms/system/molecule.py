import copy
import numpy
from atooms.system.particle import Particle, cm_position, _periodic_vector_unfolded

# For the network models, like Keating, it does not make much sense to
# use Molecule actually: the system would be one big molecule. One
# could just abuse of the NeighborList so that it does not get updated
# during the simulation! This would also allow bond switches.

class Molecule:

    def __init__(self, particle, bond, angle=None, species=None, cell=None):
        # For consistency with System, we use singular names for variables:
        # particle, bond, etc.
        self.particle = copy.deepcopy(particle)
        self.bond = bond
        if angle is None:
            angle = []
        self.angle = angle
        self.dihedral = []
        self.improper = []
        self.species = species
        if species is None:
            self.species = ''.join([str(p.species) for p in self.particle])
        self.cell = cell
        # Fold particles in cell when using PBCs
        if self.cell:
            for p in self.particle:
                p.fold(self.cell)

    @property
    def center_of_mass(self):
        if self.cell is None:
            return cm_position(self.particle)
        particle = [self.particle[0].nearest_image_of(p, self.cell) for p in self.particle]
        cm = cm_position(particle)
        cm = _periodic_vector_unfolded(cm, self.cell.side)
        return cm

    @center_of_mass.setter
    def center_of_mass(self, position):
        position = numpy.array(position)
        cm = self.center_of_mass
        for p in self.particle:
            p.position += (position - cm)
        if self.cell:
            for p in self.particle:
                p.fold(self.cell)

    @property
    def orientation(self):
        o = []
        cm = self.center_of_mass
        for p in self.particle:
            rij = p.position - cm
            if self.cell:
                rij = _periodic_vector_unfolded(rij, self.cell.side)
            o.append(rij)
        return numpy.array(o)
