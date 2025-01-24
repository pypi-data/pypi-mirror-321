# (C) Quantum Computing Inc., 2024.
import os
import logging
from typing import (Dict, List, Tuple, Union)
from warnings import warn
import numpy as np
from eqc_models.base.operators import Polynomial, QUBO, OperatorNotAvailableError

log = logging.getLogger(name=__name__)

# base class 
class EqcModel:
    """ 

    EqcModel subclasses must provide these properties/methods. 
    
    :decode: takes a raw solution and translates it into the original problem
      formulation 
    :H: property which returns a Hamiltonian operator 
    :upper_bound: Let D be an array of length n which contains the largest possible value 
      allowed for x[i], which is the variable at index i, 0<=i<n. This means that a x[i]
      is in the domain [0,D[i]]. If the solution type of x[i] is integer, then x[i] is
      in the set of integers, Z, and also 0<=x[i]<=floor(D[i]).
    :qudit_limits: maximum value permitted for each qudit 

    >>> model = EqcModel()
    >>> ub = np.array([1, 1.5, 2])
    >>> model.upper_bound = ub # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: ...
    >>> model.upper_bound = np.ones((3,))
    >>> (model.upper_bound==np.ones((3,))).all()
    True
    >>> model.upper_bound = 2*np.ones((3,))
    >>> (model.upper_bound==2).all()
    True

    """

    _upper_bound = None
    _H = None
    _machine_slacks = 0
    
    def decode(self, solution : np.ndarray) -> np.ndarray:
        """ Manipulate the solution to match the variable count """
        
        # ignore any slacks that may have been added during encoding
        solution = solution[:-self.machine_slacks]
        
        return solution

    @property
    def upper_bound(self) -> np.array:
        """ 
        An array of upper bound values for every variable in the model. Must be integer.

        """

        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, value : np.array):
        value = np.array(value)
        if (value != value.astype(np.int64)).any():
            raise ValueError("Upper bound values must be integer")
        self._upper_bound = value.astype(np.int64)

    @property
    def domains(self) -> np.array:
        if self._upper_bound is None:
            raise ValueError("Variable domains are required for model definition")
        return self._upper_bound

    @domains.setter
    def domains(self, value):
        warn("The domains property is deprecated in favor of naming it upper_bound", DeprecationWarning)
        self._upper_bound = value

    @property
    def n(self) -> int:
        """ Return the number of variables """
        return int(max(self.upper_bound.shape))
    
    @property
    def H(self):
        """ Hamiltonian operator of unknown type """
        return self._H

    @H.setter
    def H(self, value):
        """ The H setter ensures that the Hamiltonian is properly formatted. """

        raise NotImplementedError("H property setter not implemented in subclass, can't be set directly")

    @property
    def sparse(self) -> Tuple[np.ndarray, np.ndarray]:
        # Implement this for the particular subclasses
        raise NotImplementedError("sparse must be implemented in a subclass")
        
    @property
    def machine_slacks(self):
        """ Number of slack qudits to add to the model """
        return self._machine_slacks

    @machine_slacks.setter
    def machine_slacks(self, value:int):
        assert int(value) == value, "value not integer"
        self._machine_slacks = value

    def evaluateObjective(self, solution : np.ndarray) -> float:
        raise NotImplementedError("evaluateObjective must be implemented in a subclass")
    
    def createConfigElements(self) -> Dict:
        obj = {"number_of_nonzero": None}
        return obj
    def createBenchmarkConfig(self, fname : str) -> None:
        obj = self.createConfigElements()
    
    @property
    def dynamic_range(self) -> float:
        raise NotImplementedError("EqcModel does not implement dynamic_range")
        
    @property
    def polynomial(self) -> Polynomial:
        raise OperatorNotAvailableError("Polynomial operator not available")
    
    @property
    def qubo(self) -> QUBO:
        raise OperatorNotAvailableError("QUBO operator not available")
    
class SumConstraintMixin:

    _sum_constraint = None

    @property
    def sum_constraint(self):
        return self._sum_constraint
    
    @sum_constraint.setter
    def sum_constraint(self, value : Union[float, int]):
        assert value >= 0, "sum_constraint must be greater than or equal to one"
        self._sum_constraint = value

class ModelSolver:
    """ Provide a common interface for solver implementations. 
    Store a model, implement a solve method."""

    def solve(self, model:EqcModel, *args, **kwargs) -> Dict:
        raise NotImplementedError()
