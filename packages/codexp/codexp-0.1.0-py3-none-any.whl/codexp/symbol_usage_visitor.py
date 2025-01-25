"""
AST visitor for analyzing how imported symbols are used.

Tracks symbol usage as:
- Direct references
- Function calls
- Attribute access
- Subscript access

Separates internal vs external symbol usage.
"""

import ast
from typing import Dict, List, NamedTuple, Set

class SymbolUsage(NamedTuple):
    """Information about where and how a symbol is used.
    
    Attributes:
        symbol: The symbol being used
        line_no: Line number where the usage occurs
        context: Type of usage (call, attribute, subscript, etc.)
    """
    symbol: str
    line_no: int
    context: str

class SymbolUsageVisitor(ast.NodeVisitor):
    """AST visitor to track usage of imported symbols.
    
    Tracks:
    - Direct symbol usage (e.g., symbol)
    - Attribute access (e.g., symbol.attr)
    - Subscript access (e.g., symbol[key])
    - Function calls (e.g., symbol())
    
    Separates internal and external symbol usage.
    """
    
    def __init__(self, internal_symbols: Set[str], external_symbols: Set[str], constants: Set[str]):
        self.internal_symbols = internal_symbols
        self.external_symbols = external_symbols
        self.constants = constants  # Add tracking of known constants
        self.internal_usages: List[SymbolUsage] = []
        self.external_usages: List[SymbolUsage] = []
        self.constant_usages: List[SymbolUsage] = []  # Add specific tracking for constant usage
        
    def visit_Name(self, node: ast.Name) -> None:
        """Process name nodes to find direct symbol usage."""
        # Skip if this name is part of an attribute access
        if isinstance(node.parent, ast.Attribute) and node.parent.value == node:
            return
        
        context = self._get_usage_context(node)
        
        # Check if it's a constant usage
        if node.id in self.constants:
            self.constant_usages.append(SymbolUsage(
                symbol=node.id,
                line_no=node.lineno,
                context=f"constant_{context}"  # Mark constant usage specifically
            ))
            
        if node.id in self.internal_symbols:
            self.internal_usages.append(SymbolUsage(
                symbol=node.id,
                line_no=node.lineno,
                context=context
            ))
            
        if node.id in self.external_symbols:
            self.external_usages.append(SymbolUsage(
                symbol=node.id,
                line_no=node.lineno,
                context=context
            ))
            
        self.generic_visit(node)
        
    def _get_usage_context(self, node: ast.AST) -> str:
        """Determine how a symbol is being used based on its parent node."""
        parent = node.parent
        
        if isinstance(parent, ast.Call) and parent.func == node:
            return "call"
        elif isinstance(parent, ast.Attribute):
            return "attribute"
        elif isinstance(parent, ast.Subscript) and parent.value == node:
            return "subscript"
        elif isinstance(parent, ast.Assign) and node in parent.targets:
            return "assignment_target"
        elif isinstance(parent, ast.Assign):
            return "assignment_value"
        elif isinstance(parent, ast.arg):
            return "parameter"
        elif isinstance(parent, ast.Return):
            return "return"
        else:
            return "reference"
            
    def visit_Attribute(self, node: ast.Attribute) -> None:
        """Process attribute access to track chained usage."""
        if isinstance(node.value, ast.Name):
            if node.value.id in self.internal_symbols:
                self.internal_usages.append(SymbolUsage(
                    symbol=f"{node.value.id}.{node.attr}",
                    line_no=node.lineno,
                    context="attribute_access"
                ))
            if node.value.id in self.external_symbols:
                self.external_usages.append(SymbolUsage(
                    symbol=f"{node.value.id}.{node.attr}",
                    line_no=node.lineno,
                    context="attribute_access"
                ))
        self.generic_visit(node) 