"""Command-line tool to empty the ponyexpress qeueue

Usage::

		$ python -m ponyexpress.queue

"""

import sys
from . import manage

if __name__ == '__main__':
	outfile = sys.stdout
	outfile.write(manage.queue())
