# Statement

## Problem Statement

In India, income tax is not charged at a single flat rate — income is
divided into slabs, and each slab is taxed at a different rate. Taxpayers
can also choose between two different tax regimes (New Regime and Old
Regime), which use different slab structures. This makes it difficult for
a person to quickly and correctly work out how much tax they owe, or to
know which regime results in lower tax for their income level.

This project solves that problem by building a simple command-line Python
program that calculates income tax for FY 2024-25 under both regimes,
adds the applicable cess, and clearly shows the user which regime is
cheaper and by how much.

## Scope of the Project

- Calculates income tax slab-wise for the **New Regime** and **Old Regime**
  (FY 2024-25 rates).
- Applies the **4% Health & Education Cess** on the calculated tax.
- Compares both regimes and displays the amount saved by choosing the
  cheaper one.
- Validates user input (rejects negative numbers and non-numeric text).
- Saves every calculation to a history file and allows the user to view
  past calculations.
- Runs entirely from the command line — no GUI or internet connection
  required.

**Out of scope:**
- Deductions and exemptions such as Section 80C, HRA, or standard
  deduction are not calculated.
- Tax slabs for senior citizens (60+ years) are not included.
- The tool is for educational purposes only and is not intended for
  actual tax filing.

## Target Users


- Anyone who wants a quick, rough estimate of their income tax under the
  New vs Old regime without doing manual slab calculations.
- Individual salaried taxpayers in India who want to compare which
  regime might suit them, as a starting point before consulting a tax
  professional.

## High-Level Features

- **Menu-driven interface** — Calculate Tax, View History, Exit.
- **Slab-wise tax calculation** for both New and Old tax regimes.
- **Automatic cess calculation** (4%) added to the computed tax.
- **Regime comparison** — tells the user which regime is cheaper and the
  exact amount saved.
- **Input validation** — handles invalid or negative income entries
  gracefully with re-prompting instead of crashing.
- **Persistent history** — every calculation is saved to `history.txt`
  and can be viewed later from within the program.
- **No external dependencies** — built using only Python's standard
  library, making it easy to set up and run.
