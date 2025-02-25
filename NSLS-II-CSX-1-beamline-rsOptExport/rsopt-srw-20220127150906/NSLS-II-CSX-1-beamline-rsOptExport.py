#!/usr/bin/env python
import os
try:
    __IPYTHON__
    import sys
    del sys.argv[1:]
except:
    pass

from srwpy import srwl_bl
from srwpy import srwlib
from srwpy import srwlpy
import math
from srwpy import srwl_uti_smp

def set_optics(v, names=None, want_final_propagation=True):
    el = []
    pp = []
    if not names:
        names = ['Fixed_Mask', 'Fixed_Mask_M1A', 'M1A', 'M1A_Watchpoint', 'Watchpoint', 'M2A_VDM', 'M2A_VDM_Grating', 'Grating', 'Grating_Aperture', 'Aperture', 'Watchpoint2', 'M3A_HFM', 'M3A_HFM_Watchpoint3', 'Watchpoint3', 'Pinhole', 'Watchpoint4', 'Watchpoint4_Sample', 'Sample']
    for el_name in names:
        if el_name == 'Fixed_Mask':
            # Fixed_Mask: aperture 26.2m
            el.append(srwlib.SRWLOptA(
                _shape=v.op_Fixed_Mask_shape,
                _ap_or_ob='a',
                _Dx=v.op_Fixed_Mask_Dx,
                _Dy=v.op_Fixed_Mask_Dy,
                _x=v.op_Fixed_Mask_x,
                _y=v.op_Fixed_Mask_y,
            ))
            pp.append(v.op_Fixed_Mask_pp)
        elif el_name == 'Fixed_Mask_M1A':
            # Fixed_Mask_M1A: drift 26.2m
            el.append(srwlib.SRWLOptD(
                _L=v.op_Fixed_Mask_M1A_L,
            ))
            pp.append(v.op_Fixed_Mask_M1A_pp)
        elif el_name == 'M1A':
            # M1A: mirror 27.2m
            mirror_file = v.op_M1A_hfn
            assert os.path.isfile(mirror_file), \
                'Missing input file {}, required by M1A beamline element'.format(mirror_file)
            el.append(srwlib.srwl_opt_setup_surf_height_1d(
                srwlib.srwl_uti_read_data_cols(mirror_file, "\t", 0, 1),
                _dim=v.op_M1A_dim,
                _ang=abs(v.op_M1A_ang),
                _amp_coef=v.op_M1A_amp_coef,
                _size_x=v.op_M1A_size_x,
                _size_y=v.op_M1A_size_y,
            ))
            pp.append(v.op_M1A_pp)
        elif el_name == 'M1A_Watchpoint':
            # M1A_Watchpoint: drift 27.2m
            el.append(srwlib.SRWLOptD(
                _L=v.op_M1A_Watchpoint_L,
            ))
            pp.append(v.op_M1A_Watchpoint_pp)
        elif el_name == 'Watchpoint':
            # Watchpoint: watch 40.4m
            pass
        elif el_name == 'M2A_VDM':
            # M2A_VDM: mirror 40.4m
            mirror_file = v.op_M2A_VDM_hfn
            assert os.path.isfile(mirror_file), \
                'Missing input file {}, required by M2A_VDM beamline element'.format(mirror_file)
            el.append(srwlib.srwl_opt_setup_surf_height_1d(
                srwlib.srwl_uti_read_data_cols(mirror_file, "\t", 0, 1),
                _dim=v.op_M2A_VDM_dim,
                _ang=abs(v.op_M2A_VDM_ang),
                _amp_coef=v.op_M2A_VDM_amp_coef,
                _size_x=v.op_M2A_VDM_size_x,
                _size_y=v.op_M2A_VDM_size_y,
            ))
            pp.append(v.op_M2A_VDM_pp)
        elif el_name == 'M2A_VDM_Grating':
            # M2A_VDM_Grating: drift 40.4m
            el.append(srwlib.SRWLOptD(
                _L=v.op_M2A_VDM_Grating_L,
            ))
            pp.append(v.op_M2A_VDM_Grating_pp)
        elif el_name == 'Grating':
            # Grating: grating 40.46m
            mirror = srwlib.SRWLOptMirPl(
                _size_tang=v.op_Grating_size_tang,
                _size_sag=v.op_Grating_size_sag,
                _nvx=v.op_Grating_nvx,
                _nvy=v.op_Grating_nvy,
                _nvz=v.op_Grating_nvz,
                _tvx=v.op_Grating_tvx,
                _tvy=v.op_Grating_tvy,
                _x=v.op_Grating_x,
                _y=v.op_Grating_y,
            )
            opEl=srwlib.SRWLOptG(
                _mirSub=mirror,
                _m=v.op_Grating_m,
                _grDen=v.op_Grating_grDen,
                _grDen1=v.op_Grating_grDen1,
                _grDen2=v.op_Grating_grDen2,
                _grDen3=v.op_Grating_grDen3,
                _grDen4=v.op_Grating_grDen4,
                _e_avg=v.op_Grating_e_avg,
                _cff=v.op_Grating_cff,
                _ang_graz=v.op_Grating_ang,
                _ang_roll=v.op_Grating_rollAngle,
            )
            el.append(opEl)
            pp.append(v.op_Grating_pp)

        elif el_name == 'Grating_Aperture':
            # Grating_Aperture: drift 40.46m
            el.append(srwlib.SRWLOptD(
                _L=v.op_Grating_Aperture_L,
            ))
            pp.append(v.op_Grating_Aperture_pp)
        elif el_name == 'Aperture':
            # Aperture: aperture 42.46m
            el.append(srwlib.SRWLOptA(
                _shape=v.op_Aperture_shape,
                _ap_or_ob='a',
                _Dx=v.op_Aperture_Dx,
                _Dy=v.op_Aperture_Dy,
                _x=v.op_Aperture_x,
                _y=v.op_Aperture_y,
            ))
            pp.append(v.op_Aperture_pp)
        elif el_name == 'Watchpoint2':
            # Watchpoint2: watch 42.46m
            pass
        elif el_name == 'M3A_HFM':
            # M3A_HFM: sphericalMirror 42.46m
            el.append(srwlib.SRWLOptMirSph(
                _r=v.op_M3A_HFM_r,
                _size_tang=v.op_M3A_HFM_size_tang,
                _size_sag=v.op_M3A_HFM_size_sag,
                _nvx=v.op_M3A_HFM_nvx,
                _nvy=v.op_M3A_HFM_nvy,
                _nvz=v.op_M3A_HFM_nvz,
                _tvx=v.op_M3A_HFM_tvx,
                _tvy=v.op_M3A_HFM_tvy,
                _x=v.op_M3A_HFM_x,
                _y=v.op_M3A_HFM_y,
            ))
            pp.append(v.op_M3A_HFM_pp)

        elif el_name == 'M3A_HFM_Watchpoint3':
            # M3A_HFM_Watchpoint3: drift 42.46m
            el.append(srwlib.SRWLOptD(
                _L=v.op_M3A_HFM_Watchpoint3_L,
            ))
            pp.append(v.op_M3A_HFM_Watchpoint3_pp)
        elif el_name == 'Watchpoint3':
            # Watchpoint3: watch 54.36m
            pass
        elif el_name == 'Pinhole':
            # Pinhole: aperture 54.36m
            el.append(srwlib.SRWLOptA(
                _shape=v.op_Pinhole_shape,
                _ap_or_ob='a',
                _Dx=v.op_Pinhole_Dx,
                _Dy=v.op_Pinhole_Dy,
                _x=v.op_Pinhole_x,
                _y=v.op_Pinhole_y,
            ))
            pp.append(v.op_Pinhole_pp)
        elif el_name == 'Watchpoint4':
            # Watchpoint4: watch 54.36m
            pass
        elif el_name == 'Watchpoint4_Sample':
            # Watchpoint4_Sample: drift 54.36m
            el.append(srwlib.SRWLOptD(
                _L=v.op_Watchpoint4_Sample_L,
            ))
            pp.append(v.op_Watchpoint4_Sample_pp)
        elif el_name == 'Sample':
            # Sample: watch 55.5m
            pass
    if want_final_propagation:
        pp.append(v.op_fin_pp)

    return srwlib.SRWLOptC(el, pp)


from pykern.pkdebug import pkdlog
import numpy

# This function is required by rsopt to generate data but is a noop otherwise
def set_rsopt_params_dummy(Aperture_horizontalSize,Aperture_verticalSize,):
    return 0

varParam = [
    ['name', 's', 'NSLS-II CSX-1 beamline', 'simulation name'],

#---Data Folder
    ['fdir', 's', '', 'folder (directory) name for reading-in input and saving output data files'],

#---Electron Beam
    ['ebm_nm', 's', '', 'standard electron beam name'],
    ['ebm_nms', 's', '', 'standard electron beam name suffix: e.g. can be Day1, Final'],
    ['ebm_i', 'f', 0.5, 'electron beam current [A]'],
    ['ebm_e', 'f', 3.0, 'electron beam avarage energy [GeV]'],
    ['ebm_de', 'f', 0.0, 'electron beam average energy deviation [GeV]'],
    ['ebm_x', 'f', 0.0, 'electron beam initial average horizontal position [m]'],
    ['ebm_y', 'f', 0.0, 'electron beam initial average vertical position [m]'],
    ['ebm_xp', 'f', 0.0, 'electron beam initial average horizontal angle [rad]'],
    ['ebm_yp', 'f', 0.0, 'electron beam initial average vertical angle [rad]'],
    ['ebm_z', 'f', 0., 'electron beam initial average longitudinal position [m]'],
    ['ebm_dr', 'f', -1.0234, 'electron beam longitudinal drift [m] to be performed before a required calculation'],
    ['ebm_ens', 'f', 0.00089, 'electron beam relative energy spread'],
    ['ebm_emx', 'f', 7.6e-10, 'electron beam horizontal emittance [m]'],
    ['ebm_emy', 'f', 8e-12, 'electron beam vertical emittance [m]'],
    # Definition of the beam through Twiss:
    ['ebm_betax', 'f', 1.84, 'horizontal beta-function [m]'],
    ['ebm_betay', 'f', 1.17, 'vertical beta-function [m]'],
    ['ebm_alphax', 'f', 0.0, 'horizontal alpha-function [rad]'],
    ['ebm_alphay', 'f', 0.0, 'vertical alpha-function [rad]'],
    ['ebm_etax', 'f', 0.0, 'horizontal dispersion function [m]'],
    ['ebm_etay', 'f', 0.0, 'vertical dispersion function [m]'],
    ['ebm_etaxp', 'f', 0.0, 'horizontal dispersion function derivative [rad]'],
    ['ebm_etayp', 'f', 0.0, 'vertical dispersion function derivative [rad]'],

#---Undulator
    ['und_bx', 'f', 0.0, 'undulator horizontal peak magnetic field [T]'],
    ['und_by', 'f', 0.3513, 'undulator vertical peak magnetic field [T]'],
    ['und_phx', 'f', 0.0, 'initial phase of the horizontal magnetic field [rad]'],
    ['und_phy', 'f', 0.0, 'initial phase of the vertical magnetic field [rad]'],
    ['und_b2e', '', '', 'estimate undulator fundamental photon energy (in [eV]) for the amplitude of sinusoidal magnetic field defined by und_b or und_bx, und_by', 'store_true'],
    ['und_e2b', '', '', 'estimate undulator field amplitude (in [T]) for the photon energy defined by w_e', 'store_true'],
    ['und_per', 'f', 0.0492, 'undulator period [m]'],
    ['und_len', 'f', 1.85, 'undulator length [m]'],
    ['und_zc', 'f', 1.25, 'undulator center longitudinal position [m]'],
    ['und_sx', 'i', -1, 'undulator horizontal magnetic field symmetry vs longitudinal position'],
    ['und_sy', 'i', 1, 'undulator vertical magnetic field symmetry vs longitudinal position'],
    ['und_g', 'f', 6.72, 'undulator gap [mm] (assumes availability of magnetic measurement or simulation data)'],
    ['und_ph', 'f', 0.0, 'shift of magnet arrays [mm] for which the field should be set up'],
    ['und_mdir', 's', '', 'name of magnetic measurements sub-folder'],
    ['und_mfs', 's', '', 'name of magnetic measurements for different gaps summary file'],



#---Calculation Types
    # Electron Trajectory
    ['tr', '', '', 'calculate electron trajectory', 'store_true'],
    ['tr_cti', 'f', 0.0, 'initial time moment (c*t) for electron trajectory calculation [m]'],
    ['tr_ctf', 'f', 0.0, 'final time moment (c*t) for electron trajectory calculation [m]'],
    ['tr_np', 'f', 10000, 'number of points for trajectory calculation'],
    ['tr_mag', 'i', 1, 'magnetic field to be used for trajectory calculation: 1- approximate, 2- accurate'],
    ['tr_fn', 's', 'res_trj.dat', 'file name for saving calculated trajectory data'],
    ['tr_pl', 's', '', 'plot the resulting trajectiry in graph(s): ""- dont plot, otherwise the string should list the trajectory components to plot'],

    #Single-Electron Spectrum vs Photon Energy
    ['ss', '', '', 'calculate single-e spectrum vs photon energy', 'store_true'],
    ['ss_ei', 'f', 10.0, 'initial photon energy [eV] for single-e spectrum vs photon energy calculation'],
    ['ss_ef', 'f', 2000.0, 'final photon energy [eV] for single-e spectrum vs photon energy calculation'],
    ['ss_ne', 'i', 2000, 'number of points vs photon energy for single-e spectrum vs photon energy calculation'],
    ['ss_x', 'f', 0.0, 'horizontal position [m] for single-e spectrum vs photon energy calculation'],
    ['ss_y', 'f', 0.0, 'vertical position [m] for single-e spectrum vs photon energy calculation'],
    ['ss_meth', 'i', 1, 'method to use for single-e spectrum vs photon energy calculation: 0- "manual", 1- "auto-undulator", 2- "auto-wiggler"'],
    ['ss_prec', 'f', 0.01, 'relative precision for single-e spectrum vs photon energy calculation (nominal value is 0.01)'],
    ['ss_pol', 'i', 6, 'polarization component to extract after spectrum vs photon energy calculation: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['ss_mag', 'i', 1, 'magnetic field to be used for single-e spectrum vs photon energy calculation: 1- approximate, 2- accurate'],
    ['ss_ft', 's', 'f', 'presentation/domain: "f"- frequency (photon energy), "t"- time'],
    ['ss_u', 'i', 1, 'electric field units: 0- arbitrary, 1- sqrt(Phot/s/0.1%bw/mm^2), 2- sqrt(J/eV/mm^2) or sqrt(W/mm^2), depending on representation (freq. or time)'],
    ['ss_fn', 's', 'res_spec_se.dat', 'file name for saving calculated single-e spectrum vs photon energy'],
    ['ss_pl', 's', '', 'plot the resulting single-e spectrum in a graph: ""- dont plot, "e"- show plot vs photon energy'],

    #Multi-Electron Spectrum vs Photon Energy (taking into account e-beam emittance, energy spread and collection aperture size)
    ['sm', '', '', 'calculate multi-e spectrum vs photon energy', 'store_true'],
    ['sm_ei', 'f', 10.0, 'initial photon energy [eV] for multi-e spectrum vs photon energy calculation'],
    ['sm_ef', 'f', 2000.0, 'final photon energy [eV] for multi-e spectrum vs photon energy calculation'],
    ['sm_ne', 'i', 2000, 'number of points vs photon energy for multi-e spectrum vs photon energy calculation'],
    ['sm_x', 'f', 0.0, 'horizontal center position [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_rx', 'f', 0.003, 'range of horizontal position / horizontal aperture size [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_nx', 'i', 1, 'number of points vs horizontal position for multi-e spectrum vs photon energy calculation'],
    ['sm_y', 'f', 0.0, 'vertical center position [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_ry', 'f', 0.003, 'range of vertical position / vertical aperture size [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_ny', 'i', 1, 'number of points vs vertical position for multi-e spectrum vs photon energy calculation'],
    ['sm_mag', 'i', 1, 'magnetic field to be used for calculation of multi-e spectrum spectrum or intensity distribution: 1- approximate, 2- accurate'],
    ['sm_hi', 'i', 1, 'initial UR spectral harmonic to be taken into account for multi-e spectrum vs photon energy calculation'],
    ['sm_hf', 'i', 15, 'final UR spectral harmonic to be taken into account for multi-e spectrum vs photon energy calculation'],
    ['sm_prl', 'f', 1.0, 'longitudinal integration precision parameter for multi-e spectrum vs photon energy calculation'],
    ['sm_pra', 'f', 1.0, 'azimuthal integration precision parameter for multi-e spectrum vs photon energy calculation'],
    ['sm_meth', 'i', -1, 'method to use for spectrum vs photon energy calculation in case of arbitrary input magnetic field: 0- "manual", 1- "auto-undulator", 2- "auto-wiggler", -1- dont use this accurate integration method (rather use approximate if possible)'],
    ['sm_prec', 'f', 0.01, 'relative precision for spectrum vs photon energy calculation in case of arbitrary input magnetic field (nominal value is 0.01)'],
    ['sm_nm', 'i', 1, 'number of macro-electrons for calculation of spectrum in case of arbitrary input magnetic field'],
    ['sm_na', 'i', 5, 'number of macro-electrons to average on each node at parallel (MPI-based) calculation of spectrum in case of arbitrary input magnetic field'],
    ['sm_ns', 'i', 5, 'saving periodicity (in terms of macro-electrons) for intermediate intensity at calculation of multi-electron spectrum in case of arbitrary input magnetic field'],
    ['sm_type', 'i', 1, 'calculate flux (=1) or flux per unit surface (=2)'],
    ['sm_pol', 'i', 6, 'polarization component to extract after calculation of multi-e flux or intensity: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['sm_rm', 'i', 1, 'method for generation of pseudo-random numbers for e-beam phase-space integration: 1- standard pseudo-random number generator, 2- Halton sequences, 3- LPtau sequences (to be implemented)'],
    ['sm_fn', 's', 'res_spec_me.dat', 'file name for saving calculated milti-e spectrum vs photon energy'],
    ['sm_pl', 's', '', 'plot the resulting spectrum-e spectrum in a graph: ""- dont plot, "e"- show plot vs photon energy'],
    #to add options for the multi-e calculation from "accurate" magnetic field

    #Power Density Distribution vs horizontal and vertical position
    ['pw', '', '', 'calculate SR power density distribution', 'store_true'],
    ['pw_x', 'f', 0.0, 'central horizontal position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_rx', 'f', 0.03, 'range of horizontal position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_nx', 'i', 100, 'number of points vs horizontal position for calculation of power density distribution'],
    ['pw_y', 'f', 0.0, 'central vertical position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_ry', 'f', 0.03, 'range of vertical position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_ny', 'i', 100, 'number of points vs vertical position for calculation of power density distribution'],
    ['pw_pr', 'f', 1.0, 'precision factor for calculation of power density distribution'],
    ['pw_meth', 'i', 1, 'power density computation method (1- "near field", 2- "far field")'],
    ['pw_zst', 'f', 0., 'initial longitudinal position along electron trajectory of power density distribution (effective if pow_sst < pow_sfi)'],
    ['pw_zfi', 'f', 0., 'final longitudinal position along electron trajectory of power density distribution (effective if pow_sst < pow_sfi)'],
    ['pw_mag', 'i', 1, 'magnetic field to be used for power density calculation: 1- approximate, 2- accurate'],
    ['pw_fn', 's', 'res_pow.dat', 'file name for saving calculated power density distribution'],
    ['pw_pl', 's', '', 'plot the resulting power density distribution in a graph: ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],

    #Single-Electron Intensity distribution vs horizontal and vertical position
    ['si', '', '', 'calculate single-e intensity distribution (without wavefront propagation through a beamline) vs horizontal and vertical position', 'store_true'],
    #Single-Electron Wavefront Propagation
    ['ws', '', '', 'calculate single-electron (/ fully coherent) wavefront propagation', 'store_true'],
    #Multi-Electron (partially-coherent) Wavefront Propagation
    ['wm', '', '', 'calculate multi-electron (/ partially coherent) wavefront propagation', 'store_true'],

    ['w_e', 'f', 750.0, 'photon energy [eV] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ef', 'f', -1.0, 'final photon energy [eV] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ne', 'i', 1, 'number of points vs photon energy for calculation of intensity distribution'],
    ['w_x', 'f', 0.0, 'central horizontal position [m] for calculation of intensity distribution'],
    ['w_rx', 'f', 0.004, 'range of horizontal position [m] for calculation of intensity distribution'],
    ['w_nx', 'i', 100, 'number of points vs horizontal position for calculation of intensity distribution'],
    ['w_y', 'f', 0.0, 'central vertical position [m] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ry', 'f', 0.004, 'range of vertical position [m] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ny', 'i', 100, 'number of points vs vertical position for calculation of intensity distribution'],
    ['w_smpf', 'f', 0.3, 'sampling factor for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_meth', 'i', 1, 'method to use for calculation of intensity distribution vs horizontal and vertical position: 0- "manual", 1- "auto-undulator", 2- "auto-wiggler"'],
    ['w_prec', 'f', 0.01, 'relative precision for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_u', 'i', 1, 'electric field units: 0- arbitrary, 1- sqrt(Phot/s/0.1%bw/mm^2), 2- sqrt(J/eV/mm^2) or sqrt(W/mm^2), depending on representation (freq. or time)'],
    ['si_pol', 'i', 6, 'polarization component to extract after calculation of intensity distribution: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['si_type', 'i', 0, 'type of a characteristic to be extracted after calculation of intensity distribution: 0- Single-Electron Intensity, 1- Multi-Electron Intensity, 2- Single-Electron Flux, 3- Multi-Electron Flux, 4- Single-Electron Radiation Phase, 5- Re(E): Real part of Single-Electron Electric Field, 6- Im(E): Imaginary part of Single-Electron Electric Field, 7- Single-Electron Intensity, integrated over Time or Photon Energy'],
    ['w_mag', 'i', 1, 'magnetic field to be used for calculation of intensity distribution vs horizontal and vertical position: 1- approximate, 2- accurate'],

    ['si_fn', 's', 'res_int_se.dat', 'file name for saving calculated single-e intensity distribution (without wavefront propagation through a beamline) vs horizontal and vertical position'],
    ['si_pl', 's', '', 'plot the input intensity distributions in graph(s): ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],
    ['ws_fni', 's', 'res_int_pr_se.dat', 'file name for saving propagated single-e intensity distribution vs horizontal and vertical position'],
    ['ws_pl', 's', '', 'plot the resulting intensity distributions in graph(s): ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],

    ['wm_nm', 'i', 30000, 'number of macro-electrons (coherent wavefronts) for calculation of multi-electron wavefront propagation'],
    ['wm_na', 'i', 5, 'number of macro-electrons (coherent wavefronts) to average on each node for parallel (MPI-based) calculation of multi-electron wavefront propagation'],
    ['wm_ns', 'i', 5, 'saving periodicity (in terms of macro-electrons / coherent wavefronts) for intermediate intensity at multi-electron wavefront propagation calculation'],
    ['wm_ch', 'i', 0, 'type of a characteristic to be extracted after calculation of multi-electron wavefront propagation: #0- intensity (s0); 1- four Stokes components; 2- mutual intensity cut vs x; 3- mutual intensity cut vs y; 40- intensity(s0), mutual intensity cuts and degree of coherence vs X & Y'],
    ['wm_ap', 'i', 0, 'switch specifying representation of the resulting Stokes parameters: coordinate (0) or angular (1)'],
    ['wm_x0', 'f', 0.0, 'horizontal center position for mutual intensity cut calculation'],
    ['wm_y0', 'f', 0.0, 'vertical center position for mutual intensity cut calculation'],
    ['wm_ei', 'i', 0, 'integration over photon energy is required (1) or not (0); if the integration is required, the limits are taken from w_e, w_ef'],
    ['wm_rm', 'i', 1, 'method for generation of pseudo-random numbers for e-beam phase-space integration: 1- standard pseudo-random number generator, 2- Halton sequences, 3- LPtau sequences (to be implemented)'],
    ['wm_am', 'i', 0, 'multi-electron integration approximation method: 0- no approximation (use the standard 5D integration method), 1- integrate numerically only over e-beam energy spread and use convolution to treat transverse emittance'],
    ['wm_fni', 's', 'res_int_pr_me.dat', 'file name for saving propagated multi-e intensity distribution vs horizontal and vertical position'],
    ['wm_ff', 's', 'ascii', 'format of file name for saving propagated multi-e intensity distribution vs horizontal and vertical position (ascii and hdf5 supported)'],

    ['wm_nmm', 'i', 1, 'number of MPI masters to use'],
    ['wm_ncm', 'i', 100, 'number of Coherent Modes to calculate'],
    ['wm_acm', 's', 'SP', 'coherent mode decomposition algorithm to be used (supported algorithms are: "SP" for SciPy, "SPS" for SciPy Sparse, "PM" for Primme, based on names of software packages)'],
    ['wm_nop', '', '', 'switch forcing to do calculations ignoring any optics defined (by set_optics function)', 'store_true'],

    ['wm_fnmi', 's', '', 'file name of input cross-spectral density / mutual intensity; if this file name is supplied, the initial cross-spectral density (for such operations as coherent mode decomposition) will not be calculated, but rathre it will be taken from that file.'],
    ['wm_fncm', 's', '', 'file name of input coherent modes; if this file name is supplied, the eventual partially-coherent radiation propagation simulation will be done based on propagation of the coherent modes from that file.'],

    ['wm_fbk', '', '', 'create backup file(s) with propagated multi-e intensity distribution vs horizontal and vertical position and other radiation characteristics', 'store_true'],

    # Optics parameters
    ['op_r', 'f', 26.2, 'longitudinal position of the first optical element [m]'],
    # Former appParam:
    ['rs_type', 's', 'u', 'source type, (u) idealized undulator, (t), tabulated undulator, (m) multipole, (g) gaussian beam'],

#---Beamline optics:
    # Fixed_Mask: aperture
    ['op_Fixed_Mask_shape', 's', 'r', 'shape'],
    ['op_Fixed_Mask_Dx', 'f', 0.005, 'horizontalSize'],
    ['op_Fixed_Mask_Dy', 'f', 0.005, 'verticalSize'],
    ['op_Fixed_Mask_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Fixed_Mask_y', 'f', 0.0, 'verticalOffset'],

    # Fixed_Mask_M1A: drift
    ['op_Fixed_Mask_M1A_L', 'f', 1.0, 'length'],

    # M1A: mirror
    ['op_M1A_hfn', 's', 'mirror_1d.dat', 'heightProfileFile'],
    ['op_M1A_dim', 's', 'x', 'orientation'],
    ['op_M1A_ang', 'f', 0.021816600000000002, 'grazingAngle'],
    ['op_M1A_amp_coef', 'f', 0.01, 'heightAmplification'],
    ['op_M1A_size_x', 'f', 0.00545, 'horizontalTransverseSize'],
    ['op_M1A_size_y', 'f', 0.025, 'verticalTransverseSize'],

    # M1A_Watchpoint: drift
    ['op_M1A_Watchpoint_L', 'f', 13.2, 'length'],

    # M2A_VDM: mirror
    ['op_M2A_VDM_hfn', 's', 'mirror_1d.dat', 'heightProfileFile'],
    ['op_M2A_VDM_dim', 's', 'y', 'orientation'],
    ['op_M2A_VDM_ang', 'f', 0.0290353, 'grazingAngle'],
    ['op_M2A_VDM_amp_coef', 'f', 0.01, 'heightAmplification'],
    ['op_M2A_VDM_size_x', 'f', 0.025, 'horizontalTransverseSize'],
    ['op_M2A_VDM_size_y', 'f', 0.1, 'verticalTransverseSize'],

    # M2A_VDM_Grating: drift
    ['op_M2A_VDM_Grating_L', 'f', 0.060000000000002274, 'length'],

    # Grating: grating
    ['op_Grating_hfn', 's', '', 'heightProfileFile'],
    ['op_Grating_dim', 's', 'y', 'orientation'],
    ['op_Grating_size_tang', 'f', 0.3, 'tangentialSize'],
    ['op_Grating_size_sag', 'f', 0.015, 'sagittalSize'],
    ['op_Grating_nvx', 'f', 0.0, 'nvx'],
    ['op_Grating_nvy', 'f', 0.9996571086879139, 'nvy'],
    ['op_Grating_nvz', 'f', -0.026185206696153335, 'nvz'],
    ['op_Grating_tvx', 'f', 0.0, 'tvx'],
    ['op_Grating_tvy', 'f', 0.026185206696153335, 'tvy'],
    ['op_Grating_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Grating_y', 'f', 0.0, 'verticalOffset'],
    ['op_Grating_m', 'f', 1.0, 'diffractionOrder'],
    ['op_Grating_grDen', 'f', 100.0, 'grooveDensity0'],
    ['op_Grating_grDen1', 'f', 0.0548, 'grooveDensity1'],
    ['op_Grating_grDen2', 'f', 3.9e-06, 'grooveDensity2'],
    ['op_Grating_grDen3', 'f', 0.0, 'grooveDensity3'],
    ['op_Grating_grDen4', 'f', 0.0, 'grooveDensity4'],
    ['op_Grating_e_avg', 'f', 750.0, 'energyAvg'],
    ['op_Grating_cff', 'f', 1.2173701951035025, 'cff'],
    ['op_Grating_ang', 'f', 0.0261882, 'grazingAngle'],
    ['op_Grating_rollAngle', 'f', 0.0, 'rollAngle'],
    ['op_Grating_outoptvx', 'f', 0.0, 'outoptvx'],
    ['op_Grating_outoptvy', 'f', 0.05803805908774831, 'outoptvy'],
    ['op_Grating_outoptvz', 'f', 0.998314371176398, 'outoptvz'],
    ['op_Grating_outframevx', 'f', 1.0, 'outframevx'],
    ['op_Grating_outframevy', 'f', 0.0, 'outframevy'],
    ['op_Grating_computeParametersFrom', 'f', 2, 'computeParametersFrom'],
    ['op_Grating_amp_coef', 'f', 0.001, 'heightAmplification'],

    # Grating_Aperture: drift
    ['op_Grating_Aperture_L', 'f', 2.0, 'length'],

    # Aperture: aperture
    ['op_Aperture_shape', 's', 'r', 'shape'],
    ['op_Aperture_Dx', 'f', 0.001, 'horizontalSize'],
    ['op_Aperture_Dy', 'f', 0.001, 'verticalSize'],
    ['op_Aperture_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Aperture_y', 'f', 0.0, 'verticalOffset'],

    # M3A_HFM: sphericalMirror
    ['op_M3A_HFM_hfn', 's', '', 'heightProfileFile'],
    ['op_M3A_HFM_dim', 's', 'x', 'orientation'],
    ['op_M3A_HFM_r', 'f', 846.5455704, 'radius'],
    ['op_M3A_HFM_size_tang', 'f', 0.3, 'tangentialSize'],
    ['op_M3A_HFM_size_sag', 'f', 0.1, 'sagittalSize'],
    ['op_M3A_HFM_ang', 'f', 0.021816600000000002, 'grazingAngle'],
    ['op_M3A_HFM_nvx', 'f', 0.9997620274213104, 'normalVectorX'],
    ['op_M3A_HFM_nvy', 'f', 0.0, 'normalVectorY'],
    ['op_M3A_HFM_nvz', 'f', -0.02181486938835626, 'normalVectorZ'],
    ['op_M3A_HFM_tvx', 'f', 0.02181486938835626, 'tangentialVectorX'],
    ['op_M3A_HFM_tvy', 'f', 0.0, 'tangentialVectorY'],
    ['op_M3A_HFM_amp_coef', 'f', 1.0, 'heightAmplification'],
    ['op_M3A_HFM_x', 'f', 0.0, 'horizontalOffset'],
    ['op_M3A_HFM_y', 'f', 0.0, 'verticalOffset'],

    # M3A_HFM_Watchpoint3: drift
    ['op_M3A_HFM_Watchpoint3_L', 'f', 11.899999999999999, 'length'],

    # Pinhole: aperture
    ['op_Pinhole_shape', 's', 'c', 'shape'],
    ['op_Pinhole_Dx', 'f', 1e-05, 'horizontalSize'],
    ['op_Pinhole_Dy', 'f', 1e-05, 'verticalSize'],
    ['op_Pinhole_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Pinhole_y', 'f', 0.0, 'verticalOffset'],

    # Watchpoint4_Sample: drift
    ['op_Watchpoint4_Sample_L', 'f', 1.1400000000000006, 'length'],

#---Propagation parameters
    ['op_Fixed_Mask_pp', 'f',          [0, 0, 1.0, 0, 0, 1.3, 1.0, 1.3, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Fixed_Mask'],
    ['op_Fixed_Mask_M1A_pp', 'f',      [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Fixed_Mask_M1A'],
    ['op_M1A_pp', 'f',                 [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M1A'],
    ['op_M1A_Watchpoint_pp', 'f',      [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M1A_Watchpoint'],
    ['op_M2A_VDM_pp', 'f',             [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M2A_VDM'],
    ['op_M2A_VDM_Grating_pp', 'f',     [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M2A_VDM_Grating'],
    ['op_Grating_pp', 'f',             [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0580381, 0.998314, 1.0, 0.0], 'Grating'],
    ['op_Grating_Aperture_pp', 'f',    [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Grating_Aperture'],
    ['op_Aperture_pp', 'f',            [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Aperture'],
    ['op_M3A_HFM_pp', 'f',             [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M3A_HFM'],
    ['op_M3A_HFM_Watchpoint3_pp', 'f', [0, 0, 1.0, 1, 0, 1.0, 8.0, 1.0, 16.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M3A_HFM_Watchpoint3'],
    ['op_Pinhole_pp', 'f',             [0, 0, 1.0, 0, 0, 0.1, 20.0, 0.1, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Pinhole'],
    ['op_Watchpoint4_Sample_pp', 'f',  [0, 0, 1.0, 3, 0, 0.3, 1.0, 0.3, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Watchpoint4_Sample'],
    ['op_fin_pp', 'f',                 [0, 0, 1.0, 0, 0, 0.2, 1.0, 0.35, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'final post-propagation (resize) parameters'],

    #[ 0]: Auto-Resize (1) or not (0) Before propagation
    #[ 1]: Auto-Resize (1) or not (0) After propagation
    #[ 2]: Relative Precision for propagation with Auto-Resizing (1. is nominal)
    #[ 3]: Allow (1) or not (0) for semi-analytical treatment of the quadratic (leading) phase terms at the propagation
    #[ 4]: Do any Resizing on Fourier side, using FFT, (1) or not (0)
    #[ 5]: Horizontal Range modification factor at Resizing (1. means no modification)
    #[ 6]: Horizontal Resolution modification factor at Resizing
    #[ 7]: Vertical Range modification factor at Resizing
    #[ 8]: Vertical Resolution modification factor at Resizing
    #[ 9]: Type of wavefront Shift before Resizing (not yet implemented)
    #[10]: New Horizontal wavefront Center position after Shift (not yet implemented)
    #[11]: New Vertical wavefront Center position after Shift (not yet implemented)
    #[12]: Optional: Orientation of the Output Optical Axis vector in the Incident Beam Frame: Horizontal Coordinate
    #[13]: Optional: Orientation of the Output Optical Axis vector in the Incident Beam Frame: Vertical Coordinate
    #[14]: Optional: Orientation of the Output Optical Axis vector in the Incident Beam Frame: Longitudinal Coordinate
    #[15]: Optional: Orientation of the Horizontal Base vector of the Output Frame in the Incident Beam Frame: Horizontal Coordinate
    #[16]: Optional: Orientation of the Horizontal Base vector of the Output Frame in the Incident Beam Frame: Vertical Coordinate
]


_BEAM_TMP_DIR = 'beams'
_DATASET_DIR = 'datasets'
_PARAM_TMP_DIR = 'parameters'
_SRW_OUT_DIR = 'data_files'
_TMP_DIRS = [_BEAM_TMP_DIR, _DATASET_DIR, _PARAM_TMP_DIR, _SRW_OUT_DIR]

def _apply_rotation(angle, norms):
    rx = numpy.array([[1, 0, 0], [0, numpy.cos(angle[0]), -numpy.sin(angle[0])], [0, numpy.sin(angle[0]), numpy.cos(angle[0])]])
    ry = numpy.array([[numpy.cos(angle[1]), 0, numpy.sin(angle[1])], [0, 1, 0], [-numpy.sin(angle[1]), 0, numpy.cos(angle[1])]])
    rz = numpy.array([[numpy.cos(angle[2]), -numpy.sin(angle[2]), 0], [numpy.sin(angle[2]), numpy.cos(angle[2]), 0], [0, 0, 1]])

    rxy = numpy.dot(rx, ry)
    r = numpy.dot(rxy ,rz)

    return numpy.dot(r, norms)


def _get_beamline_param(vp, srw_prefix, sirepo_name):
    for p_arr in vp:
        if p_arr[0].startswith(srw_prefix) and p_arr[3] == sirepo_name:
            return p_arr
    return None


def _read_srw_file(filename):
    from srwpy import uti_plot_com
    """ This function takes in an srw file and returns the beam data. This was adapted from srwl_uti_dataProcess.py file"""
    data, mode, ranges, labels, units = uti_plot_com.file_load(filename)
    data = numpy.array(data).reshape((ranges[8], ranges[5]), order='C')
    '''
    return {'data': data,
            'shape': data.shape,
            'mean': numpy.mean(data),
            'photon_energy': ranges[0],
            'horizontal_extent': ranges[3:5],
            'vertical_extent': ranges[6:8],
            'labels': labels,
            'units': units}
    '''
    return data


def _rsopt_run(filename):
    from pykern import pkio
#    from sirepo.template import template_common
    import h5py
    import multiprocessing
    import time

    # create temporary directories
    for d in _TMP_DIRS:
        pkio.mkdir_parent(d)

    start_time = time.time()
    data = numpy.load(filename)
    tasks = data['x']
    shape = data.dtype['x'].shape
    # if a single parameter varies, rsopt does not put it into an array, so we must
    if not shape:
        tasks = tasks.reshape(len(tasks), -1)
    n_runs = len(tasks)

    n_processes = min(n_runs, multiprocessing.cpu_count() - 1)
    pkdlog(f'Number of processes available: {n_processes}')

    ####################### splits up the number of tasks to be done evenly across the number of processes available and assigns a task cut to each process
    processes = []
    split = n_runs // n_processes
    idx0 = 0
    for j in range(n_processes):
        idx1 = n_runs if j == n_processes - 1 else idx0 + split
        p = multiprocessing.Process(target=_rsopt_run_set, args=(tasks, idx0, idx1, j))
        processes.append(p)
        p.start()
        idx0 += split

    pkdlog('Processes started')

    ####################### must join all processes to end multiprocess thread
    for p in processes:
        pkdlog(f'joining {p}...')
        p.join()
        pkdlog(f'joined {p}')

    end_time = time.time()
    pkdlog(f'Time to run {n_runs} simulations with {n_processes} processes: {numpy.round((end_time - start_time) / 60, 4)}m')

    ###### reads in the temporary storage folder info to create one input and one output file for ML
    beam_arrays = []
    task_arrays = []
    for i in range(n_runs):
        beam_arrays.append(numpy.load(f'{_BEAM_TMP_DIR}/beam_{i}.npy'))
        task_arrays.append(numpy.load(f'{_PARAM_TMP_DIR}/values_{i}.npy'))

    beams_all = numpy.concatenate(beam_arrays, axis=0)
    params_all = numpy.concatenate(task_arrays, axis=0)

    with h5py.File(f'{_DATASET_DIR}/results.h5', 'w') as f:
        f.create_dataset('params', data=['Aperture_horizontalSize','Aperture_verticalSize',])
        f.create_dataset('paramVals', data=params_all.tolist())
        f.create_dataset('beamIntensities', data=beams_all.tolist())
'''
    ###### consolidated input and output file used for ML
    template_common.write_dict_to_h5(
        {
            'params': ['Aperture_horizontalSize','Aperture_verticalSize',],
            'paramVals': params_all.tolist(),
            'beamIntensities': beams_all.tolist(),
        },
        f'{_DATASET_DIR}/results.h5'
    )
'''

def _rsopt_run_set(param_arr, start, end, proc_num):
    pkdlog(f'Process {proc_num} to complete {end - start} tasks')
    task_num = start
    param_set = param_arr[start:end]
    for vals in param_set:
        _rsopt_run_single(vals, proc_num, task_num)
        task_num += 1


def _rsopt_run_single(param_vals, proc_num, task_num):
    vp = _rsopt_set_params(*param_vals)
    f = _get_beamline_param(
        vp,
        'ws_fni',
        'file name for saving propagated single-e intensity distribution vs horizontal and vertical position'
    )
    f[2] = f'{_SRW_OUT_DIR}/res_int_se_{task_num}.dat'
    v = srwl_bl.srwl_uti_parse_options(srwl_bl.srwl_uti_ext_options(vp), use_sys_argv=False)
    names = ['Fixed_Mask','Fixed_Mask_M1A','M1A','M1A_Watchpoint','Watchpoint','M2A_VDM','M2A_VDM_Grating','Grating','Grating_Aperture','Aperture','Watchpoint2','M3A_HFM','M3A_HFM_Watchpoint3','Watchpoint3','Pinhole','Watchpoint4','Watchpoint4_Sample','Sample']
    op = set_optics(v, names, True)
    v.ws = True
    v.ss = False
    v.sm = False
    v.pw = False
    v.si = False
    v.tr = False
    srwl_bl.SRWLBeamline(_name=v.name).calc_all(v, op)

    beam = _read_srw_file(f[2])
    h = beam.shape[0]
    w = beam.shape[1]
    beam = beam.reshape(1, h, w)
    numpy.save(f'{_BEAM_TMP_DIR}/beam_{task_num}.npy', beam)
    numpy.save(f'{_PARAM_TMP_DIR}/values_{task_num}.npy', [param_vals])
    pkdlog(f'Process {proc_num} finished task {task_num}')


# This function actually sets the data
def _rsopt_set_params(Aperture_horizontalSize,Aperture_verticalSize,):
    vp = varParam.copy()
    p = _get_beamline_param(vp, 'op_Aperture', 'horizontalSize')
    if p:
        p[2] = Aperture_horizontalSize
    p = _get_beamline_param(vp, 'op_Aperture', 'verticalSize')
    if p:
        p[2] = Aperture_verticalSize
    return vp


def main():
    import sys
    args = sys.argv[1:]
    if len(args) < 2 or args[0] != 'rsopt_run':
        sys.exit(f'usage: python {sys.argv[0]} rsopt_run <filename>')
    del sys.argv[1:]
    _rsopt_run(args[1])

if __name__ == "__main__":
    main()
