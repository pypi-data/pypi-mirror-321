from .checks import Container, skip
from .pipify import pipify, setupcommand
from .projectinfo import ProjectInfo
from .util import bgcontainer
from contextlib import contextmanager
from lagoon.text import diff
from pathlib import Path
from shutil import copy2
from tempfile import TemporaryDirectory
import re, sys

@contextmanager
def egginfodir(projectdir, version, dockerenabled):
    with TemporaryDirectory() as tempdir:
        copy2(projectdir / ProjectInfo.projectaridname, tempdir)
        try:
            copy2(projectdir / 'README.md', tempdir)
        except FileNotFoundError:
            pass
        copyinfo = ProjectInfo.seek(tempdir)
        pipify(copyinfo, version)
        if dockerenabled and {'setuptools', 'wheel'} != set(copyinfo.allbuildrequires):
            with bgcontainer('-v', f"{tempdir}:{Container.workdir}", f"python:{copyinfo.pyversiontags[0]}") as container:
                container = Container(container)
                container.inituser()
                for command in ['apt-get', 'update'], ['apt-get', 'install', '-y', 'sudo']:
                    container.call(command, check = True, root = True)
                container.call(['pip', 'install', '--upgrade', 'setuptools'], check = True, root = True)
                container.call(['pip', 'install', *copyinfo.allbuildrequires], check = True, root = True)
                container.call(['python', 'setup.py', 'egg_info'], check = True)
        else:
            setupcommand(copyinfo, False, 'egg_info')
        d, = Path(tempdir).glob('*.egg-info')
        yield tempdir, d

linematch = re.compile('[^<>]|(?:> Requires-Dist|> License-File|[<>] Metadata-Version|< Dynamic): ').match

def metacheck(projectdir, version, dockerenabled):
    if not (projectdir / ProjectInfo.projectaridname).exists():
        return skip
    with egginfodir(projectdir, version, dockerenabled) as (tempdir, d):
        p = d / 'requires.txt'
        q = projectdir / p.relative_to(tempdir)
        if p.exists():
            diff[print](p, q)
        else:
            assert not q.exists()
        p = d / 'PKG-INFO'
        q = projectdir / p.relative_to(tempdir)
        assert q.exists()
        text = diff(p, q, check = False).stdout
        sys.stdout.write(text)
        assert all(linematch(l) is not None for l in text.splitlines())
