# regpnlpypi

regpnlpypi is a Python package designed to simplify the process of creating, running, and evaluating backtests. It offers an intuitive interface for exploring strategies and automating complex workflows.

---

## Installation

To install the package, use the following command:

```bash
pip install regpnlpypi
```
---

## Usage

Every new functionality developed in this package has been interfaced so you have very little to do!

### Step-by-Step Guide

1. **Create a `launch.py` file**

   Add the following lines to your `launch.py` file that is already created in the folder:

   ```python
   from regpnlpypi.main import run

   if __name__ == "__main__":
        run()

   ```

2. **Run the application**

   Open the terminal in the folder where the `launch.py` file is located and run the following command:

   ```bash
   streamlit run launch.py
   ```
---

## Commands Cheat Sheet

Here's a quick reference for all coding-related commands used:


### Running the Application

1. Create the `launch.py` file:
   
   ```python
   from regpnlpypi.main import run

   if __name__ == "__main__":
        run()

   ```

2. Run the application via Streamlit:
   
   ```bash
   streamlit run launch.py
   ```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
