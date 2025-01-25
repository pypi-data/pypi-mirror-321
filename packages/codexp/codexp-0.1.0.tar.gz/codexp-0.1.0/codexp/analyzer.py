"""
Core module for static code analysis of Python packages.

Provides PackageAnalyzer to:
- Parse Python source into AST
- Track imports and dependencies
- Collect symbol definitions and usage
- Build dependency graphs
- Resolve symbol references
"""

import ast
import os
from pathlib import Path
from typing import Dict, List, Set, Optional, NamedTuple
from pprint import pprint
from collections import namedtuple
from .import_visitor import ImportVisitor, RawImport
from .symbol_visitor import SymbolTopLevelVisitor
from .symbol_usage_visitor import SymbolUsageVisitor

# Define our named tuples
class Import(NamedTuple):
    """Represents a normalized import statement.
    
    Attributes:
        module_path: Full module path (e.g. 'package.submodule.symbol')
        source_file: Path to source file relative to package root (e.g. 'submodule/file.py')
        symbol_name: Name used in importing module (may differ from original if using 'as')
        lineno: Line number where the import occurs
    """
    module_path: str
    source_file: str
    symbol_name: str
    lineno: int

class PackageAnalyzer:
    """Analyzes Python package structure and dependencies using AST."""
    
    def __init__(self, package_dir: str):
        """Initialize analyzer with package directory.
        
        Args:
            package_dir: Path to the root directory of the Python package
        """
        self.package_root = Path(package_dir)
        self.modules: Dict[str, ast.Module] = {}  # source_file -> AST
        self.imports: Dict[str, Set[Import]] = {}  # source_file -> set of imports
        self.module_symbols: Dict[str, Dict[str, int]] = {}  # source_file -> {symbol -> line_no}
        self.entry_point: Optional[str] = None
        self.symbol_usages: Dict[str, Dict] = {}  # source_file -> {internal: [usages], external: [usages]}
        self.constants: Dict[str, Dict[str, int]] = {}  # source_file -> {constant -> line_no}
        self.globals: Dict[str, Dict[str, int]] = {}  # source_file -> {global_var -> line_no}
        
    def analyze_entry_points(self) -> None:
        """Analyze the package's entry points."""
        found_entry_point = False
        
        # Check for root __init__.py
        init_file = self.package_root / '__init__.py'
        if init_file.exists():
            self.analyze_file(init_file)
            found_entry_point = True
        
        # Check for __main__.py
        main_file = self.package_root / '__main__.py'
        if main_file.exists():
            self.entry_point = '__main__.py'
            self.analyze_file(main_file)
            found_entry_point = True
        
        if not found_entry_point:
            raise FileNotFoundError("No __main__.py or __init__.py found in package root")

    def _get_module_name(self, file_path: Path) -> str:
        """Convert file path to module name.
        
        Args:
            file_path: Path to the Python file
            
        Returns:
            str: Module name in dot notation
        """
        rel_path = file_path.relative_to(self.package_root)
        return str(rel_path).replace(os.sep, '.').replace('.py', '')

    def _find_module_file(self, module_name: str) -> Optional[Path]:
        """Find the file path for a module name.
        
        Args:
            module_name: Module name in dot notation
            
        Returns:
            Optional[Path]: Path to the module file if found
        """
        # Handle package.module.submodule notation
        parts = module_name.split('.')
        
        # Try direct path first
        potential_path = self.package_root.joinpath(*parts).with_suffix('.py')
        if potential_path.exists():
            return potential_path
            
        # Try as a module in a package
        if len(parts) > 1:
            package_path = self.package_root.joinpath(*parts[:-1])
            module_file = package_path / f"{parts[-1]}.py"
            if module_file.exists():
                return module_file
                
        return None

    def _get_source_file(self, module_path: str) -> str:
        """Get the source file path for a module path."""
        # Strip package name prefix since package_root is already the package directory
        package_name = self.package_root.name
        if module_path.startswith(package_name + '.'):
            module_path = module_path[len(package_name)+1:]
        
        parts = module_path.split('.')
        current_path = self.package_root
        file_parts = []
        
        # Try resolving each part of the path
        for i, part in enumerate(parts):
            remaining_parts = parts[i:]
            current_path = current_path / part
            file_parts.append(part)
            
            # Check if this part is a package
            init_file = current_path / '__init__.py'
            if init_file.exists():
                # Analyze __init__.py to find its symbols
                with open(init_file, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=str(init_file))
                    
                # Add parent references to all nodes
                for parent in ast.walk(tree):
                    for child in ast.iter_child_nodes(parent):
                        child.parent = parent
                
                symbol_visitor = SymbolTopLevelVisitor(str(init_file))
                symbol_visitor.visit(tree)
                
                # If the symbol we're looking for is defined in __init__.py
                if i == len(parts) - 1 or parts[-1] in symbol_visitor.symbols:
                    return f"{self.package_root.name}/{'/'.join(file_parts)}/__init__.py"
                continue  # Keep going deeper if symbol not found
            
            # Check if this part is a module
            module_file = current_path.with_suffix('.py')
            if module_file.exists():
                if i == len(parts) - 1:  # If this is the last part
                    return f"{self.package_root.name}/{'/'.join(file_parts)}.py"
                # If not last part, try remaining parts as attributes
                return f"{self.package_root.name}/{'/'.join(file_parts)}.py"
            
            # If we get here and haven't found anything, try remaining parts as one module
            if i < len(parts) - 1:
                combined_remaining = '_'.join(remaining_parts)
                module_file = current_path.parent / f"{combined_remaining}.py"
                if module_file.exists():
                    file_parts.pop()  # Remove last part since we're using combined
                    return f"{self.package_root.name}/{'/'.join(file_parts)}/{combined_remaining}.py"
        
        return f"{self.package_root.name}/{'/'.join(file_parts)}.py"

    def _normalize_import_path(self, current_module: str, import_path: str) -> tuple[str, str]:
        """Convert relative import path to absolute path and get source file.
        
        Args:
            current_module: Module doing the import
            import_path: Import path to normalize
            
        Returns:
            tuple[str, str]: (normalized path, source file)
        """
        package_name = self.package_root.name
        
        # If already starts with package name, return as is
        if import_path.startswith(package_name + '.'):
            source_file = self._get_source_file(import_path)
            return import_path, source_file
        
        # If absolute import but doesn't start with package name and exists in project
        if not import_path.startswith('.'):
            module_path = self.package_root / import_path.replace('.', '/')
            if (module_path.with_suffix('.py').exists() or 
                (module_path / '__init__.py').exists()):
                normalized = f"{package_name}.{import_path}"
                source_file = self._get_source_file(normalized)
                return normalized, source_file
            return import_path, import_path  # External import
        
        # Handle relative imports
        dots = 0
        while import_path.startswith('.'):
            dots += 1
            import_path = import_path[1:]
        
        current_parts = current_module.split('.')
        
        if dots > len(current_parts):
            return None, None  # Invalid relative import
        target_parts = current_parts[:-dots] if dots else current_parts
        
        if import_path:
            target_parts.append(import_path)
        
        # Ensure result starts with package name
        if not target_parts[0] == package_name:
            target_parts.insert(0, package_name)
        
        normalized = '.'.join(target_parts)
        source_file = self._get_source_file(normalized)
        return normalized, source_file

    def analyze_file(self, file_path: Path) -> None:
        """Analyze a single Python file for imports and symbols."""
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()
            tree = ast.parse(source, filename=str(file_path))
        
        # Add parent references to all nodes
        for parent in ast.walk(tree):
            for child in ast.iter_child_nodes(parent):
                child.parent = parent
                
        # Use package-relative path for source_file
        source_file = f"{self.package_root.name}/{file_path.name}"
        module_name = self._get_module_name(file_path)
        
        # Store using source_file as key
        self.modules[source_file] = tree
        self.imports[source_file] = set()
        self.module_symbols[source_file] = {}
        
        # Collect imports with their source paths
        import_visitor = ImportVisitor()
        import_visitor.visit(tree)
        
        # Normalize relative imports before storing
        normalized_imports = set()
        for raw_import in import_visitor.imports:
            if raw_import.source.startswith('.'):
                normalized_path, import_source_file = self._normalize_import_path(module_name, raw_import.source)
                if normalized_path:
                    normalized_imports.add(Import(
                        module_path=normalized_path,
                        source_file=import_source_file,
                        symbol_name=raw_import.asname,
                        lineno=raw_import.lineno
                    ))
            else:
                if raw_import.source.startswith(self.package_root.name):
                    # Internal import - resolve source file
                    import_source_file = self._get_source_file(raw_import.source)
                    normalized_imports.add(Import(
                        module_path=raw_import.source,
                        source_file=import_source_file,
                        symbol_name=raw_import.asname,
                        lineno=raw_import.lineno
                    ))
                else:
                    # External import - use "External"
                    normalized_imports.add(Import(
                        module_path=raw_import.source,
                        source_file="External",
                        symbol_name=raw_import.asname,
                        lineno=raw_import.lineno
                    ))
                
        self.imports[source_file].update(normalized_imports)
        
        # Collect symbols including constants and globals
        symbol_visitor = SymbolTopLevelVisitor(source_file)
        symbol_visitor.visit(tree)
        self.module_symbols[source_file].update(symbol_visitor.symbols)
        self.constants[source_file] = symbol_visitor.constants
        self.globals[source_file] = symbol_visitor.globals
        
        # Separate internal and external imported symbols
        internal_symbols = {imp.symbol_name for imp in self.imports[source_file] 
                           if imp.source_file != "External"}
        external_symbols = {imp.symbol_name for imp in self.imports[source_file] 
                           if imp.source_file == "External"}
        
        # Track symbol usage
        usage_visitor = SymbolUsageVisitor(
            internal_symbols=internal_symbols,
            external_symbols=external_symbols,
            constants={name for name in symbol_visitor.constants}
        )
        usage_visitor.visit(tree)
        self.symbol_usages[source_file] = {
            'internal': usage_visitor.internal_usages,
            'external': usage_visitor.external_usages
        }

    def _should_analyze_file(self, file_path: Path) -> bool:
        """Determine if a file should be analyzed based on path.
        
        Args:
            file_path: Path to the Python file
            
        Returns:
            bool: True if file should be analyzed, False otherwise
        """
        # Skip virtual environments, tests, etc.
        excluded = {'.venv', 'venv', '.tox', '.eggs', 'tests', '__pycache__'}
        return not any(part in excluded for part in file_path.parts)

    def analyze(self) -> None:
        """Start the analysis process by analyzing the package entry points."""
        self.analyze_entry_points()

    def get_analysis_results(self) -> Dict[str, Dict]:
        """Get the results of the analysis.
        
        Returns:
            Dict containing:
            - modules: Dict[str, ast.Module] - AST for each module
            - imports: Dict[str, Set[str]] - imports per module
            - symbols: Dict[str, Set[str]] - defined symbols per module
            - entry_point: str - main module path
            - package_root: Path - root directory of the package
        """
        return {
            'modules': self.modules,
            'imports': self.imports,
            'symbols': self.module_symbols,
            'entry_point': self.entry_point,
            'package_root': self.package_root
        }

    def to_dict(self) -> dict:
        """Convert analysis results to a structured dictionary format.
        
        Returns:
            Dict containing analysis results in a JSON-friendly format.
        """
        def format_symbol_location(symbol_name: str, location) -> dict:
            """Format a symbol location into a structured dict."""
            return {
                "name": symbol_name,
                "source": location.file_path,
                "line": location.line_no
            }

        def format_symbol_usage(usage) -> dict:
            """Format a symbol usage into a structured dict."""
            return {
                "symbol": usage.symbol,
                "source": usage.source_file if hasattr(usage, 'source_file') else None,
                "line": usage.line_no
            }

        return {
            'package_root': str(self.package_root),
            'entry_point': self.entry_point,
            'modules': [
                {
                    "path": module_path,
                    "type": "module"
                }
                for module_path in self.modules.keys()
            ],
            'imports': {
                src: [
                    {
                        "module": imp.module_path,
                        "symbol": imp.symbol_name,
                        "source": imp.source_file,
                        "line": imp.lineno,
                        "type": "external" if imp.source_file == "External" else "internal"
                    }
                    for imp in imports
                ]
                for src, imports in self.imports.items()
            },
            'symbols': {
                module: [
                    format_symbol_location(name, location)
                    for name, location in symbols.items()
                ]
                for module, symbols in self.module_symbols.items()
            },
            'symbol_usage': {
                src: {
                    'internal': [format_symbol_usage(usage) for usage in usages['internal']],
                    'external': [format_symbol_usage(usage) for usage in usages['external']]
                }
                for src, usages in self.symbol_usages.items()
            }
        }
