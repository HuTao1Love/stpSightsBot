import glob
from os.path import dirname
from loader import dp

modules = glob.glob("*.py", root_dir=dirname(__file__))
modules = [module.replace('.py', '')
           for module in modules
           if '__' not in module]

__all__ = ['dp'] + modules
