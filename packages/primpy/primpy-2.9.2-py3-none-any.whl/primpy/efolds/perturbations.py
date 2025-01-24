#!/usr/bin/env python
""":mod:`primpy.efolds.perturbations`: curvature perturbations with respect to e-folds `_N`."""
import numpy as np
from primpy.perturbations import Perturbation, ScalarMode, TensorMode


class PerturbationN(Perturbation):
    """Curvature perturbation for wavenumber `k` with respect to e-folds `_N=ln(a)`.

    Solves the Mukhanov--Sasaki equations w.r.t. number of e-folds `_N` of the
    scale factor `a` for curved universes.

    Input Parameters
    ----------------
        background : Bunch object
            Background solution as returned by
            :func:`primpy.efolds.inflation.InflationEquationsN.sol`.
            Monkey-patched version of the Bunch type usually returned by
            :func:`scipy.integrate.solve_ivp`.
        k : float
            wavenumber

    """

    def __init__(self, background, k, **kwargs):
        super(PerturbationN, self).__init__(background=background, k=k)
        self.scalar = ScalarModeN(background=background, k=k, **kwargs)
        self.tensor = TensorModeN(background=background, k=k, **kwargs)


class ScalarModeN(ScalarMode):
    """Template for scalar modes."""

    def __init__(self, background, k, **kwargs):
        super(ScalarModeN, self).__init__(background=background, k=k, **kwargs)
        self._set_independent_variable('_N')

    def __call__(self, x, y):
        """Vector of derivatives."""
        raise NotImplementedError("Equations class must define __call__.")

    def mukhanov_sasaki_frequency_damping(self):
        """Frequency and damping term of the Mukhanov-Sasaki equations for scalar modes.

        Frequency and damping term of the Mukhanov-Sasaki equations for the
        comoving curvature perturbations `R` w.r.t. e-folds `_N`, where the e.o.m. is
        written as `ddR + 2 * damping * dR + frequency**2 R = 0`.

        """
        K = self.background.K
        a2 = np.exp(2 * self.background._N[self.idx_beg:self.idx_end+1])
        H = self.background.H[self.idx_beg:self.idx_end+1]
        dphidN = self.background.dphidN[self.idx_beg:self.idx_end+1]
        H2 = H**2
        dV = self.background.potential.dV(self.background.phi[self.idx_beg:self.idx_end+1])
        Omega_K = self.background.Omega_K[self.idx_beg:self.idx_end+1]

        kappa2 = self.k**2 + self.k * K * (K + 1) - 3 * K
        epsilon = dphidN**2 / 2
        xi = Omega_K + epsilon - 3

        damping2 = 2 * kappa2 / (kappa2 + K * epsilon) * (xi - dV / (H2 * dphidN)) - xi
        frequency2 = kappa2 / (a2 * H2) + (damping2 + xi + 1) * Omega_K
        if np.all(frequency2 > 0):
            return np.sqrt(frequency2), damping2 / 2
        else:
            return np.sqrt(frequency2 + 0j), damping2 / 2

    def get_vacuum_ic_RST(self):
        """Get initial conditions for scalar modes for RST vacuum w.r.t. e-folds `_N`."""
        a_i = np.exp(self.background._N[self.idx_beg])
        H_i = self.background.H[self.idx_beg]
        z_i = a_i * self.background.dphidN[self.idx_beg]
        Rk_i = 1 / np.sqrt(2 * self.k) / z_i
        dRk_i = -1j * self.k / (a_i * H_i) * Rk_i
        return Rk_i, dRk_i


class TensorModeN(TensorMode):
    """Template for tensor modes."""

    def __init__(self, background, k, **kwargs):
        super(TensorModeN, self).__init__(background=background, k=k, **kwargs)
        self._set_independent_variable('_N')

    def __call__(self, x, y):
        """Vector of derivatives."""
        raise NotImplementedError("Equations class must define __call__.")

    def mukhanov_sasaki_frequency_damping(self):
        """Frequency and damping term of the Mukhanov-Sasaki equations for tensor modes.

        Frequency and damping term of the Mukhanov-Sasaki equations for the
        tensor perturbations `h` w.r.t. e-folds `_N`, where the e.o.m. is
        written as `ddh + 2 * damping * dh + frequency**2 h = 0`.

        """
        K = self.background.K
        N = self.background._N[self.idx_beg:self.idx_end+1]
        H2 = self.background.H[self.idx_beg:self.idx_end+1]**2
        dphidN = self.background.dphidN[self.idx_beg:self.idx_end+1]
        frequency2 = (self.k**2 + self.k * K * (K + 1) + 2 * K) * np.exp(-2 * N) / H2
        damping2 = 3 - dphidN**2 / 2 + K * np.exp(-2 * N) / H2
        if np.all(frequency2 > 0):
            return np.sqrt(frequency2), damping2 / 2
        else:
            return np.sqrt(frequency2 + 0j), damping2 / 2

    def get_vacuum_ic_RST(self):
        """Get initial conditions for tensor modes for RST vacuum w.r.t. e-folds `_N`."""
        a_i = np.exp(self.background._N[self.idx_beg])
        H_i = self.background.H[self.idx_beg]
        hk_i = 2 / np.sqrt(2 * self.k) / a_i
        dhk_i = -1j * self.k / (a_i * H_i) * hk_i
        return hk_i, dhk_i
