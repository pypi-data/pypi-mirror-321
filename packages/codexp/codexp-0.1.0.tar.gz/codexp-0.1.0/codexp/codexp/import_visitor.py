"""
Module containing the ImportVisitor class for analyzing Python import statements.

This module is responsible for:
- Parsing and collecting import statements from Python AST
- Handling both regular imports and from-imports
- Normalizing import names and aliases
"""

import ast
from typing import Set
from collections import namedtuple

// ... rest of import_visitor.py ... 