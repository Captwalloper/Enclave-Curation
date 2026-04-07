import asyncio, shutil, os
from pathlib import Path
from invoke import task, Context
import stellaris

PROJ_DIR = Path(__file__).resolve().parent
REPO_MOD_DIR = PROJ_DIR / "Enclave Curation"
DEPLOYED_MOD_DIR = Path.home() / "Documents" / "Paradox Interactive" / "Stellaris" / "mod" / "Enclave Curation"

def overwrite_folder(src_path: str, dst_path: str):
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
    shutil.copytree(src_path, dst_path)

@task
def restore(c: Context):
    """Use pip to ensure dependencies are installed"""
    c.run('pip install -r requirements.txt')

@task
def launch(c: Context):
    """Launch Stellaris"""
    stellaris.launch()

@task
def kill(c: Context):
    """Kill Stellaris"""
    stellaris.kill()

@task
def resume(c: Context):
    """Launch Stellaris, and resume from latest save (click resume button)"""
    asyncio.run(stellaris.launch_resume())

@task
def re(c: Context):
    """Restart Stellaris and resume from latest save"""
    kill(c)
    resume(c)

@task
def zip(c: Context):
    """Zip mod folder contents"""
    shutil.make_archive(REPO_MOD_DIR, "zip", DEPLOYED_MOD_DIR)

@task
def stash(c: Context):
    """Overwrite mod folder with the contents of the deployed mod folder"""
    overwrite_folder(DEPLOYED_MOD_DIR, REPO_MOD_DIR)

@task 
def stashz(c: Context):
    """Stash & Zip"""
    stash(c);
    zip(c);

@task 
def deploy(c: Context):
    overwrite_folder(REPO_MOD_DIR, DEPLOYED_MOD_DIR)
