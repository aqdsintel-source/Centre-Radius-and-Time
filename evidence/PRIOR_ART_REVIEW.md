# Bounded Prior-Art Review

Date: 2026-09-13
Status: first-pass bounded review; not exhaustive

## Review Question

Which parts of the proposed comparison are established mathematics, which parts are direct consequences of the 2026 OpenAI construction, and which part remains David's interpretive centre-outward time hypothesis?

## Findings

### 1. Radius-Squared Time Scaling Is Established

Parabolic equations naturally pair spatial scale `r` with time scale `r^2`. The official Clay problem statement uses parabolic cylinders

```math
Q_r=B_r\times I_r,
\qquad |I_r|=r^2.
```

The relation between a shrinking radial scale and remaining time is therefore established PDE structure, not a new discovery by this note.

### 2. Self-Similar Navier-Stokes Scaling Is Established

Leray-type self-similar analysis predates the OpenAI paper. A standard representative form is

```math
u(x,t)=\frac{U(y)}{\sqrt{2\sigma(t_*-t)}},
\qquad
y=\frac{x}{\sqrt{2\sigma(t_*-t)}}.
```

The OpenAI construction uses a more specialised anisotropic and forced construction, but the general use of `sqrt(t_*-t)` as a shrinking spatial scale has clear prior art.

### 3. Axisymmetric Swirl And Angular Momentum Are Established

The cylindrical decomposition

```math
u=u_r e_r+u_\theta e_\theta+u_z e_z
```

and the swirl/angular-momentum quantity

```math
\Theta=r u_\theta
```

are standard in axisymmetric Navier-Stokes analysis.

### 4. Circle Kinematics Are Established

The following are standard consequences of Euclidean circle geometry and rotational kinematics:

```math
C=2\pi r,
\quad A=\pi r^2,
\quad u_\theta=r\Omega,
\quad P_\theta=\frac{2\pi}{\Omega}=\frac{2\pi r}{u_\theta},
\quad a_c=\frac{u_\theta^2}{r}.
```

### 5. Structural And Multidimensional Time Proposals Have Prior Art

Atkin (1978) proposed time as dependent on multidimensional system structure and discussed hierarchical temporalities. Bars (1998) developed a technically different two-time gauge framework. Other fields also use radial coordinates as scale variables.

These sources mean that neither "multidimensional time" nor "radial variable as scale" can be claimed as a new category.

### 6. The Specific Comparative Synthesis Remains Unclassified

This first-pass review did not identify a source that performs the exact following comparison:

```math
\text{OpenAI 2026 blow-up similarity structure}
\;\longleftrightarrow\;
\text{circle area and rotational period}
\;\longleftrightarrow\;
\text{centre-outward time interpretation}.
```

That absence is not proof of novelty. A comprehensive scholarly search and specialist review have not been completed.

## Prior-Art Conclusion

- The component mathematics is substantially established.
- The algebraic contact map is a transparent derivation from established relations and the published 2026 scaling.
- The centre-outward temporal interpretation is a research hypothesis.
- Novelty: `Not verified yet` and not claimed.
- Physical correctness: `Not verified yet`.

