
import logging
import os
import subprocess
import sys

#if sys.version_info.major == 2:
#    if sys.version_info.minor == 6:
#        from utils_2_6.py import *
#    elif sys.version_info.minor == 7:
#        from utils_2_7.py import *

FORMAT = "%(module)s.%(funcName)s(%(lineno)s) => %(message)s (%(asctime)s)"
DATEFMT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=FORMAT, datefmt=DATEFMT, level=logging.DEBUG)


def load_env(configs):
    """Sources bash files and loads the resulting environment into os.environ

    @param configs is a list of file names that should be searched for.
    A string for a single configuration file is also accepted.
    """
    if type(configs) == str:
        load_env([configs])
    elif type(configs) == list:
        for config in configs:
            if os.path.exists(config):
                config_contents = subprocess.Popen(['bash', '-c', 'source ' + config + '; env'], stdout=subprocess.PIPE)
                for line in config_contents.stdout:
                    if type(line) == bytes:
                        (key, sep, value) = line.decode('utf-8').partition('=')
                    elif type(line) == str:
                        (key, sep, value) = line.partition('=')
                    else:
                        print('Not sure how to handle subprocess output. Contact Dan.')
                        break
                    os.environ[str(key)] = str(value).strip('\n')

                config_contents.communicate()
    else:
        print('You passed an invalid argument type to utils.load_env()')
        exit()

def append_to_file(file_name, lines):
    """Appends lines to a file

    @param file_name is the file to append to
    @param lines is the list of lines to append to the file
    """

    if type(lines) is not list:
        append_to_file(file_name,[lines])

    else:
        the_file = open(file_name,'a')
        for line in lines:
            the_file.write(line + '\n')

        the_file.close()
