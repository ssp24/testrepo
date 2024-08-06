# Traitlet configuration file for jupyter-notebook.

c = get_config()

# Create a launcher entry for welcome.md
c.ServerApp.contents_manager_class = "jupyter_server.services.contents.largefilemanager.LargeFileManager"
c.LabApp.shortcuts = [
    {
        "command": "launcher:create",
        "args": {"kernelName": None, "cwd": None, "filePath": "welcome.md"},
        "category": "Launcher",
        "rank": 1,
        "launcher_entry": {
            'enabled': True,
            'title': 'Welcome',
    }
]

# Optional: Set a custom name for the launcher entry
c.LabApp.shortcuts[-1]["args"]["label"] = "Welcome"
