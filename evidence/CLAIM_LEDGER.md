# Claim And Evidence Ledger

| ID | Claim | Class | Evidence | Status |
|---|---|---|---|---|
| S-01 | The governing equation is `partial_t u + (u dot grad)u - nu Delta u + grad p = f`, with `div u=0`. | Source mathematics | OpenAI paper (1.1); Clay statement (1)-(2) | Verified against local PDFs |
| S-02 | The OpenAI theorem constructs smooth forced data from rest with bounded kinetic energy and unbounded velocity as `t` approaches 1. | Source claim | OpenAI paper, Theorem 1.1 | Accurately transcribed; full proof not independently verified |
| S-03 | The construction uses scalar time `t` and remaining time `tau=1-t`. | Source mathematics | OpenAI paper Sections 2-3 | Verified against local PDF |
| S-04 | The core uses cylindrical coordinates and a singular centre at the spatial origin. | Source mathematics | OpenAI paper Section 2.1 | Verified against local PDF |
| S-05 | The similarity variable is `X=r^2/(2q)`, with `q` comparable to `tau` in a fixed core chart. | Source mathematics | OpenAI paper (3.2) | Verified against local PDF |
| S-06 | The leading radial pressure balance is `partial_r p^(0)=(u_theta^(0))^2/r`. | Source mathematics | OpenAI paper, page 8 | Verified against local PDF |
| S-07 | The radial and azimuthal scales satisfy `ell_r asymp tau^(1/2)` and `u_theta asymp tau^(-1/2-h)`. | Source mathematics | OpenAI paper Sections 2.1 and 3.1 | Verified against local PDF |
| S-08 | Angular averaging uses a full `2 pi` period. | Source mathematics | OpenAI paper (3.7)-(3.8) | Verified against local PDF |
| D-01 | From `X=r^2/(2q)` and `A=pi r^2`, `A=2 pi q X`. | Derived mathematics | Algebraic substitution | Symbolically verified; see `derivation_verification.json` |
| D-02 | For fixed `X` in the core, `A asymp 2 pi X tau`. | Derived mathematics | D-01 plus `q asymp tau` | Exponent and identity symbolically verified; source comparison checked |
| D-03 | `P_theta=2 pi r/u_theta=2A/(r u_theta)`. | Derived mathematics | Circle kinematics and angular momentum | Symbolically verified; see `derivation_verification.json` |
| D-04 | Under the paper's scales, `P_theta asymp tau^(1+h)`. | Derived mathematics | S-07 plus D-03 | Symbolically verified; see `derivation_verification.json` |
| D-05 | The centripetal acceleration scale is `a_c asymp tau^(-3/2-2h)`. | Derived mathematics | `a_c=u_theta^2/r` plus S-07 | Symbolically verified; see `derivation_verification.json` |
| D-06 | The dominant core-energy scale is `tau^(1/2-3h)` and tends to zero for the paper's `h<1/100`. | Source-confirming derivation | Volume times squared velocity; OpenAI page 16 | Symbolically verified; see `derivation_verification.json` |
| I-01 | One scalar external time coordinate can parameterise multiple nonlinear local process times. | Mathematical interpretation | D-02 through D-05 | Supported as interpretation, not physical ontology |
| H-01 | Physical time itself is centre-outward, radial, layered, or multidimensional. | David's research hypothesis | Requires a defined model and discriminating observations | Not verified yet |
| H-02 | The Navier-Stokes construction provides evidence that physical time has the structure in H-01. | Strong physical inference | No discriminating empirical result supplied | Not verified yet |
| P-01 | The OpenAI proof has received complete independent mathematical acceptance. | External status | No completed independent acceptance established in this package | Not verified yet |
| G-01 | The paper implements a controlled path from human question and permission through AI assistance, evidence capture, verification, claim classification, human correction and approval, and qualified release or withholding. | Governance design | David's 2026-09-14 directive; manuscript Section 9.4 | Implemented as a publication control; external effectiveness not verified |
| G-02 | Individual AI tools and agentic AI systems must not erase contrary evidence, move their permission boundary, self-validate, or strengthen public claims beyond their evidence. | Governance requirement | David's 2026-09-14 directive; manuscript Section 9.4 | Active normative boundary; not an empirical capability claim |

## Gate

No `D`, `I`, or `H` claim may be rewritten as part of the source paper. No `H` claim may be presented as established physics. No `G` requirement may be represented as proof that the governance process is universally effective without external evaluation.
