import typer
from dotenv import load_dotenv, find_dotenv
from typing import Optional
from nexio.helpers.inbox import StoreOptions, InboxManagerTodoist

load_dotenv(find_dotenv())
app = typer.Typer()


@app.command()
def pull(store: StoreOptions = StoreOptions.no_store, output: Optional[str] = None):
    manager = InboxManagerTodoist()
    units = manager.get_units()
    manager.store(store_options=store, items=units, output=output)


if __name__ == '__main__':
    app()
