Setup

Clone the repository:
<!-- 
git clone https://github.com/your-username/ex_basics_3.git -->
cd ex_basics_3


(Optional) Create a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows

Install dependencies:

pip install typer build


# Step 1: Build the package
python -m build

# Step 2: Install it locally
pip install dist/ex_basics_3-0.1.0-py3-none-any.whl




Greet someone:Run the CLI
ex-basics-3  Swapna

✅ Output:
Hello, Swapna!


Show help:

ex-basics-3 --help

# alternates cases when i get errors:
Reinstall your package (since cli.py changed):
pip install --force-reinstall dist/ex_basics_3-0.1.0-py3-none-any.whl
Then run:

ex-basics-3  Swapna

✅ Expected output:
Hello, Swapna!
