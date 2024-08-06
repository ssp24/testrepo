# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['echo', '-p', '{port}', '-d', 'placeholder', '-i', '0.0.0.0'],
        'port': 3333,
        'timeout': 60,
        'launcher_entry': {
            'enabled': True,
            'title': 'OpenRefine Session',
        },
    },
    'welcome': {
        'command': ['echo', 'This is a placeholder command'],
        'absolute_url': False,
        'launcher_entry': {
            'enabled': True,
            'title': 'Welcome',
        },
    },
}
