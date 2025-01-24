from __future__ import annotations # Enable Python 4 type hints in Python 3

import numpy as np
import pandas as pd
from pytest import raises

import thermoengine as thermo
from thermoengine import chemistry, chem_library
from thermoengine.core import UnorderedList
from thermoengine.chemistry import OxideMolComp, OxideWtComp, ElemMolComp, Oxides, OxideWt

from utils_testing import are_close, are_roughly_close, dict_values_are_close

from typing import List, Set, Dict, Tuple, Optional


class TestComp:
    def test_should_define_simple_elemental_compositions_by_chemical_formula(self):
        ox = ElemMolComp.get_by_formula('MgO')
        assert ox.comp == {'Mg':1,'O':1}

        assert ElemMolComp.get_by_formula('K2O') == ElemMolComp(K=2, O=1)
        assert ElemMolComp.get_by_formula('Al2O3') == {'Al': 2, 'O':3}
        assert ElemMolComp.get_by_formula('Mg2SiO4') == {'Mg': 2, 'Si':1, 'O': 4}

    def test_should_compare_approximately_equal_compositions(self):
        assert ElemMolComp(Si=1, O=2) == ElemMolComp(Si=1.0000001, O=2)
        assert not ElemMolComp(Si=1, O=2) == ElemMolComp(Si=1.01, O=2)

    def test__should_compare_comp_objects_enabling_ordering(self):
        H = ElemMolComp(H=1)
        Fe = ElemMolComp(Fe=1)

        assert H.sort_index < Fe.sort_index
        assert H < Fe
        assert Oxides.SiO2 < Oxides.Fe2O3


    def test_should_retrieve_oxides(self):
        assert Oxides.SiO2 == {'Si':1, 'O':2}
        assert Oxides.Cr2O3 == {'Cr':2, 'O':3}

    def test_should_add_elemental_compositions(self):
        assert (
                ElemMolComp.get_by_formula('MgO') +
                ElemMolComp.get_by_formula('SiO2') ==
                ElemMolComp.get_by_formula('MgSiO3')
        )

    def test_should_add_oxides(self):
        assert (Oxides.MgO + Oxides.SiO2 ==
                ElemMolComp.get_by_formula('MgSiO3'))
        assert (2 * Oxides.MgO + Oxides.SiO2 ==
                ElemMolComp.get_by_formula('Mg2SiO4'))

    def test_should_add_oxide_comps(self):
        MgO = OxideMolComp(MgO=1)
        SiO2 = OxideMolComp(SiO2=1)
        MgSiO3 = OxideMolComp(MgO=1, SiO2=1)

        assert MgO + SiO2 == MgSiO3

    def test_should_compare_oxide_comps_with_no_shared_components(self):
        MgO, SiO2 = OxideMolComp(MgO=1), OxideMolComp(SiO2=1)
        assert MgO == OxideMolComp(MgO=1)
        assert not MgO == SiO2

    def test_should_calc_linear_combination_of_oxide_comps(self):
        MgO, SiO2, Mg2SiO4 = OxideMolComp(MgO=1), OxideMolComp(SiO2=1), OxideMolComp(MgO=2, SiO2=1)
        Mg2SiO4_elems = ElemMolComp.get_by_formula('Mg2SiO4')
        components = np.array([MgO, SiO2])

        assert 2*MgO + SiO2 == Mg2SiO4
        assert MgO*2 + SiO2 == Mg2SiO4
        assert components.dot([2, 1]) == Mg2SiO4
        assert components.dot([2, 1]) == Mg2SiO4_elems

    def test_should_represent_empty_oxide_comp_as_default(self):
        empty_comp = OxideMolComp()

        assert empty_comp.data_is_empty
        assert empty_comp == {}

    def test__should_get_non_default_data_from_oxide_comp(self):
        comp = OxideMolComp(MgO=1, SiO2=1)
        assert {'MgO':1, 'SiO2':1} == comp.data

    def test__should_get_non_default_data_from_elem_comp(self):
        comp = ElemMolComp(**{'Mg': 1, 'Si': 1, 'O': 3})
        assert {'Mg':1, 'Si': 1, 'O': 3} == comp.data

    def test_should_get_nonzero_values_from_oxide_comp(self):
        comp = OxideMolComp(MgO=1, SiO2=1)
        assert not np.any(comp.values==0)

    def test_should_get_nonzero_values_from_elem_comp(self):
        comp = ElemMolComp(**{'Mg': 1, 'Si': 1, 'O': 3})
        assert not np.any(comp.values==0)

    def test_should_get_all_values_from_oxide_comp(self):
        comp = OxideMolComp(MgO=1, SiO2=1)
        assert np.any(comp.all_values==0)

    def test_should_get_all_values_from_elem_comp(self):
        comp = ElemMolComp(**{'Mg': 1, 'Si': 1, 'O': 3})
        assert np.any(comp.all_values == 0)

    def test_should_get_all_components_from_oxide_comp(self):
        comp = OxideMolComp(MgO=1, SiO2=1)
        assert len(comp.all_components) > len(comp.components)

    def test_should_get_all_components_from_elem_comp(self):
        comp = ElemMolComp(**{'Mg': 1, 'Si': 1, 'O': 3})
        assert len(comp.all_components) > len(comp.components)

    def test_should_get_nonzero_components_from_oxide_comp(self):
        comp = OxideMolComp(MgO=1, SiO2=1)
        all_data = pd.Series(comp.all_data)

        assert np.all(all_data[comp.components]>0)
        assert np.all(all_data[comp.zero_components]==0)

        assert UnorderedList(comp.all_components) == (
                list(comp.components) + list(comp.zero_components) )

    def test_should_get_nonzero_components_from_elem_comp(self):
        comp = ElemMolComp(**{'Mg': 1, 'Si': 1, 'O': 3})
        all_data = pd.Series(comp.all_data)

        assert np.all(all_data[comp.components]>0)
        assert np.all(all_data[comp.zero_components]==0)

        assert UnorderedList(comp.all_components) == (
                list(comp.components) + list(comp.zero_components) )

    def test_should_define_composition_by_oxide_molar_abundance(self):
        comp = OxideMolComp(MgO=1, SiO2=1)
        assert comp == {'MgO':1, 'SiO2':1}

    def test_should_compare_normalized_oxide_compositions(self):
        comp = OxideMolComp(MgO=1, SiO2=1)
        assert comp == {'MgO':0.5, 'SiO2':0.5}
        assert comp == {'MgO':3, 'SiO2':3}
        assert not comp == {'MgO':2, 'SiO2':0.5}

    def test_should_compare_normalized_elemental_compositions(self):
        comp = ElemMolComp(**{'Mg': 2, 'Si': 1, 'O': 4})
        assert comp == {'Mg': 2, 'Si': 1, 'O': 4}
        assert comp == {'Mg': 2/7, 'Si': 1/7, 'O': 4/7}

    def test_should_calculate_elemental_comp_from_oxides(self):
        assert OxideMolComp(Al2O3=1).elem_comp == {'Al': 2, 'O': 3}
        assert OxideMolComp(MgO=1, SiO2=1).elem_comp == {'Mg': 1, 'Si': 1, 'O': 3}

    def test_should_set_simple_oxide_comp_by_wt_or_mols(self):
        assert OxideWtComp(SiO2=100) == OxideMolComp(SiO2=1)
        assert OxideMolComp(MgO=1, SiO2=1) == OxideWtComp(
            MgO=40.3044, SiO2=60.0848)

    def test_should_compare_natural_comps_by_wt_or_mols(self):
        BSE = OxideWtComp(SiO2=44.95, TiO2=0.158, Al2O3=3.52,
                          Cr2O3=0.385, MnO=0.131, FeO=7.97, NiO=0.252,
                          MgO=39.50, CaO=2.79, Na2O=0.298, K2O=0.023,
                          P2O5=0.015)

        assert BSE == OxideMolComp(
            SiO2=38.8, TiO2=0.10256129117905899, Al2O3=1.7904987989927128,
            Cr2O3=0.13137471668468576, FeO=5.753338927767198, MnO=0.09577731951497395,
            MgO=50.82896713297678, NiO=0.17494113572627076, CaO=2.5802839102636868,
            Na2O=0.2493668785846322, K2O=0.012663821802104725, P2O5=0.0054807409820552275)

        assert BSE == OxideMolComp(
            SiO2=38.8, TiO2=0.1026, Al2O3=1.7905,
            Cr2O3=0.1314, FeO=5.7533, MnO=0.09578,
            MgO=50.829, NiO=0.1749, CaO=2.5803,
            Na2O=0.2494, K2O=0.01266, P2O5=0.0055)

        assert OxideMolComp(
            SiO2=38.8, TiO2=0.1026, Al2O3=1.7905,
            Cr2O3=0.1314, FeO=5.7533, MnO=0.09578,
            MgO=50.829, NiO=0.1749, CaO=2.5803,
            Na2O=0.2494, K2O=0.01266, P2O5=0.0055) == BSE
        # assert BSE == OxideMolComp(SiO2=38.80, Al2O3=1.79, FeO=5.75, MgO=50.83, CaO=2.58, Na2O=0.25)






