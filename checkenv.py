from colorama import Fore
from pkgutil import iter_modules


def check_import(packagename):
    """
    Checks that a package is present. Returns true if it is available, and
    false if not available.
    """
    if packagename in (name for _, name, _ in iter_modules()):
        return True
    else:
        return False


packages = ['missingno', 'pytest', 'pytest_cov', 'tinydb', 'yaml',
            'pandas_summary', 'environment_kernels']

try:
    for pkg in packages:
        assert check_import(pkg)
    print(Fore.GREEN + 'All packages found; environment checks passed.')
except AssertionError:
    print(Fore.RED + f"{pkg} cannot be found. Please pip or conda install.")
