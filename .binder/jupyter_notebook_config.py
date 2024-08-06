# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'welcome': {
        'command': ['echo', 'This is a placeholder command'],
        'absolute_url': False,
        'launcher_entry': {
            'enabled': True,
            'title': 'Welcome',
        },
    },
}
