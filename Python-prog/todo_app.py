import streamlit as st
import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f)

st.title("📝 To-Do List App")

tasks = load_tasks()

new_task = st.text_input("Add a task")
if st.button("Add"):
    if new_task.strip():
        tasks.append({'title': new_task.strip(), 'done': False})
        save_tasks(tasks)
        st.success(f"Added: {new_task}")
        st.rerun()

for i, task in enumerate(tasks[:]):
    col1, col2 = st.columns([0.85, 0.15])
    display_title = f"~~{task['title']}~~" if task['done'] else task['title']
    checked = col1.checkbox(display_title, value=task['done'], key=f"checkbox_{i}")

    if checked != task['done']:
        tasks[i]['done'] = checked
        save_tasks(tasks)
        st.rerun()

    if col2.button("❌", key=f"delete_{i}"):
        tasks.pop(i)
        save_tasks(tasks)
        st.rerun()

st.caption(f"📋 Total Tasks: {len(tasks)}")

st.markdown(
    """
    <div style='text-align: center; font-size: 0.85rem; color: gray;'>
        Created by <a href='https://pragadeeshfolio.netlify.app/' target='_blank'>Pragadeesh Srinivasan</a>
    </div>
    """,
    unsafe_allow_html=True
)

