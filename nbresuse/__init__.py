from nbresuse.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'nbresuse',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "nbresuse",
        "src": "static",
        "require": "nbresuse/mainmainmain"
    }]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("my module enabled!"),
    setup_handlers(nbapp.web_app)
