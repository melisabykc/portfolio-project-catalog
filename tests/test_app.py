import tempfile, unittest
from pathlib import Path
import app
class Tests(unittest.TestCase):
 def test_add(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'test.db'; self.assertEqual(app.add('Demo','Python','', 'planned',p),1)
if __name__=='__main__': unittest.main()
