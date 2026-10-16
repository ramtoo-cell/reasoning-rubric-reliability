import copy
import json
import unittest
from pathlib import Path
from engine import analyze
EXAMPLE=json.loads(Path(__file__).with_name("example.json").read_text())

class Tests(unittest.TestCase):
    def test_agreement(self):
        r=analyze({'labels':['no','yes'],'rows':[{'a':'no','b':'no'},{'a':'yes','b':'yes'}]})
        self.assertEqual(r['cohen_kappa'],1)
        self.assertEqual(r['quadratic_weighted_kappa'],1)
    def test_opposite(self):
        r=analyze({'labels':['no','yes'],'rows':[{'a':'no','b':'yes'},{'a':'yes','b':'no'}]})
        self.assertEqual(r['cohen_kappa'],-1)
    def test_degenerate(self):
        self.assertIsNone(analyze({'labels':['no','yes'],'rows':[{'a':'yes','b':'yes'}]})['cohen_kappa'])
    def test_unknown(self):
        with self.assertRaises(ValueError): analyze({'labels':['no','yes'],'rows':[{'a':'maybe','b':'yes'}]})

if __name__=="__main__": unittest.main()
