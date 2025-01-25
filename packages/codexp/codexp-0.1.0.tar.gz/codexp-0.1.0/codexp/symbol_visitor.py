"""
AST visitor for collecting top-level symbol definitions.

Tracks module-level:
- Functions
- Classes 
- Constants
- Variables
- Main entry points
"""

import ast
from typing import Dict, NamedTuple, List

class SymbolLocation(NamedTuple):
    """Location information for a symbol.
    
    Attributes:
        file_path: Path to the file containing the symbol
        line_no: Line number where the symbol is defined
    """
    file_path: str
    line_no: int

class SymbolTopLevelVisitor(ast.NodeVisitor):
    """AST visitor to collect top-level defined symbols.
    
    Collects only module-level symbols:
    - Function definitions
    - Class definitions
    - Top-level assignments
    - Main entry point (if __name__ == "__main__")
    """
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.symbols: Dict[str, SymbolLocation] = {}
        self.constants: Dict[str, SymbolLocation] = {}
        self.globals: Dict[str, SymbolLocation] = {}  # Add tracking for globals
        self.has_main_entry = False
        self.main_entry_line = None
        
    def visit_If(self, node: ast.If) -> None:
        """Process if statements to detect main entry point."""
        if isinstance(node.parent, ast.Module):  # Only check module-level if statements
            # Check if it's an if __name__ == "__main__" block
            if (isinstance(node.test, ast.Compare) and 
                isinstance(node.test.left, ast.Name) and node.test.left.id == "__name__" and
                len(node.test.ops) == 1 and isinstance(node.test.ops[0], ast.Eq) and
                len(node.test.comparators) == 1 and 
                isinstance(node.test.comparators[0], ast.Constant) and 
                node.test.comparators[0].value == "__main__"):
                
                self.has_main_entry = True
                self.main_entry_line = node.lineno
                self.symbols["__main__"] = SymbolLocation(self.file_path, node.lineno)
        
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Process top-level function definitions."""
        if isinstance(node.parent, ast.Module):  # Only collect module-level functions
            name = f"{node.name}(...)"  # Show (...) to indicate it's callable with params
            self.symbols[name] = SymbolLocation(self.file_path, node.lineno)
        
    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Process top-level class definitions."""
        if isinstance(node.parent, ast.Module):  # Only collect module-level classes
            name = f"{node.name}(...)"  # Show (...) to indicate it's instantiable with possible params
            self.symbols[name] = SymbolLocation(self.file_path, node.lineno)
        
    def visit_Global(self, node: ast.Global) -> None:
        """Process global statements."""
        for name in node.names:
            self.globals[name] = SymbolLocation(
                file_path=self.file_path,
                line_no=node.lineno
            )
            # Also add to symbols with GLOBAL prefix
            self.symbols[f"GLOBAL {name}"] = SymbolLocation(
                file_path=self.file_path,
                line_no=node.lineno
            )
            
    def visit_Assign(self, node: ast.Assign) -> None:
        """Process assignments.
        
        Identifies:
        - Module-level constants (UPPERCASE)
        - Module-level variables
        - Global variables
        """
        # Check module-level assignments
        if isinstance(node.parent, ast.Module):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    name = target.id
                    location = SymbolLocation(self.file_path, node.lineno)
                    
                    # Track constants separately
                    if name.isupper():
                        self.constants[name] = location
                        name = f"CONST {name}"
                    
                    self.symbols[name] = location
                    
        # Check assignments to global variables
        elif isinstance(target, ast.Name) and target.id in self.globals:
            location = SymbolLocation(self.file_path, node.lineno)
            self.globals[target.id] = location  # Update global location
            self.symbols[f"GLOBAL {target.id}"] = location
        