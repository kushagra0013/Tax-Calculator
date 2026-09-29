# Income Tax Calculator

A simple command-line Python program that calculates income tax in India
(FY 2024-25) under the New and Old tax regimes and tells you which one is
cheaper. Every calculation is saved to a history file.

## Features

- Slab-wise tax calculation for New and Old regime
- 4% Health & Education Cess included
- Compares both regimes and shows the savings
- Input validation (handles negative numbers and invalid text)
- Saves and displays calculation history

## Project Files

```
tax-calculator/
├── tax_calculator.py       # Main program
├── README.md                 # This file
├── PROBLEM_STATEMENT.md      # Project problem statement
└── report.md                 # Project report
```

(`history.txt` is created automatically the first time you run a calculation.)

---

## Step 1: Environment Setup

This project needs Python 3.6 or later. No other software is required.

1. **Check if Python is already installed:**

   ```bash
   python --version
   ```

   or, on some systems:

   ```bash
   python3 --version
   ```

   If you see something like `Python 3.10.6`, you're good to go and can
   skip to Step 2.

2. **If Python is not installed**, download and install it:
   - **Windows / macOS**: download the installer from
     [python.org/downloads](https://www.python.org/downloads/) and run it.
     On Windows, make sure to check **"Add Python to PATH"** during
     installation.
   - **Linux (Debian/Ubuntu)**:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

3. **Verify the installation again:**

   ```bash
   python --version
   ```

## Step 2: Get the Project

Clone the repository (or download and extract the ZIP, then `cd` into the
folder):

```bash
git clone https://github.com/<kushagra0013>/<Tax Calculator>.git
cd <repo-name>
```

## Step 3: Install Dependencies

This project uses **only Python's built-in standard library** — no external
packages need to be installed. There is nothing to run with `pip`.

If you still want to set up an isolated environment (optional, but good
practice):

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

You can confirm no extra packages are needed by checking that the program
only imports built-in modules — open `tax_calculator.py` and note the
`import` lines at the top (they only reference standard Python modules).

## Step 4: Configuration

No configuration or environment variables are required to run this project.

The only thing that can optionally be changed is the history file location,
set at the top of `tax_calculator.py`:

```python
HISTORY_FILE = "history.txt"
```

By default, `history.txt` is created in the same folder as the script the
first time you run a calculation. Change this value if you want the history
saved elsewhere or under a different name — no other setup is needed.

## Step 5: Run the Program

From inside the project folder, run:

```bash
python tax_calculator.py
```

(Use `python3 tax_calculator.py` if `python` points to Python 2 on your
system.)

You'll see a menu:

```
========================================
   INCOME TAX CALCULATOR (FY 2024-25)
========================================

1. Calculate tax
2. View history
3. Exit
Enter your choice (1-3):
```

- Enter `1` to calculate tax — you'll be asked for your annual income, and
  the program will show tax under both regimes.
- Enter `2` to view all past calculations saved in `history.txt`.
- Enter `3` to exit the program.

### Sample Run

```
Enter your choice (1-3): 1
Enter annual income (Rs.): 850000

--- Result (includes 4% cess) ---
Income         : Rs. 850,000.00
New Regime Tax : Rs. 41,600.00
Old Regime Tax : Rs. 85,800.00
New Regime saves you Rs. 44,200.00
```

## Step 6: Verify It's Working

- Run the program and choose option `1`, enter an income (e.g. `500000`),
  and confirm you see a tax result printed.
- Choose option `2` and confirm your previous calculation is listed.
- Try entering an invalid value (e.g. a negative number or text) at the
  income prompt and confirm the program shows an error and asks again
  instead of crashing.

## Note

This project is for learning purposes only and does not include deductions
such as 80C or HRA. It should not be used for actual tax filing.

## Author

<Your Name Kushagra Yadav>, <Registration Number 26MIM10162  >
