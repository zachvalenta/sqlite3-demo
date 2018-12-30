import subprocess
import unittest
from unittest.mock import patch
from io import StringIO


class TestSUT(unittest.TestCase):

# https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on
# https://stackoverflow.com/questions/18739239/python-how-to-get-stdout-after-running-os-system

    def test_to_stdout(self):
        expected = 'alice\n'
        # expected = 'hai'
        # expected = "[('Origins of Political Order', 10, '0374533229'), " \
        #            "('Political Order and Political Decay', 10, '0374533229')]"
        # capture all stdout
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            # send text to stdout
            # print('hai', end='')
            # os.system('python3 sl.py')
            # text sent = what you expected

            subprocess.check_output('python3 sl.py', shell=True)

            # conn = sqlite3.connect('test.db')
            # c = conn.cursor()
            # c.execute("""SELECT * FROM book""")
            # print(c.fetchall())
            # conn.close()

            self.assertEqual(fake_stdout.getvalue(), expected)
