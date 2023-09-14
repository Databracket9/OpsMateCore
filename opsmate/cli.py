import typer
from utils.project_setup import base_setup

app = typer.Typer()
# setup = base_setup()

@app.command()
def primesetup(projname: str):
    print(projname)
    base_setup().project_def(project_name=projname)

@app.command()
def hello(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()