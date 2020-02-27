from setuptools import setup

setup(name='WARP+ to WireGuard',
      version='0.1',
      description='A simple cli to get WARP+ as WireGuard configuration',
      url='https://git.arian.lol/warp-plus/python',
      author='Arian Amiramjadi',
      author_email='me@arian.lol',
      packages=['warpy'],
      install_requires=['pynacl'],
      scripts = ['scripts/warpy'])