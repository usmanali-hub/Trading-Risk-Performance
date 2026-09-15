# Data

No raw trade history from a real account is stored in this repository.

Run:

```bash
python src/generate_data.py
python src/clean_data.py
```

This creates the synthetic source and cleaned datasets locally. The CSV files are excluded from Git to keep the repository lightweight and reproducible.

The generator uses a fixed random seed, so the same pipeline can recreate the dataset consistently.
