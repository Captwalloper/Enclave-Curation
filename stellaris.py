import subprocess, asyncio, time
from typing import Callable
import pywinauto
import psutil

def launch():
  """Launch Stellaris"""
  subprocess.run(['steam', 'steam://rungameid/281990'])

def kill():
  """Kill Stellaris"""
  [p.kill() for p in psutil.process_iter() if p.name() in ["stellaris.exe", "Paradox Launcher.exe"]]

async def launch_resume():
  launch()
  launcher: pywinauto.application.controls.uiawrapper.UIAWrapper = None
  def find_launcher():
    nonlocal launcher
    desktop = pywinauto.Desktop(backend="uia")
    windows = desktop.windows(visible_only=True)
    launcher = next((x for x in windows if "'Stellaris', Dialog" in str(x)), None)
    return launcher != None
  if not await _succeed_before_timeout(find_launcher, 10):
    print('Failed to detect Stellaris Launcher')
    return
  resume_button: pywinauto.application.controls.uiawrapper.UIAWrapper = None
  def find_resume_button():
    nonlocal resume_button
    resume_button = next((x for x in launcher.descendants() if "'RESUME', Button" in str(x)), None)
    return resume_button != None
  if not await _succeed_before_timeout(find_resume_button, 5):
    print('Failed to find Resume button')
    return
  def click_resume_button():
    resume_button.set_focus()
    resume_button.click_input()
    return not resume_button.is_active()
  if not await _succeed_before_timeout(click_resume_button, 10):
    print("Resume button wasn't clickable... WAT")
    return

async def _succeed_before_timeout(condition: Callable[[], bool], timeout: int = 10) -> bool:
  """Wait for a condition to be met, or timeout succeeded. Return whether condition is satisfied before timeout."""
  start_time = time.time()
  while time.time() - start_time < timeout:
    if condition():
      return True
    await asyncio.sleep(0.1)
  return False
