

import os
import pprint

PATH = os.environ['PATH']
PATH_list = PATH.split(';')
pprint.pprint(PATH_list)
