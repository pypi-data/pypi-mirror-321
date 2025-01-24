from __future__ import annotations # Enable Python 4 type hints in Python 3

from typing import List

from pytest import mark
import numpy as np
import pandas as pd
from scipy import optimize as opt

import thermoengine as thermo
import thermoengine.model
import thermoengine.phases
# import thermoengine.equilibrate
from numpy import allclose

# Load phase once implemented
# phs = thermo.model.Database(liq_mod='v1.0').get_phase('Liq')

T = 1673.0
P = 1e4

compDB = thermoengine.model.GeoCompDB()
MORB_comp = compDB.get_syscomp('MORB')
MORB_mol_oxides = MORB_comp.mol_comp(components='oxides').iloc[0]
MORB_mol_oxides['CO2'] = 0.0

mol_oxides = MORB_mol_oxides.values

# Uncomment once phase implemented
# mol = phs.calc_endmember_comp(mol_oxides, method='intrinsic')

@mark.xfail
def test_should_return_same_gibbs_as_objc():
    target = -1695279.8043334917

    gibbs_val = phs.gibbs_energy(T, P, mol=mol, deriv=None)
    print(gibbs_val)
    
    assert allclose(gibbs_val, target)

@mark.xfail
def test_should_return_same_chempot_as_objc():
    # THIS TEST IS FLAKY POSSIBLY DUE TO MEMORY ISSUE IN RUBICON
    # ACTIVATE TEST AND VALIDATE VALS WHEN REPLACED WITH CODER PHASE
    target = np.array([[-1062735.70490184, -1154582.74411342, -1918325.21684312,
                        -1202580.25015512, -2175135.12861048, -1982776.19908715,
                        -1343177.84422034, -2528622.46597489, -1134069.61562785,
                        -1190388.93458176, -1916686.45367498, -2043508.37993188,
                        -2605601.84451424, -4890335.89065307,  -491867.4678311 ]])
    deriv = {'dmol':1}

    chempot_val = phs.gibbs_energy(T, P, mol=mol, deriv=deriv)
    print(chempot_val.__repr__())
    print(target - chempot_val)

    assert allclose(target, chempot_val)

@mark.xfail
def test_should_return_same_chempot_gradients_as_objc():
    # THIS TEST IS FLAKY POSSIBLY DUE TO MEMORY ISSUE IN RUBICON
    # ACTIVATE TEST AND VALIDATE VALS WHEN REPLACED WITH CODER PHASE
    target = np.array([[[ 2.37420262e+04,  7.01184615e+01, -1.86525233e+04,
                          2.64489604e+03, -3.72141512e+03,  6.91270137e+03,
                          3.32072621e+03, -5.64075743e+03, -4.35671772e+02,
                        -8.32598780e+02, -7.87040171e+03, -3.48248335e+04,
                        -3.88316922e+04, -6.76190228e+02, -1.45895666e+04],
                        [ 7.01184615e+01,  1.06747893e+06, -2.03600334e+04,
                        -8.82503777e+04, -1.00985852e+05, -1.92555254e+04,
                        -3.68214743e+04, -2.23694021e+04, -2.93270907e+04,
                        -2.52533830e+04, -4.80051219e+04,  2.77926785e+04,
                        -6.12781011e+04, -4.20669119e+04,  1.95751618e+04],
                        [-1.86525233e+04, -2.03600334e+04,  1.23955482e+05,
                          8.75847504e+03, -2.75786941e+04, -1.21722067e+04,
                        -3.15067345e+04, -9.18342948e+03,  8.27645609e+03,
                          1.19954565e+04, -2.94640946e+04, -3.44052730e+04,
                        -3.78641382e+03,  1.89445370e+04, -2.74949298e+04],
                        [ 2.64489604e+03, -8.82503777e+04,  8.75847504e+03,
                          2.49967101e+06, -9.35527013e+02, -1.61171024e+05,
                        -1.03067523e+03, -6.25751324e+04, -1.37484353e+04,
                        -5.65413098e+03,  1.16337887e+04, -7.06086298e+04,
                          4.89848032e+04, -4.99266018e+04, -5.95979221e+03],
                        [-3.72141512e+03, -1.00985852e+05, -2.75786941e+04,
                        -9.35527013e+02,  4.93119075e+06, -1.01156176e+05,
                        -2.78387591e+04,  1.61185633e+04, -3.79029116e+04,
                        -2.93611784e+04,  4.26902589e+03,  1.34851108e+05,
                          4.12069690e+04, -6.51826030e+04, -5.68441380e+04],
                        [ 6.91270137e+03, -1.92555254e+04, -1.21722067e+04,
                        -1.61171024e+05, -1.01156176e+05,  2.63698948e+05,
                        -1.96234893e+04, -4.20321045e+04, -3.81660870e+04,
                        -2.49347886e+04, -1.94108367e+04, -2.84365425e+04,
                          1.02344694e+04,  2.05105647e+04, -1.74202747e+04],
                        [ 3.32072621e+03, -3.68214743e+04, -3.15067345e+04,
                        -1.03067523e+03, -2.78387591e+04, -1.96234893e+04,
                          9.33472468e+11, -1.99790336e+04, -2.16893497e+04,
                        -1.37724860e+04, -4.58690692e+03,  3.75734504e+04,
                          1.12916134e+04, -5.45302401e+04, -4.15454393e+04],
                        [-5.64075743e+03, -2.23694021e+04, -9.18342948e+03,
                        -6.25751324e+04,  1.61185633e+04, -4.20321045e+04,
                        -1.99790336e+04,  1.44581908e+05, -3.67293936e+04,
                        -2.27090931e+04, -3.06780246e+04,  1.89369279e+04,
                          1.41321951e+04, -7.06553684e+04, -6.48894042e+03],
                        [-4.35671772e+02, -2.93270907e+04,  8.27645609e+03,
                        -1.37484353e+04, -3.79029116e+04, -3.81660870e+04,
                        -2.16893497e+04, -3.67293936e+04,  9.33472448e+11,
                        -2.31774116e+04, -1.07010042e+04,  3.84526897e+04,
                        -1.53141834e+04, -6.42043710e+04, -5.12195702e+04],
                        [-8.32598780e+02, -2.52533830e+04,  1.19954565e+04,
                        -5.65413098e+03, -2.93611784e+04, -2.49347886e+04,
                        -1.37724860e+04, -2.27090931e+04, -2.31774116e+04,
                          9.33472466e+11, -3.13806162e+04,  5.07319841e+04,
                        -1.01453015e+04, -5.55600006e+04, -4.25751998e+04],
                        [-7.87040171e+03, -4.80051219e+04, -2.94640946e+04,
                          1.16337887e+04,  4.26902589e+03, -1.94108367e+04,
                        -4.58690692e+03, -3.06780246e+04, -1.07010042e+04,
                        -3.13806162e+04,  6.16067977e+04,  4.53365511e+04,
                          1.10959786e+04, -1.67269579e+04, -1.82641963e+04],
                        [-3.48248335e+04,  2.77926785e+04, -3.44052730e+04,
                        -7.06086298e+04,  1.34851108e+05, -2.84365425e+04,
                          3.75734504e+04,  1.89369279e+04,  3.84526897e+04,
                          5.07319841e+04,  4.53365511e+04,  4.40624965e+05,
                          6.03253457e+04,  2.30127262e+04, -6.18640405e+04],
                        [-3.88316922e+04, -6.12781011e+04, -3.78641382e+03,
                          4.89848032e+04,  4.12069690e+04,  1.02344694e+04,
                          1.12916134e+04,  1.41321951e+04, -1.53141834e+04,
                        -1.01453015e+04,  1.10959786e+04,  6.03253457e+04,
                          2.18332172e+07, -3.63039515e+04, -2.91698214e+04],
                        [-6.76190228e+02, -4.20669119e+04,  1.89445370e+04,
                        -4.99266018e+04, -6.51826030e+04,  2.05105647e+04,
                        -5.45302401e+04, -7.06553684e+04, -6.42043710e+04,
                        -5.55600006e+04, -1.67269579e+04,  2.30127262e+04,
                        -3.63039515e+04,  2.45839292e+07, -4.55827148e+04],
                        [-1.45895666e+04,  1.95751618e+04, -2.74949298e+04,
                        -5.95979221e+03, -5.68441380e+04, -1.74202747e+04,
                        -4.15454393e+04, -6.48894042e+03, -5.12195702e+04,
                        -4.25751998e+04, -1.82641963e+04, -6.18640405e+04,
                        -2.91698214e+04, -4.55827148e+04,  1.10814837e+05]]])
    
    
    deriv = {'dmol':2}

    chempot_grads = phs.gibbs_energy(T, P, mol=mol, deriv=deriv)
    print(chempot_grads.__repr__())
    print(chempot_grads - target)
    
    assert allclose(target, chempot_grads)

@mark.xfail
def test_should_return_same_affinityAndComp_as_objC():
    # NOTE: ObjC Liquids do not have a built-in "intrinsic" affinity_and_comp algorithm
    #       Therefore it must rely on the generic algo which is less accurate
    #       Expect we should tighten TOL to .01 J once replaced w/ coder Liquid
    TOL_GENERIC_ALGO_AFF = 5
    TOL_GENERIC_ALGO_MOL = 5e-2

    mol_target = mol.copy()
    aff_target = 0.0

    mu = phs.chem_potential(T, P, mol=mol_target)
    # print(mu.__repr__())

    aff, mol_calc = phs.affinity_and_comp(T, P, mu.squeeze())

    print(mol_calc.__repr__())
    print(aff)
    
    assert allclose(mol_calc, mol_target, atol = TOL_GENERIC_ALGO_MOL)
    assert allclose(aff, aff_target, atol= TOL_GENERIC_ALGO_AFF)

@mark.xfail
def test_should_return_same_elem_comp_as_objc():
    target = np.array([0.00000000e+00, 3.33052089e-01, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       2.87068619e+00, 0.00000000e+00, 0.00000000e+00, 8.55129178e-02,
                       1.89309356e-01, 3.46013702e-01, 7.88891607e-01, 1.12720097e-03,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 6.36919687e-04,
                       2.21828336e-01, 0.00000000e+00, 1.26409909e-02, 0.00000000e+00,
                       5.59246583e-03, 0.00000000e+00, 1.11081861e-01, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                       0.00000000e+00, 0.00000000e+00, 0.00000000e+00])
    
    mol_elems = phs.convert_endmember_comp(mol, output='moles_elements')

    
    print(mol_elems.__repr__())
    assert allclose(mol_elems, target)

@mark.xfail
def test_contents_of_props_dict_are_correct():
    print (phs.props['formula'].__repr__())
    print(phs.props['molwt'].__repr__())
    print(phs.props['endmember_name'].__repr__())
    
    assert phs.props['endmember_num'] == 15 

    assert np.all(phs.props['endmember_name'] == np.array(['SiO2', 'TiO2', 'Al2O3', 'Fe2O3', 'MgCr2O4', 'Fe2SiO4',
                                                          'MnSi0.5O2', 'Mg2SiO4', 'NiSi0.5O2', 'CoSi0.5O2', 'CaSiO3',
                                                          'Na2SiO3', 'KAlSiO4', 'Ca3(PO4)2', 'H2O'], dtype='<U9'))
    assert np.all((phs.props['formula'] == ['SiO2', 'TiO2', 'Al2O3', 'Fe2O3', 'MgCr2O4', 
                                           'Fe2SiO4', 'MnSi0.5O2', 'Mg2SiO4', 'NiSi0.5O2', 'CoSi0.5O2', 'CaSiO3',
                                           'Na2SiO3', 'KAlSiO4', 'Ca3(PO4)2', 'H2O']))
    
    molwt_target = np.array([ 60.0843 ,  79.8988 , 101.96128, 159.6922 , 192.2946 , 203.7771 ,
                             100.97955, 140.6931 , 104.75155, 104.97475, 116.1637 , 122.06324,
                             158.16664, 310.18272,  18.0152 ])
    
    assert allclose(phs.props['molwt'], molwt_target)
    
@mark.xfail
def test_valid_comp():

    comp_valid = mol

    assert phs.test_endmember_comp(comp_valid) == True
    
@mark.xfail
def test_invalid_comp_negative_mol():

    comp_invalid = mol.copy()
    comp_invalid[0] = -mol[0]
    assert phs.test_endmember_comp(comp_invalid) == False

@mark.xfail
def test_invalid_comp_number_of_components():
    # NOTE: This test fails for Objective C liquid phase because Rubicon does not validate
    #       array lengths. Python code and/or coder liquid should fix this issue. 
    # TODO: Updating python code would fix this common bug trap for everyone
    comp_invalid = np.zeros(16)
    comp_invalid[:15] = mol
    assert phs.test_endmember_comp(comp_invalid) == False
