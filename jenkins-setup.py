#!python

import sys
import subprocess
import glob
if(sys.platform == 'win32'):
  #commands
  set_env_cmd = ['set', 'OPENERP_DLLS=C:\\jenkins\\openerp\\&&', 'set', 'GTK_RUNTIME=C:\\Python26\\Lib\\site-packages\\gtk-2.0\\runtime\\&&']
  build_cmd = ['python', 'setup.py', 'py2exe']
  make_installer_cmd = ['C:\\Program Files\\NSIS\\makensis.exe', 'setup.nsi']
  #build
  code = subprocess.call((set_env_cmd + build_cmd), shell=True)
  #create installer
  code = subprocess.call(make_installer_cmd, shell=True) if not code else code
elif(sys.platform == 'linux2'):
  #presuming a debian install for the time being...
  subprocess.call(['git', 'clean', '-f'])
  code = subprocess.call(['dpkg-buildpackage', '-nc'])
  debs = glob.glob('../openerp-client*.deb')
  if debs:
    code = subprocess.call(['mv'] + debs + ['.'])
  else:
    code = 0
exit(code)
