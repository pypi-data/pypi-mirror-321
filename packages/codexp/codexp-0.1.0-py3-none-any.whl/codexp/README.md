# CodeXP Package Structure

## Core Modules

### analyzer.py
Core module for static code analysis of Python packages. The `PackageAnalyzer` class:
- Parses Python source into AST
- Tracks imports and dependencies
- Collects symbol definitions and usage
- Builds dependency graphs
- Resolves symbol references

### visterm.py
Terminal visualization module that renders:
- Package structure
- Import relationships
- Symbol definitions and usage
- Source code context
- Color-coded output using `rich`

## Visitor Modules

### import_visitor.py
AST visitor for analyzing Python import statements. Collects and normalizes:
- Regular imports (`import x`)
- Aliased imports (`import x as y`)
- From imports (`from x import y`)
- Relative imports (`.x`)

### symbol_visitor.py
AST visitor for collecting top-level symbol definitions. Tracks module-level:
- Functions
- Classes
- Constants (UPPERCASE)
- Variables
- Main entry points

### symbol_usage_visitor.py
AST visitor for analyzing how imported symbols are used. Tracks:
- Direct references
- Function calls
- Attribute access
- Subscript access
- Separates internal vs external usage

## Entry Point

### __main__.py
Command-line interface that:
- Processes command line arguments
- Initializes the analyzer
- Triggers visualization
- Handles output options

## Data Flow

1. `__main__.py` receives package directory path
2. `PackageAnalyzer` traverses the directory
3. AST visitors collect data:
   - `ImportVisitor` → import statements
   - `SymbolVisitor` → symbol definitions
   - `SymbolUsageVisitor` → symbol usage
4. `visterm.py` visualizes the collected data

## Type Definitions

- `Import`: Normalized import statement
- `RawImport`: Pre-normalized import data
- `SymbolLocation`: Symbol definition location
- `SymbolUsage`: Symbol usage information

## Dependencies

Internal:
- All modules depend on `analyzer.py`
- `visterm.py` depends on visitor results
- Visitors are independent of each other

External:
- `rich`: Terminal visualization
- `typer`: CLI interface
- `ast`: Python standard library 