# decoraid stands for Decorator Aid :) -->

pip install decoraid
decoraid --example  or decoraid --help

decoraid/
├── decoraid/
│   ├── __init__.py
│   └── cpdec.py
├── dist/
├── tests/
│   └── test_cpdec.py
├── pyproject.toml
├── README.md


# sample usage: -->
wrap the decorator around the function you want to test, provide the name of the package and the path to the virtual environment

    from decoraid.cpdec import check_package
    
    venv_path = "C:/projects/git/xxxx/.venv/" 
    
    
    @check_package("pandas", venv_path)
    
    def test_pandas():
    
        print('test_cpdec')
    
    if __name__ == "__main__":
    
        test_pandas()
