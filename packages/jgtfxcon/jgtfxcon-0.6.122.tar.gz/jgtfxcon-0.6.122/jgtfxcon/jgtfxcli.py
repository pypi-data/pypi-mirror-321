#!/usr/bin/env python

TEST_MODE = False
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from jgtutils import jgtconstants as constants

# import jgtfxcommon as jgtcommon
from jgtutils import jgtos, jgtcommon, jgtpov
from jgtutils.jgtcliconstants import PDSCLI_PROG_NAME
#from jgtutils import jlog

import argparse
import subprocess

import JGTPDS as pds,JGTPDSSvc as svc

import pandas as pd
verbose_level=0
parser:argparse.ArgumentParser=None
def _parse_args(enable_specified_settings=False):
    global parser
    parser=jgtcommon.new_parser("JGT PDS CLI","It saves its data in JGTPY_DATA/pds folder, if --full JGTPY_DATA_FULL/pds",PDSCLI_PROG_NAME,enable_specified_settings=enable_specified_settings,add_exiting_quietly_flag=True)

    # jgtfxcommon.add_main_arguments(parser)
    jgtcommon.add_instrument_timeframe_arguments(parser)
    # jgtfxcommon.add_date_arguments(parser)
    jgtcommon.add_tlid_range_argument(parser)
    #jgtcommon.add_max_bars_arguments(parser)
    jgtcommon.add_viewpath_argument(parser)
    jgtcommon.add_exit_if_error(parser)
    # jgtfxcommon.add_output_argument(parser)
    jgtcommon.add_compressed_argument(parser)
    #jgtcommon.add_use_full_argument(parser)
    jgtcommon.add_bars_amount_V2_arguments(parser)

    # jgtfxcommon.add_quiet_argument(parser)
    jgtcommon.add_verbose_argument(parser)
    jgtcommon.add_debug_argument(parser)
    # jgtfxcommon.add_cds_argument(parser)
    jgtcommon.add_iprop_init_argument(parser)
    jgtcommon.add_pdsserver_argument(parser)
    jgtcommon.add_keepbidask_argument(parser)
    
    #dropna_volume
    jgtcommon.add_dropna_volume_argument(parser)

    jgtcommon.add_jgtclirqdata_arguments(parser)
    jgtcommon.add_load_json_file_argument(parser)

    args=jgtcommon.parse_args(parser)
    # args = parser.parse_args()
    return args


def run(enable_specified_settings=True):
    global verbose_level
    args = _parse_args(enable_specified_settings)
    #if no arguments, print help
    if len(sys.argv) == 1 and (not args.instrument and not args.timeframe):
        subprocess.run([sys.argv[0], "--help"])
        return
    
    exit_on_error = False
    if args.exitonerror: #@STCIssue DEPRECATING
        exit_on_error = True

    instrument = args.instrument
    timeframe = args.timeframe
    use_full = False
    if args.full:
        use_full = True
    
    using_tlid = False
    tlid_range = None
    viewpath = args.viewpath
    #if viewpath:
        #print("Viewpath is on")

    if args.tlidrange is not None:
        using_tlid = True
        tlid_range = args.tlidrange

    # Do we have keep_bid_ask set to true?
    #config = jgtcommon.readconfig()
    
    keep_bid_ask = args.keepbidask
    # config_has_keep_bid_ask = False
    # if 'keep_bid_ask' in config and (config['keep_bid_ask'] == True or config['keep_bid_ask'] == "1" or config['keep_bid_ask'] == "true"):
    #     config_has_keep_bid_ask = True
    # #env variable bypass if env exist JGT_KEEP_BID_ASK=1, keep_bid_ask = True
    # if os.getenv("JGT_KEEP_BID_ASK","0") == "1" or config_has_keep_bid_ask:
    #     #print("KEEP BID ASK ENV VAR ON (bypassing the --keepbidask argument)")
    #     keep_bid_ask = True
        
    quotescount = args.quotescount if not use_full and tlid_range is None else -1

    # print(args.quotescount)
    debug = args.debug
    if args.server == True:
        try:
            from . import pdsserver as svr
            print("#@STCIssue DEPRECATING  Starting server - REQUIRES Upgrade and rethingking as it might be migrated to jgtpy")
            svr.app.run(debug=debug)
        except:
            print("Error starting server")
            return
    if args.iprop == True: 
        try:
            from . import dl_properties

            print("--------------- #@STCIssue DEPRECATING-----------------------------------")
            print("------Iprop should be downloaded in $HOME/.jgt---")
            return  # we quit
        except:
            print("---BAHHHHHHHHHH Iprop trouble downloading-----")
            return

    compressed = False
    verbose_level = args.verbose
    quiet = False
    with_index = False
    start_date = None
    end_date = None
    
 
    if verbose_level < 2 :  # verbose 2 is not quiet
        quiet = True
    
    # if not quiet and verbose_level == 0:
    #     verbose_level=2  # Default to verbose 2 if not quiet
    # if (verbose_level == 0 or verbose_level == 1) and not quiet:  # verbose 2 is not quiet
    #     quiet = True

    do_we_dropna_volume = args.dropna_volume
    if do_we_dropna_volume and not quiet:
        print("INFO(jgtfxcli)::Dropping NA Volume")

    if args.compress:
        compressed = args.compress

    try:

        updated_povs:list=svc.getPHs(instrument=instrument,timeframe=timeframe,quote_count=quotescount,start=start_date,end=end_date,with_index=with_index,quiet=quiet,compressed=compressed,tlid_range=tlid_range,use_full=use_full,verbose_level=verbose_level,view_output_path_only=viewpath,keep_bid_ask=keep_bid_ask,dropna_volume=do_we_dropna_volume)
        
        for i in updated_povs:
            vprint(i,1)
        
            
    except Exception as e:
        #jlog.error("Error in main ",e)
        jgtcommon.print_exception(e)

    # try:
    #     pds.disconnect()
    # except Exception as e:
    #     jgtcommon.print_exception(e)


def main():
    run(enable_specified_settings=True)

def print_quiet(quiet, content):
    if not quiet:
        print(content)

def vprint(content,level=1):
    global verbose_level
    if level <= verbose_level:
        print(content)

if __name__ == "__main__":
    main()
