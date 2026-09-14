# Source Ledger

Access date for online sources: 2026-09-13 (Australia/Sydney)

## Primary Mathematical Sources

### S01 - OpenAI, "Finite Time Blowup for Navier-Stokes"

- Type: primary claimed proof manuscript, 166 pages.
- URL: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
- Local evidence file: `external/openai-finite-time-blowup-navier-stokes-2026.pdf`
- Local SHA256: `0E779481C4DA40BD28D1E642E1D8CA57447D129610DF28DFA5A11E9AF8AE228F`
- Used for: theorem statement, governing equation, cylindrical construction, similarity variables, scaling exponents, radial pressure balance, angular averaging, energy scaling, and proof outline.
- Boundary: this AQDS note does not independently verify the full 166-page proof.

### S02 - OpenAI, "On the Navier-Stokes Millennium Prize Problem"

- Type: primary publication announcement and AI-process description.
- URL: https://openai.com/index/navier-stokes-solution/
- Used for: publication date, coordinated-agent process, problem variants, Euler precursor, cross-group consolidation, message/token counts, and Lean-formalisation timeline.

### S03 - OpenAI, `NavierStokesAndEuler`

- Type: primary public Lean repository accompanying the claimed result.
- URL: https://github.com/openai/NavierStokesAndEuler
- Used for: existence and stated scope of the formalisation and its build instructions.
- Boundary: the repository was identified; an independent local Lean build has not been completed for this note.

### S04 - Charles L. Fefferman / Clay Mathematics Institute, "Existence and Smoothness of the Navier-Stokes Equation"

- Type: official Millennium Prize problem statement.
- URL: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
- Local evidence file: `external/clay-navier-stokes-official-problem.pdf`
- Local SHA256: `C1B5F27B1A64705CFAF1AFCEEA513DB5DEEDCA8A18CA56AB32E7F86445A06D0C`
- Used for: standard equation, physical quantities, alternatives A-D, and the established parabolic spacetime scaling in which a spatial radius `r` is paired with a time interval of length `r^2`.

## Bounded Prior-Art Sources

### S05 - Xinyu He, "Existence of Leray's Self-Similar Solutions of the Navier-Stokes Equations"

- Type: peer-reviewed mathematical article.
- DOI: https://doi.org/10.4153/CMB-2004-005-3
- Landing page: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/existence-of-lerays-selfsimilar-solutions-of-the-navierstokes-equations-in-mathcaldsubset-mathbbr3/B15DC0383FB369091C388E2BB706E8D7
- Used for: prior use of the similarity coordinate `y=x/sqrt(2 sigma (t*-t))` and velocity scaling proportional to `(t*-t)^(-1/2)`.

### S06 - W. S. Ożański and S. Palasek, "Quantitative Control of Solutions to the Axisymmetric Navier-Stokes Equations in Terms of the Weak L3 Norm"

- Type: peer-reviewed mathematical article, Annals of PDE 9, article 15, published 10 August 2023.
- DOI: https://doi.org/10.1007/s40818-023-00156-7
- Used for: established axisymmetric cylindrical decomposition and the swirl quantity `Theta = r u_theta`.

### S07 - R. H. Atkin, "Time as a Pattern on a Multi-Dimensional Structure"

- Type: conceptual/mathematical prior art, Journal of Social and Biological Structures 1(3), 1978, 281-295.
- DOI: https://doi.org/10.1016/0140-1750(78)90027-1
- Used for: prior existence of a proposal relating time to multidimensional system structure and hierarchical temporalities.
- Boundary: Atkin's simplicial-complex approach is not the same construction as David's centre-outward proposition.

### S08 - Itzhak Bars, "Two-Time Physics"

- Type: theoretical-physics prior art.
- URL: https://arxiv.org/abs/hep-th/9809034
- Used for: prior existence of physical models with more than one time dimension.
- Boundary: two-time gauge physics is not evidence for, or an equivalent of, the centre-radius contact map derived in this note.

## Publication-Process Sources

### S09 - Zenodo generative-AI policy for depositors

- URL: https://support.zenodo.org/help/en-gb/13-policies/227-what-is-your-usage-policy-for-generative-ai-for-depositors
- Used for: AI disclosure and attribution boundary. Zenodo does not permit an AI tool to be entered as an author, creator, or contributor in deposit metadata.

### S10 - Zenodo DOI guidance

- URL: https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/
- Used for: DOI reservation and publication process.

### S11 - GitHub citation-file guidance

- URL: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
- Used for: future `CITATION.cff` configuration after David confirms his preferred publication name and the final repository identity.

## Source-Control Rules

- Third-party PDFs in `external/` are evidence copies and are not automatically licensed for redistribution in a future public AQDS repository.
- Public release packaging must link to authoritative third-party sources unless redistribution rights are separately verified.
- URLs, local hashes, access dates, and claim mappings must be rechecked immediately before publication.
