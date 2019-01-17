#!/usr/bin/python
# Copyright: 2005 Brian Harring (ferringb@gentoo.org)
# License: GPL2
# $Header: /home/cvsrep/confcache/setup.py,v 1.14 2005/11/22 02:36:09 bharring Exp $

from distutils.core import setup
from distutils.command.install import install
from distutils.command.sdist import sdist

import os

# cough, hack
class myinstall(install):
	def run(self):
		os.umask(0)
		os.chmod("redirect.sh", 0755)
		install.run(self)

class mysdist(sdist):
	default_format = dict(sdist.default_format)
	default_format["posix"] = "bztar"
	def run(self):
		print "regenning ChangeLog"
		os.system("bzr log > ChangeLog")
		sdist.run(self)
		

versions = [x.strip() for x in open("version", "r") if not x.strip().startswith("#") and x.strip()]

if len(versions) != 1:
	import sys
	print "too many versions found in 'versions' file:"
	print "\t",
	print "\n\t".join(versions)
	sys.exit(1)

version = versions[0]
if version.startswith("confcache"):
	version = version[len("confcache"):].strip("-").strip()

setup(
	name="confcache",
	version=version,
	license="GPL",
	author="Brian Harring",
	author_email="ferringb@gmail.com",
	description="global autoconf configure caching utility",
	scripts=["confcache"],
	cmdclass={"install":myinstall, "sdist":mysdist},
	data_files=[["/usr/share/confcache", ["redirect.sh"]], ["/usr/share/doc/confcache", ["COPYING", "README", "ChangeLog"]]]
)
