#!/usr/bin/env python

#Copyright 2013 Mitchell Jon Stanton-Cook Licensed under the
#Educational Community License, Version 2.0 (the "License"); you may
#not use this file except in compliance with the License. You may
#obtain a copy of the License at
#
#    http://www.osedu.org/licenses/ECL-2.0
#
##Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an "AS IS"
#BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#or implied. See the License for the specific language governing 
#permissions and limitations under the License. 

"""
Fetch Beta-Lactamase sequences from the NCBI
"""

import os
import sys 
import traceback
import argparse
import time
import __init__ as meta

import fetcher

epi     = "Licence: %s by %s <%s>" % (meta.__licence__, meta.__author__, 
                                      meta.__author_email__)
prog    = meta.__name__.replace(' ', '_')
__doc__ = " %s v%s - %s" % (prog, meta.__version__, meta.__description__)


def core(args):
    """
    """
    csv = os.path.expanduser(args.csv_file)
    fetcher.fetch(csv)


if __name__ == '__main__':
    try:
        start_time = time.time()
        desc = __doc__.strip()
        parser = argparse.ArgumentParser(description=desc,epilog=epi)
        parser.add_argument('-v', '--verbose', action='store_true',
                                default=False, help='verbose output')
        parser.add_argument('--version', action='version',
                                version='%(prog)s ' + meta.__version__)
        parser.add_argument('csv_file', action='store',
                                type=str, help='Full path to the input csv')
        parser.set_defaults(func=core)
        args = parser.parse_args()
        args.func(args)
        if args.verbose: print "Executing @ " + time.asctime()
        if args.verbose: print "Ended @ " + time.asctime()
        if args.verbose: print 'total time in minutes:',
        if args.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
