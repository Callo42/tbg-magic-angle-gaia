# magnetic-bloch-tbg-gaia

Standalone audited Gaia subgraph for LKM root `gcn_afdfbd0c013048d8`.

The package maps one selected evidence chain from Herzog-Arbeitman, Chew, and
Bernevig (2022) on the magnetic Bloch theorem and reentrant flat bands in
magic-angle twisted bilayer graphene at `phi=2*pi` flux.

Run checks from the workspace root:

```bash
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile /home/rsw/ThisIsDP/dev/test_lkm2gaia/tbg-magic-angle-gaia/artifacts/subgraphs/magnetic-bloch-tbg-gaia
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief /home/rsw/ThisIsDP/dev/test_lkm2gaia/tbg-magic-angle-gaia/artifacts/subgraphs/magnetic-bloch-tbg-gaia
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole /home/rsw/ThisIsDP/dev/test_lkm2gaia/tbg-magic-angle-gaia/artifacts/subgraphs/magnetic-bloch-tbg-gaia
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer /home/rsw/ThisIsDP/dev/test_lkm2gaia/tbg-magic-angle-gaia/artifacts/subgraphs/magnetic-bloch-tbg-gaia
```
