# cython: language_level=3

import numpy as np
cimport numpy as cnp # cimport gives us access to NumPy's C API

# here we just replicate the function signature from the header
cdef extern from "Forsterite_stixrude_tmp_calc.h":
    const char *Forsterite_stixrude_tmp_identifier();
    const char *Forsterite_stixrude_tmp_name();
    const char *Forsterite_stixrude_tmp_formula();
    const double Forsterite_stixrude_tmp_mw();
    const double *Forsterite_stixrude_tmp_elements();
    double Forsterite_stixrude_tmp_g(double t, double p)
    double Forsterite_stixrude_tmp_dgdt(double t, double p)
    double Forsterite_stixrude_tmp_dgdp(double t, double p)
    double Forsterite_stixrude_tmp_d2gdt2(double t, double p)
    double Forsterite_stixrude_tmp_d2gdtdp(double t, double p)
    double Forsterite_stixrude_tmp_d2gdp2(double t, double p)
    double Forsterite_stixrude_tmp_d3gdt3(double t, double p)
    double Forsterite_stixrude_tmp_d3gdt2dp(double t, double p)
    double Forsterite_stixrude_tmp_d3gdtdp2(double t, double p)
    double Forsterite_stixrude_tmp_d3gdp3(double t, double p)
    double Forsterite_stixrude_tmp_s(double t, double p)
    double Forsterite_stixrude_tmp_v(double t, double p)
    double Forsterite_stixrude_tmp_cv(double t, double p)
    double Forsterite_stixrude_tmp_cp(double t, double p)
    double Forsterite_stixrude_tmp_dcpdt(double t, double p)
    double Forsterite_stixrude_tmp_alpha(double t, double p)
    double Forsterite_stixrude_tmp_beta(double t, double p)
    double Forsterite_stixrude_tmp_K(double t, double p)
    double Forsterite_stixrude_tmp_Kp(double t, double p)

# here is the "wrapper" signature
def cy_Forsterite_stixrude_tmp_identifier():
    result = <bytes> Forsterite_stixrude_tmp_identifier()
    return result.decode('UTF-8')
def cy_Forsterite_stixrude_tmp_name():
    result = <bytes> Forsterite_stixrude_tmp_name()
    return result.decode('UTF-8')
def cy_Forsterite_stixrude_tmp_formula():
    result = <bytes> Forsterite_stixrude_tmp_formula()
    return result.decode('UTF-8')
def cy_Forsterite_stixrude_tmp_mw():
    result = Forsterite_stixrude_tmp_mw()
    return result
def cy_Forsterite_stixrude_tmp_elements():
    cdef const double *e = Forsterite_stixrude_tmp_elements()
    np_array = np.zeros(106)
    for i in range(0,106):
        np_array[i] = e[i]
    return np_array
def cy_Forsterite_stixrude_tmp_g(double t, double p):
    result = Forsterite_stixrude_tmp_g(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_dgdt(double t, double p):
    result = Forsterite_stixrude_tmp_dgdt(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_dgdp(double t, double p):
    result = Forsterite_stixrude_tmp_dgdp(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_d2gdt2(double t, double p):
    result = Forsterite_stixrude_tmp_d2gdt2(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_d2gdtdp(double t, double p):
    result = Forsterite_stixrude_tmp_d2gdtdp(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_d2gdp2(double t, double p):
    result = Forsterite_stixrude_tmp_d2gdp2(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_d3gdt3(double t, double p):
    result = Forsterite_stixrude_tmp_d3gdt3(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_d3gdt2dp(double t, double p):
    result = Forsterite_stixrude_tmp_d3gdt2dp(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_d3gdtdp2(double t, double p):
    result = Forsterite_stixrude_tmp_d3gdtdp2(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_d3gdp3(double t, double p):
    result = Forsterite_stixrude_tmp_d3gdp3(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_s(double t, double p):
    result = Forsterite_stixrude_tmp_s(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_v(double t, double p):
    result = Forsterite_stixrude_tmp_v(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_cv(double t, double p):
    result = Forsterite_stixrude_tmp_cv(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_cp(double t, double p):
    result = Forsterite_stixrude_tmp_cp(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_dcpdt(double t, double p):
    result = Forsterite_stixrude_tmp_dcpdt(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_alpha(double t, double p):
    result = Forsterite_stixrude_tmp_alpha(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_beta(double t, double p):
    result = Forsterite_stixrude_tmp_beta(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_K(double t, double p):
    result = Forsterite_stixrude_tmp_K(<double> t, <double> p)
    return result
def cy_Forsterite_stixrude_tmp_Kp(double t, double p):
    result = Forsterite_stixrude_tmp_Kp(<double> t, <double> p)
    return result
