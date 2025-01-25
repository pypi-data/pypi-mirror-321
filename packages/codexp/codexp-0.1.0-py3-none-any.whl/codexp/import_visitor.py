"""
AST visitor for analyzing Python import statements.

Collects and normalizes:
- Regular imports (import x)
- Aliased imports (import x as y)
- From imports (from x import y)
- Relative imports (.x)
"""

import ast
from typing import Set, NamedTuple, List

class RawImport(NamedTuple):
    """Represents a raw import statement before normalization.
    
    Attributes:
        source: Original import path (e.g. '.submodule.symbol' or 'package.symbol')
        asname: Name used in importing module (from 'as' clause or original name)
        lineno: Line number where the import occurs
    """
    source: str
    asname: str
    lineno: int

class ImportVisitor(ast.NodeVisitor):
    """AST visitor to collect import statements."""
    
    def __init__(self):
        self.imports: Set[RawImport] = set()
        
    def visit_Import(self, node: ast.Import) -> None:
        """Process Import nodes (e.g., 'import foo as bar')."""
        for name in node.names:
            self.imports.add(RawImport(
                source=name.name,
                asname=name.asname or name.name,
                lineno=node.lineno
            ))
            
    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Process ImportFrom nodes (e.g., 'from foo import bar as baz')."""
        base = '.' * (node.level or 0)
        if node.module:
            base += node.module
            
        for name in node.names:
            if name.name == '*':
                self.imports.add(RawImport(
                    source=f"{base}.*",
                    asname='*',
                    lineno=node.lineno
                ))
            else:
                # Only add the dot if we have a module
                source = f"{base}.{name.name}" if node.module else f"{base}{name.name}"
                self.imports.add(RawImport(
                    source=source,
                    asname=name.asname or name.name,
                    lineno=node.lineno
                ))
        self.generic_visit(node) 