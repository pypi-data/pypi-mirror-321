from shadow4.beamline.s4_beamline import S4Beamline
from shadow4.tools.logger import is_verbose, is_debug, set_verbose

# set_verbose()

beamline = S4Beamline()

#
#
#
from shadow4.sources.source_geometrical.source_geometrical import SourceGeometrical
light_source = SourceGeometrical(name='SourceGeometrical', nrays=1000, seed=5676563)
light_source.set_spatial_type_point()
light_source.set_depth_distribution_off()
light_source.set_angular_distribution_flat(hdiv1=0.000000,hdiv2=0.000000,vdiv1=0.000000,vdiv2=0.000000)
light_source.set_energy_distribution_singleline(12914.000000, unit='eV')
light_source.set_polarization(polarization_degree=1.000000, phase_diff=0.000000, coherent_beam=0)
beam = light_source.get_beam()

beamline.set_light_source(light_source)

# optical element number XX
from shadow4.beamline.optical_elements.crystals.s4_plane_crystal import S4PlaneCrystal
optical_element = S4PlaneCrystal(name='Plane Crystal',
    boundary_shape=None, material='Si',
    miller_index_h=8, miller_index_k=0, miller_index_l=0,
    f_bragg_a=False, asymmetry_angle=0.0,
    is_thick=1, thickness=0.001,
    f_central=1, f_phot_cent=0, phot_cent=12914.0,
    file_refl='Si(800)_12890_12940.dat',
    f_ext=0,
    material_constants_library_flag=0, # 0=xraylib,1=dabax,2=preprocessor v1,3=preprocessor v2
    method_efields_management=0, # 0=new in S4; 1=like in S3
    )
from syned.beamline.element_coordinates import ElementCoordinates
coordinates = ElementCoordinates(p=0, q=0.005657, angle_radial=0.7853355061, angle_azimuthal=0, angle_radial_out=0.7853355061)
movements = None
from shadow4.beamline.optical_elements.crystals.s4_plane_crystal import S4PlaneCrystalElement
beamline_element = S4PlaneCrystalElement(optical_element=optical_element,coordinates=coordinates, movements=movements, input_beam=beam)

beam, mirr = beamline_element.trace_beam()

beamline.append_beamline_element(beamline_element)


# test plot
if 0:
   from srxraylib.plot.gol import plot_scatter
   plot_scatter(beam.get_photon_energy_eV(nolost=1), beam.get_column(23, nolost=1), title='(Intensity,Photon Energy)', plot_histograms=0)
   plot_scatter(1e6 * beam.get_column(1, nolost=1), 1e6 * beam.get_column(3, nolost=1), title='(X,Z) in microns')

print(f'{beam.get_intensity(polarization=0):.6g} {beam.get_intensity(polarization=1):.6g} {beam.get_intensity(polarization=2):.6g}')
print(beam.get_column(23)[0:5], beam.get_column(24)[0:5], beam.get_column(25)[0:5])
