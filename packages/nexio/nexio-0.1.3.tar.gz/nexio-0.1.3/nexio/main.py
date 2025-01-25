import typer
import nexio.jobs
import nexio.todoist
import nexio.inbox

app = typer.Typer()
app.add_typer(nexio.jobs.app, name="jobs")
app.add_typer(nexio.todoist.app, name="todoist")
app.add_typer(nexio.inbox.app, name="inbox")
