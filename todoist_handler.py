import todoist
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('todoist_api_token')
project = os.getenv('project_id')

api = todoist.TodoistAPI(token)

def add_items(items):
    for item in items:
        api.items.add(item, project_id=project)  # oh no, typo!
    api.commit()  # commit the changes to the server

def list_items():
    project_data = api.projects.get_data(project)
    dirty_items = project_data['items']
    items = []
    for item in dirty_items:
        items.append(item['content'])
    
    return items

if __name__ == '__main__':
    list_items()