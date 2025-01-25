import typer
import json
from pathlib import Path
from . import analyzer
from . import visterm


app = typer.Typer(
    help="CodeXP - Code Explorer CLI tool",
    add_completion=False,
)

@app.command()
def main(
    source_directory: Path = typer.Argument(
        ...,
        help="Directory containing source code to analyze",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
    no_line_info: bool = typer.Option(
        False,
        "--no-line-info", "-n",
        help="Hide file and line information"
    ),
    json_output: bool = typer.Option(
        False,
        "--json", "-j",
        help="Output results in JSON format"
    ),
):
    """
    Analyze entry points in the specified directory.
    """
    typer.echo(f"Analyzing entry points in: {source_directory}")
    
    package_analyzer = analyzer.PackageAnalyzer(source_directory)
    package_analyzer.analyze()
    
    if json_output:
        print(json.dumps(package_analyzer.to_dict(), indent=2))
    else:
        visterm.visualize_package(package_analyzer, show_line_info=not no_line_info)

if __name__ == "__main__":
    app() 