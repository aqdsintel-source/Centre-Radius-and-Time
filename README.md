# Centre, Radius and Time

**A Comparative Mathematical Process Across Circular Geometry,
Navier-Stokes Dynamics and OpenAI's Published Blow-Up Construction**

Author: **David Penny**  
AI analytical collaborator: **Helios, under AQDS governance**  
Contact: **AQDS - aqds.intel@gmail.com**  
Release: **v1.0-public-review**

## Status

This is an interdisciplinary public-review research note. It is not peer
reviewed and does not claim:

- a new proof of a Navier-Stokes theorem;
- independent verification of the complete source proof or Lean artifact;
- resolution of the unforced Clay Millennium problem;
- proof that physical time is circular, radial, centre-outward or
  multidimensional; or
- verified novelty or scientific consensus.

The paper preserves four distinct evidence classes:

1. source mathematics;
2. independently derived and symbolically checked mathematics;
3. comparative interpretation; and
4. David Penny's physical-time hypothesis.

## Main Result Of The Comparison

On the central plane of the selected similarity construction, the source
variables give `q = tau` and `X = r^2/(2q)`. Circle geometry therefore yields
the exact identity

```text
A = pi r^2 = 2 pi X tau.
```

The paper traces this relation through rotational period, velocity,
acceleration, pressure-gradient and angular-momentum scaling while retaining
the boundary between mathematical parameterisation and physical interpretation.

## Governance Contribution

The final section defines a closed control process at the point where AI output
is first treated as possible knowledge:

```text
human question and permission
  -> AI-assisted search, generation or comparison
  -> evidence capture
  -> reproducible verification
  -> claim classification
  -> human correction and approval
  -> qualified release or withholding
```

Failed, conflicting and unknown results return to evidence and correction.
Confidence, repetition, institutional prestige, computational scale, agent
agreement and media reach cannot promote a claim to fact.

## Repository Contents

- `paper/` - canonical public-review PDF and Markdown source.
- `figures/` - the three generated explanatory figures.
- `evidence/` - source, claim, prior-art, derivation and release ledgers.
- `scripts/` - self-contained symbolic verification and figure generation.

Third-party source PDFs are deliberately excluded. The paper and source ledger
link to their authoritative public locations.

## Reproduce The Registered Algebra

Using Python 3.12 with the dependencies in `requirements.txt`:

```powershell
python scripts\verify_derivations.py
```

The registered local result is 10/10 selected symbolic identities reducing to
zero under the stated assumptions. This verifies those identities only; it is
not verification of the complete source proof or the physical-time hypothesis.

## Publication Record

- GitHub: https://github.com/aqdsintel-source/Centre-Radius-and-Time
- Zenodo: https://doi.org/10.5281/zenodo.22746711

## Licensing

The paper, figures and AQDS-authored evidence are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The original
reproducibility scripts in `scripts/` are licensed under the MIT License.
See `LICENSE` and `LICENSE-CODE` for the exact scope and terms.

## AI-Use Disclosure

Helios operated through OpenAI Codex using the locally configured
`gpt-5.6-sol` model and ultra reasoning effort during the recorded drafting and
release-preparation sessions. Its role included source comparison,
mathematical derivation assistance, reproducibility tooling, symbolic checks,
figures, document preparation and release packaging. David Penny supplied the
originating concept and research direction, corrected and governed the work,
and remains the accountable human author and publication authority.

The paper contains the complete attribution, claim boundary and governance
statement.
