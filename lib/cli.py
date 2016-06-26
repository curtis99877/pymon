import sys
import argparse
import textwrap

def parse_cli():
    parser = argparse.ArgumentParser(sys.argv[0],
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent('''\
                    %s
                    --------------------------------
                    Created by Curtis Li
                    ''' % get_version()))

    parser.add_argument("-v", "--version", 
            action="version", 
            version=get_version())
    parser.add_argument("-r", "-R", "--recursive", 
            action="store_true",
            help="recursively monitor directories (Default)")
    parser.add_argument("--no-recursive",
            action="store_false",
            help="do not recursively monitor directories")
    parser.add_argument("--exec",
            action="store",
            metavar="PROG",
            default="python",
            help="program to execute application (Default: python)")
    parser.add_argument("--match",
            action="append",
            metavar="REGEX",
            help="regex to match monitored files (Default: .py)")
    parser.add_argument("--ignore",
            action="append",
            metavar="REGEX",
            help="regex to filter monitored files (Default: .pyc)")
    parser.add_argument("args", 
            nargs=argparse.REMAINDER)

    args = parser.parse_args()
    
    cli = dict()

    cli["execp"] = "python"
    cli["app_args"] = ' '.join(sys.argv[1:])
    cli["path"] = '.'
    cli["regexes"] = ['.*[.]py']
    cli["ignores"] = ['.*[.]pyc']
    
    return cli 

def get_version():
    return "%s %s" % ("Pymon", "0.1")
