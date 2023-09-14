import typer
from opsmate.utils.project_setup import base_setup

app = typer.Typer()
setup = base_setup()

@app.command()
def projsetup(projname: str):
    setup.project_def(project_name=projname)

@app.command()
def hello(name: str):
    print(f"Hello {name}")


def entrypoint():
    app()