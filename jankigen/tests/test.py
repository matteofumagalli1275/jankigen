import unittest
import os
from jankigen import cli_utils


class MyTest(unittest.TestCase):
    def test(self):
        dirname = os.path.dirname(__file__)
        mydir = os.path.join(dirname, 'res-test')

        cli = cli_utils.CliUtils(mydir,
                                 user_dict=os.path.join(dirname, "res-test/custom_dic.csv"),
                                 user_dict_en=os.path.join(dirname, "res-test/custom_dic_en.csv"))

        cli.run()