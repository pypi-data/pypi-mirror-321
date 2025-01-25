"""
Terminal visualization module for code analysis results.

Renders:
- Package structure
- Import relationships
- Symbol definitions
- Symbol usage
- Source code context
"""

from rich.console import Console
from rich.tree import Tree
from rich.panel import Panel
from rich import print as rprint
from typing import Dict, Set, List
from .analyzer import PackageAnalyzer, Import
from rich.text import Text
from pathlib import Path

def get_line_content(file_path: Path, line_no: int) -> str:
    """Get content of a specific line from a file.
    
    Args:
        file_path: Path to the file to read
        line_no: Line number to get (1-based)
        
    Returns:
        str: The line content
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines[line_no - 1].rstrip('\n')  # Keep indentation, just remove newline

def get_file_path(package_root: Path, source_file: str) -> Path:
    """Get the actual file path, removing duplicate package name.
    
    Args:
        package_root: Root directory of the package
        source_file: Source file path (e.g. 'package/file.py')
        
    Returns:
        Path: Correct file path without package name duplication
    """
    # Remove package name from source_file since it's already in package_root
    parts = source_file.split('/')
    if parts[0] == package_root.name:
        parts = parts[1:]
    return package_root.joinpath(*parts)

def format_imports(imports: List[Import], prefix: str, source_file: str, package_root: Path, show_line_info: bool = True, is_external: bool = False) -> List[Text]:
    """Format a list of imports with aligned columns.
    
    Args:
        imports: List of Import objects to format
        prefix: Line prefix for tree structure
        source_file: The source file from which the imports are imported
        package_root: The root directory of the package
        show_line_info: Whether to include file and line information
        is_external: Whether these are external imports
    
    Returns:
        List of formatted Text objects
    """
    if not imports:
        return []
        
    # Sort imports
    sorted_imports = sorted(imports, key=lambda x: (x.module_path, x.symbol_name))
    
    # Calculate maximum lengths for alignment
    max_module_len = max(len(imp.module_path) for imp in sorted_imports)
    max_symbol_len = max(len(imp.symbol_name) + 2 for imp in sorted_imports)  # +2 for []
    max_file_len = max(len(source_file) for imp in sorted_imports)
    max_line_len = max(len(str(imp.lineno)) for imp in sorted_imports)
    
    lines = []
    for imp in sorted_imports:
        text = Text()
        text.append(prefix)  # Tree structure
        text.append("| ", style="dim")  # Import prefix
        
        # Module path and symbol columns
        text.append(f"{imp.module_path:<{max_module_len}}", style="cyan")
        text.append(" ")  # Space between module and symbol
        text.append(f"[{imp.symbol_name}]".ljust(max_symbol_len), style="green" if is_external else "cyan")
        
        if show_line_info:
            text.append("  ")
            file_line = f"{source_file}:{str(imp.lineno)}"
            text.append(f"{file_line:<{max_file_len + max_line_len + 1}}", style="blue")
        
        # Get line content
        file_path = get_file_path(package_root, source_file)
        line_content = get_line_content(file_path, imp.lineno)
        
        text.append("  ║  ", style="dim")
        text.append(line_content, style="yellow")
            
        lines.append(text)
    
    return lines

def format_symbols(symbols: Dict[str, 'SymbolLocation'], package_root: Path, show_line_info: bool = True) -> List[Text]:
    """Format symbols with aligned columns."""
    if not symbols:
        return []
        
    # Calculate maximum lengths for alignment
    max_symbol_len = max(len(name) for name in symbols.keys())
    max_file_len = max(len(loc.file_path) for loc in symbols.values())
    max_line_len = max(len(str(loc.line_no)) for loc in symbols.values())
    
    lines = []
    for name, location in sorted(symbols.items()):
        text = Text()
        text.append("    │   ")  # Tree structure
        text.append("| ", style="dim")  # Symbol prefix
        
        # Symbol name column
        if name == "__main__":
            text.append("__main__", style="bold yellow")
            text.append(" " * (max_symbol_len - 8))
        else:
            text.append(f"{name:<{max_symbol_len}}", style="cyan")
            
        text.append("  ")
        
        # File path and line number column
        file_line = f"{location.file_path}:{str(location.line_no)}"
        text.append(f"{file_line:<{max_file_len + max_line_len + 1}}", style="blue")
        
        # Get line content
        file_path = get_file_path(package_root, location.file_path)
        line_content = get_line_content(file_path, location.line_no)
        
        text.append("  ║  ", style="dim")
        text.append(line_content, style="yellow")
        lines.append(text)
    
    return lines

def visualize_package(analyzer: PackageAnalyzer, show_line_info: bool = True) -> None:
    """Visualize package structure and dependencies.
    
    Args:
        analyzer: PackageAnalyzer instance with analysis results
        show_line_info: Whether to include file and line information (default: True)
    """
    results = analyzer.get_analysis_results()
    package_root = results['package_root']
    console = Console()
    
    console.print("\nPackage Structure:")
    console.print("├── Entry Points")
    
    if results['entry_point']:
        text = Text("│   └── ", style="dim")
        text.append(results['entry_point'], style="cyan")
        console.print(text)
    
    console.print("├── Modules")
    max_module_len = max(len(module) for module in results['modules'].keys())
    for module in sorted(results['modules'].keys()):
        text = Text("│   └── ", style="dim")
        text.append(f"{module:<{max_module_len}}", style="cyan")
        console.print(text)
    
    console.print("├── Imports")
    console.print("│   ├── Internal")
    # Group by source module first
    for source_file, imports in sorted(results['imports'].items()):
        internal_imports = [imp for imp in imports if imp.source_file != "External"]
        if internal_imports:
            for line in format_imports(internal_imports, "│   │   ", source_file=source_file, package_root=package_root, show_line_info=show_line_info):
                console.print(line)
    
    console.print("│   └── External")
    for source_file, imports in sorted(results['imports'].items()):
        external_imports = [imp for imp in imports if imp.source_file == "External"]
        if external_imports:
            for line in format_imports(external_imports, "│       ", source_file=source_file, package_root=package_root, show_line_info=show_line_info, is_external=True):
                console.print(line)
    
    console.print("└── Top Level Symbols")
    for module, symbols in sorted(results['symbols'].items()):
        if symbols:
            text = Text("    ├── ", style="dim")
            text.append(module, style="cyan")
            console.print(text)
            for line in format_symbols(symbols, package_root, show_line_info):
                console.print(line)

    console.print("└── Symbol Usage")
    for source_file, usages in sorted(analyzer.symbol_usages.items()):
        if usages['internal'] or usages['external']:
            text = Text("    ├── ", style="dim")
            text.append(source_file, style="cyan bold")
            console.print(text)
            
            if usages['internal']:
                console.print("    │   ├── Internal")
                for usage in sorted(usages['internal'], key=lambda u: (u.symbol, u.line_no)):
                    text = Text("    │   │   ")
                    text.append("| ", style="dim")
                    text.append(f"{usage.symbol:<30}", style="cyan")
                    
                    if show_line_info:
                        file_line = f"{source_file}:{str(usage.line_no)}"
                        text.append(f"{file_line:<{len(source_file) + 5}}", style="blue")
                    
                    # Get line content
                    file_path = get_file_path(package_root, source_file)
                    line_content = get_line_content(file_path, usage.line_no)
                    
                    text.append("  ║  ", style="dim")
                    text.append(line_content, style="yellow")
                    console.print(text)
                    
            if usages['external']:
                console.print("    │   └── External")
                for usage in sorted(usages['external'], key=lambda u: (u.symbol, u.line_no)):
                    text = Text("    │       ")
                    text.append("| ", style="dim")
                    text.append(f"{usage.symbol:<30}", style="green")
                    
                    if show_line_info:
                        file_line = f"{source_file}:{str(usage.line_no)}"
                        text.append(f"{file_line:<{len(source_file) + 5}}", style="blue")
                    
                    # Get line content
                    file_path = get_file_path(package_root, source_file)
                    line_content = get_line_content(file_path, usage.line_no)
                    
                    text.append("  ║  ", style="dim")
                    text.append(line_content, style="yellow")
                    console.print(text)
