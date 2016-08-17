"""
Contains methods for manipulating txt files and sourcing bash scripts.

:author: Daniel Abercrombie <dabercro@mit.edu>
"""

import os
import subprocess


def load_env(configs):
    """Sources bash files and loads the resulting environment into os.environ

    :param configs: is a list of file names that should be sourced.
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
                print('Info: ' + config + ' does not exist.')
    else:
        print('You passed an invalid argument type to utils.load_env()')
        exit()


def append_to_file(file_name, lines):
    """Appends lines to a file.
    This function may be useful for the exceedingly lazy.

    :param file_name: is the file to append to
    :param lines: is the list of lines or a single line to append to the file
    """

    if type(lines) is not list:
        append_to_file(file_name, [lines])

    else:
        with open(file_name, 'a') as the_file:
            for line in lines:
                the_file.write(line + '\n')
