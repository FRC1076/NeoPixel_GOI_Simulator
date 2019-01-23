import unittest

import NeoDisplay as nd
 
class NeoDisplayTest(unittest.TestCase):
    def test_just_0(self):
        display = nd.NeoDisplay(8*8, width=8, height=8)
        display.set_pixels([0])
        renderlines = display.render().split('\n')
        # skip line 0, just look for the 'x' in line 1,
        # which I think is at character 2 on line 1.
        paydirt = renderlines[1][2]
        self.assertEqual(paydirt,'x')

if __name__ == '__main__':
    unittest.main()
