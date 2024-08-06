# Traitlet configuration file for jupyter-notebook.

c = get_config()

c.ServerProxy.servers = {
    'welcome': {
        'command': ['echo', 'This is a placeholder command'],
        'absolute_url': False,
        'launcher_entry': {
            'enabled': True,
            'icon_path': '/home/jovyan/binder/welcome-icon.svg',
            'title': 'Welcome',
        },
    },
}

def launch_welcome(url):
    return '/lab/tree/welcome.md'

c.ServerProxy.host_whitelist = ['localhost']

c.ServerProxy.handlers = [
    ('welcome', launch_welcome),
]
