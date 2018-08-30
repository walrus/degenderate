""" Command line script to run the de-gendering process"""

import argparse
import pythem

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='De-gender a string')
    parser.add_argument('input_string')

    args = parser.parse_args()
    print(pythem.replace_pronouns(args.input_string))
