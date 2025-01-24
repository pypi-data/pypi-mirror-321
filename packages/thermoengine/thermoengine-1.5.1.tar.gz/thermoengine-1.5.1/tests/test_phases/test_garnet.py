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
# phs = thermo.model.Database().get_phase('Grt')

@mark.xfail
def test_should_return_same_gibbs_as_objc():
    t = 1100.0
    p = 2e4
    mol = 10*np.array([0.2, 0.3, 0.5])
    target = -65375724.92156197

    gibbs_val = phs.gibbs_energy(t, p, mol=mol, deriv=None)
    
    assert allclose(gibbs_val, target)

@mark.xfail
def test_should_return_same_chempot_as_objc():
    t = 1300.0 #1200.0
    p = 1e4 # 2e4
    mol = 10*np.array([0.2, 0.3, 0.5])
    target = np.array([[-6036515.6318096 , -7251706.85585962, -6911549.86389587]])
    deriv = {'dmol':1}

    chempot_val = phs.gibbs_energy(t, p, mol=mol, deriv=deriv)

    assert allclose(target, chempot_val)

@mark.xfail
def test_should_return_same_chempot_gradients_as_objc():
    t = 1300.0 #1200.0
    p = 1e4 # 2e4
    mol = 10*np.array([0.2, 0.3, 0.5])
    target = np.array([[[13368.48 , -2592.295, -3792.015],
                      [-2592.295,  4497.705, -1661.705],
                      [-3792.015, -1661.705,  2513.829]]])
    deriv = {'dmol':2}

    chempot_grads = phs.gibbs_energy(t, p, mol=mol, deriv=deriv)
    # chempot_grads = grt_thermo.gibbs_energy(t, p, mol=mol, deriv=deriv)
    
    assert allclose(target, chempot_grads)

@mark.xfail
def test_should_return_same_affinityAndComp_as_objC():
    t = 1300.0 #1200.0
    p = 1e4 # 2e4
    mol_target = np.array([0.2, 0.3, 0.5])
    aff_target = 0.0

    # mu = grt_thermo.chem_potential(t, p, mol=mol_target)
    mu = np.array([-6036515.6318096, -7251706.85585962, -6911549.86389587])

    print(f'mu = {mu}')

    aff, mol = phs.affinity_and_comp(t, p, mu.squeeze())
    
    assert allclose(mol, mol_target, rtol = 1e-2)
    assert allclose(aff, aff_target, atol= 1e-2)

@mark.xfail
def test_should_return_same_elem_comp_as_objc():
    mol_endms = np.array([0.2, 0.3, 0.5])
    target = np.array([ 0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. , 12. ,  0. ,  0. ,
                        0. ,  1.5,  2. ,  3. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0.9,  0. ,
                        0. ,  0. ,  0. ,  0. ,  0.6,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,
                        0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,
                        0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,
                        0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,
                        0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,
                        0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,
                        0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,
                        0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ])
    
    # print(grt_thermo.props['element_comp'].__repr__())
    mol_elems = phs.convert_endmember_comp(mol_endms, output='moles_elements')

    
    # print(mol_elems.__repr__())
    assert allclose(mol_elems, target)

@mark.xfail
def test_contents_of_props_dict_are_correct():
    print (phs.props['formula'].__repr__())
    print(phs.props['molwt'].__repr__())
    print(phs.props['endmember_name'].__repr__())
    assert phs.props['endmember_num'] == 3

    assert np.all(phs.props['endmember_name'] == ['almandine', 'grossular', 'pyrope'])
    assert np.all((phs.props['formula'] == 
                   ['Fe3Al2Si3O12', 'Ca3Al2Si3O12', 'Mg3Al2Si3O12']))
    assert allclose(phs.props['molwt'], np.array([497.75338, 450.45238, 403.12738]))
    
@mark.xfail
def test_comp_is_valid():

    comp_valid = np.array([.2,.2,.6])
    comp_invalid = np.array([-.2,.2,.6])

    assert phs.test_endmember_comp(comp_valid) == True
    assert phs.test_endmember_comp(comp_invalid) == False