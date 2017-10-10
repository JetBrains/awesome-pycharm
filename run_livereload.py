"""

Automatically re-build Sphinx docs while editing, serve docs on an
HTTP port, and also reload any browsers pointed to the docs.

"""
import glob

from livereload import Server, shell
from livereload.watcher import Watcher


class CustomWatcher(Watcher):
    """ Handle recursive globs with Python 3.5+ globbing  """

    def is_glob_changed(self, path, ignore=None):
        for f in glob.glob(path, recursive=True):
            if self.is_file_changed(f, ignore):
                return True
        return False


server = Server(watcher=CustomWatcher())
server.watch('docs/**', shell('make html', cwd='docs'),
             ignore=lambda s: '_build' in s)
server.serve(root='docs/_build/html', live_css=False)
