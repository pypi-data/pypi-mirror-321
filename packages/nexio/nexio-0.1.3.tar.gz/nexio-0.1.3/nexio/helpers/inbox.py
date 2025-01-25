import re
import pandas as pd
from nexio.utils.postgres import Postgres
from nexio.helpers.todoist import TodoistHelper
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from rich import print
from rich.progress import track


class StoreOptions(str, Enum):
    no_store = "no_store"
    csv = "csv"
    postgres = "postgres"


class TodoistUnit(BaseModel):
    name: str = Field(description="Job name", default="")
    saved_at: str = Field(description="Job saved date/time", default="")
    content: str = Field(description="Job content", default="")
    description: str = Field(description="Job description", default="")
    due_at: Optional[str] = Field(description="Job due date/time", default="")
    id: int = Field(description="Job ID", default="")
    label: List[str] = Field(description="Job labels", default="")
    order: int = Field(description="Job order", default=0)
    priority: int = Field(description="Job priority", default=0)
    project_id: str = Field(description="Job's project ID", default="")
    project_name: str = Field(description="Job's project name", default="")
    section_id: Optional[int] = Field(description="Job's section ID", default="")
    url: str = Field(description="Job's URL", default="")


class InboxManagerTodoist:
    def __init__(self):
        self._todoist_helper = TodoistHelper()
        self._project_parent = dict(name="0_jr_inbox", id="2343658323")
        self._project_children = self._todoist_helper.get_project_children(parent_id=self._project_parent['id'])

    def get_units(self):
        project_ids = [project_id for project_id in self._project_children.keys()]
        tasks = self._todoist_helper.get_tasks(project_ids=project_ids)
        units = []
        for id, task in track(enumerate(tasks)):
            name, url = self._parse_content(content=task.content)
            units.append(TodoistUnit(
                id=task.id,
                name=name,
                saved_at=task.created_at,
                content=task.content,
                description=task.description,
                due_at=str(task.due),
                label=task.labels,
                order=task.order,
                priority=task.priority,
                project_id=task.project_id,
                project_name=self._project_children.get(task.project_id),
                section_id=task.section_id,
                url=url,
            ))
            print(f"{id} -- {units[-1].project_name}\n\t{units[-1].content[:100]}\n")

        return units

    @staticmethod
    def _parse_content(content):
        # Regular expression to extract the job_name and url
        pattern = r'\[(.*?)\]\((.*?)\)'

        # Use re.search to extract the groups
        match = re.search(pattern, content)

        if match:
            job_name = match.group(1)
            url = match.group(2)
            return job_name, url

        return content, ""

    @staticmethod
    def store(store_options: StoreOptions, items: List[TodoistUnit], output: str):
        # if store_options == StoreOptions.csv:
        #     InboxManagerTodoist._store_to_csv(items, output)

        # if store_options == StoreOptions.postgres:
        InboxManagerTodoist._store_to_postgres(units=items)

    @staticmethod
    def _store_to_csv(items, output):
        if output is None:
            raise ValueError("Output cannot be None")

        items = [item.model_dump() for item in items]
        df = pd.DataFrame(items)
        # cols = ['name', 'saved_at', 'content', 'description', 'due_at', 'id', 'label',
        #         'order', 'priority', 'project_id', 'project_name', 'section_id', 'url'],
        new_order = ['id', 'name', 'order', 'project_name', 'url', 'saved_at', 'content', 'description', 'due_at',
                     'label', 'priority', 'project_id', 'section_id']
        df = df[new_order]
        df.to_csv(output, index=False)
        print(df.head(5))

    @staticmethod
    def _store_to_postgres(units: List[TodoistUnit]):
        postgres = Postgres()
        postgres.connect()
        postgres.conn.autocommit = True
        cursor = postgres.conn.cursor()

        insert_query = """
           INSERT INTO inbox (
               id, "order", name, url, label, saved_at, project_id, due_at, description, section_id, priority, content, project_name 
           ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
           ON CONFLICT (id) DO NOTHING;  -- Prevents duplicates based on 'id'
           """

        # Iterate over DataFrame rows and insert them
        for unit in track(units):
            try:
                cursor.execute(insert_query, (
                    unit.id,
                    unit.order,
                    unit.name,
                    unit.url,
                    unit.label,
                    unit.saved_at,
                    unit.project_id,
                    unit.due_at,
                    unit.description,
                    unit.section_id,
                    unit.priority,
                    unit.content,
                    unit.project_name,
                ))
                print(f"Storing to postgres db: {unit.project_name} -- {unit.id}")
                # postgres.conn.commit()
            except Exception as e:
                print(f"Error on row {unit.content}: {e}")

        cursor.close()
        postgres.conn.close()
