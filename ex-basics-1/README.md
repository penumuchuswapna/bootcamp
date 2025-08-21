# swapna-hello

A simple Python package that prints a friendly greeting.


1. Initialize project with uv
# Go to your bootcamp repo
cd bootcamp

# Initialize uv project
uv init ex_basics_1
cd ex_basics_1

2. Create & activate virtual environment
# Create venv
uv venv

# Activate venv (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

3. Build the package
uv build

This will create dist/swapna_hello-0.1.0.tar.gz and .whl.

4. Upload to TestPyPI

First install twine:

pip install twine

5. Upload:

python -m twine upload --repository testpypi dist/*

It will ask for TestPyPI credentials (username = __token__, password = your API token from https://test.pypi.org/manage/account/
).


6. Install from TestPyPI
pip install -i https://test.pypi.org/simple/ swapna-hello

7. Run it:
python -m swapna_hello
output :Hello, world!
python -m swapna_hello swapna
output:Hello, swapna!
























