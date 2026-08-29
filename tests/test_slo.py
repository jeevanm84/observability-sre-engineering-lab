import copy, unittest
from pathlib import Path
from sre.model import SREError,evaluate,read_json
ROOT=Path(__file__).resolve().parents[1]
class SLOTests(unittest.TestCase):
    def load(self,name): return read_json(ROOT/f"scenarios/{name}.json")
    def test_healthy(self): self.assertEqual(evaluate(self.load("healthy"))["decision"],"no-page")
    def test_fast(self): self.assertEqual(evaluate(self.load("fast-burn"))["decision"],"critical-page")
    def test_slow(self): self.assertEqual(evaluate(self.load("slow-burn"))["decision"],"ticket")
    def test_empty_traffic_fails(self):
        value=copy.deepcopy(self.load("healthy")); value["windows"][0]["valid_events"]=0
        with self.assertRaises(SREError): evaluate(value)
if __name__=="__main__": unittest.main()

