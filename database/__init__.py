from .models import *
from .base_model import db, Model
from functions.default_func import all_subclasses


all_models = [
    sub for sub in all_subclasses(Model)
    if not sub.__name__.startswith('_')
]

db.create_tables(all_models)
__all__ = all_models
