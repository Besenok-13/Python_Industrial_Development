from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from task_notifier import configure_transport
from task_web import TaskStore
from task_workflow import completion_for_dashboard

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
app = FastAPI(title="Team Board")
store = TaskStore()


@app.on_event("startup")
def prepare_application() -> None:
    configure_transport()
    store.seed()


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request) -> HTMLResponse:
    tasks = store.list_tasks()
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"tasks": tasks, "completion": completion_for_dashboard(tasks)},
    )
