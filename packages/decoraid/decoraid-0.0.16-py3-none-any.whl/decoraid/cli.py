import argparse
# import os

# # Hardcoded version information
VERSION = "0.0.15"

# # Hardcoded dependencies information
# DEPENDENCIES = {
#     "python": "^3.11",
#     "PyYAML": "^6.0.2",
#     "SQLAlchemy": "^2.0.36",
#     "psycopg2": "^2.9.10",
#     "pandas": "^2.2.3",
#     "pyodbc": "^5.2.0",
#     "pylint": "^3.3.1"
# }

# Hardcoded usage information
EXAMPLE = """

sample usage:

from decoraid.cpdec import check_package
venv_path = "C:/projects/git/xxxx/.venv/" 

# wrap the decorator around the function you want to test, provide the name of the package and the path to the virtual environment
@check_package("pandas", venv_path)
def test_pandas():
    print('test_cpdec')

if __name__ == "__main__":
    test_pandas()

"""

def main():
    parser = argparse.ArgumentParser(description='Decoraid ~ collection of usefull decorator utilities')
    parser.add_argument('--version', action='version', version=f'ConnectionVault {VERSION}')
    parser.add_argument('--example', action='store_true', help='Show sample code syntax')

    
    args = parser.parse_args()

    if args.example:
        print(EXAMPLE)

    # if args.connections:
    #     conn_manage_main()

    # if args.yamldir:
    #     conn_home = os.getenv('conn_home')
    #     if conn_home:
    #         print(f"conn_home: {conn_home}")
    #     else:
    #         print("please set conn_home variable")

if __name__ == '__main__':
    main()