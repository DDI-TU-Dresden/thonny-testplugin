from thonny import get_workbench


def hello():
    # get content of current notebook
    print(get_workbench().get_editor_notebook().get_current_editor_content())


def load_plugin():
    get_workbench().add_command(
        command_id="hello", menu_name="tools", command_label="Hello!", handler=hello
    )
