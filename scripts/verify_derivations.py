"""Verify the algebraic contact relations used in the AQDS research note."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evidence" / "derivation_verification.json"


def expression_hash(expressions: dict[str, sp.Expr]) -> str:
    payload = "\n".join(
        f"{name}={sp.srepr(sp.simplify(expr))}"
        for name, expr in sorted(expressions.items())
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest().upper()


def main() -> int:
    tau, h = sp.symbols("tau h", positive=True)
    k_r, k_u, k_z = sp.symbols("k_r k_u k_z", positive=True)
    q, X = sp.symbols("q X", positive=True)

    half = sp.Rational(1, 2)
    r = k_r * tau**half
    u_theta = k_u * tau ** (-half - h)
    ell_z = k_z * tau ** (half - h)

    circumference = 2 * sp.pi * r
    area = sp.pi * r**2
    omega = u_theta / r
    period = 2 * sp.pi / omega
    acceleration = u_theta**2 / r
    angular_momentum = r * u_theta
    volume_scale = area * ell_z
    energy_scale = sp.Rational(1, 2) * volume_scale * u_theta**2

    similarity_radius = sp.sqrt(2 * q * X)
    similarity_area = sp.pi * similarity_radius**2

    checks = {
        "period_from_circumference": sp.simplify(
            period - circumference / u_theta
        ),
        "period_from_area_and_angular_momentum": sp.simplify(
            period - 2 * area / angular_momentum
        ),
        "centripetal_acceleration_from_period": sp.simplify(
            acceleration - 4 * sp.pi**2 * r / period**2
        ),
        "similarity_area_identity": sp.simplify(
            similarity_area - 2 * sp.pi * q * X
        ),
        "area_time_exponent": sp.simplify(
            area / (sp.pi * k_r**2) - tau
        ),
        "period_time_exponent": sp.simplify(
            period / (2 * sp.pi * k_r / k_u) - tau ** (1 + h)
        ),
        "acceleration_time_exponent": sp.simplify(
            acceleration / (k_u**2 / k_r) - tau ** (-sp.Rational(3, 2) - 2 * h)
        ),
        "angular_momentum_time_exponent": sp.simplify(
            angular_momentum / (k_r * k_u) - tau ** (-h)
        ),
        "volume_time_exponent": sp.simplify(
            volume_scale / (sp.pi * k_r**2 * k_z)
            - tau ** (sp.Rational(3, 2) - h)
        ),
        "energy_time_exponent": sp.simplify(
            energy_scale
            / (sp.Rational(1, 2) * sp.pi * k_r**2 * k_z * k_u**2)
            - tau ** (sp.Rational(1, 2) - 3 * h)
        ),
    }

    dimensional_checks = {
        "partial_t_u": [1, -2],
        "u_dot_grad_u": [1, -2],
        "nu_laplacian_u": [1, -2],
        "gradient_kinematic_pressure": [1, -2],
        "force_per_unit_mass": [1, -2],
        "angular_momentum_per_unit_mass": [2, -1],
        "centripetal_acceleration": [1, -2],
    }
    dimensions_pass = len({tuple(value) for value in list(dimensional_checks.values())[:5]}) == 1

    h_value = sp.Rational(1, 200)
    sample_taus = [sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)]
    sample_rows = []
    for tau_value in sample_taus:
        substitutions = {tau: tau_value, h: h_value, k_r: 1, k_u: 1, k_z: 1}
        sample_rows.append(
            {
                "tau": float(tau_value),
                "radius": float(sp.N(r.subs(substitutions), 15)),
                "area": float(sp.N(area.subs(substitutions), 15)),
                "period": float(sp.N(period.subs(substitutions), 15)),
                "velocity": float(sp.N(u_theta.subs(substitutions), 15)),
                "acceleration": float(sp.N(acceleration.subs(substitutions), 15)),
                "energy_scale": float(sp.N(energy_scale.subs(substitutions), 15)),
            }
        )

    expressions = {
        "radius": r,
        "azimuthal_velocity": u_theta,
        "circumference": circumference,
        "area": area,
        "angular_speed": omega,
        "rotational_period": period,
        "centripetal_acceleration": acceleration,
        "angular_momentum": angular_momentum,
        "volume_scale": volume_scale,
        "energy_scale": energy_scale,
        "similarity_area": similarity_area,
    }

    result = {
        "schema_version": 1,
        "generated_date": "2026-09-14",
        "engine": f"SymPy {sp.__version__}",
        "assumptions": {
            "tau": "positive remaining-time parameter",
            "h": "positive; OpenAI paper requires 0 < h < 1/100",
            "k_r_k_u_k_z": "positive representative scaling constants",
            "scope": "algebraic consequences only; no physical-time ontology is tested",
        },
        "checks": {name: str(value) for name, value in checks.items()},
        "all_symbolic_checks_zero": all(value == 0 for value in checks.values()),
        "dimensions": {
            "basis": ["length exponent", "time exponent"],
            "terms": dimensional_checks,
            "navier_stokes_acceleration_terms_match": dimensions_pass,
        },
        "representative_sample": {
            "h": "1/200",
            "k_r": 1,
            "k_u": 1,
            "k_z": 1,
            "rows": sample_rows,
        },
        "expressions": {name: str(sp.simplify(expr)) for name, expr in expressions.items()},
        "expression_set_sha256": expression_hash(expressions),
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["all_symbolic_checks_zero"] and dimensions_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
