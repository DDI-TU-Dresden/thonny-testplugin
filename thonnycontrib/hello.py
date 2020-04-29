from thonny import get_workbench
from tkinter.messagebox import showinfo


def hello():
    # Draw Info tkinter messagebox
    # showinfo(Hello!, Thonny rules!)

    # get filename of open file
    # for editor in get_workbench().get_editor_notebook().get_all_editors():
    # print(editor.get_filename())
    # print(get_workbench().get_current_editor().get_filename())

    # get content of current notebook
    print(get_workbench().get_editor_notebook().get_current_editor_content())


def load_plugin():
    get_workbench().add_command(
        command_id="hello", menu_name="tools", command_label="Hello!", handler=hello
    )
