#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    23.01.2017 14:41:35 CET
# File:    test_matrix_representation.py

import pytest
import sympy as sp

from kdotp_symmetry.matrix_representation import matrix_representation

from kdotp_symmetry.constants import K_VEC
from kdotp_symmetry.expr_utils import expr_to_vector, monomial_basis, matrix_to_expr_operator

from kdotp_symmetry.hermitian_utils import hermitian_to_vector, hermitian_basis

@pytest.mark.parametrize('operator,basis,to_vector_fct,result', [
    (
        matrix_to_expr_operator([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
        monomial_basis(2),
        expr_to_vector,
        sp.Matrix([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        ])
    ),
    (
        matrix_to_expr_operator([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
        monomial_basis(1),
        expr_to_vector,
        sp.Matrix([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, -1]
        ])
    #~ ),
    #~ (
    
    )
])
def test_matrix_representation(operator, basis, to_vector_fct, result):
    kx, ky, kz = K_VEC
    assert matrix_representation(operator, basis, to_vector_fct) == result
