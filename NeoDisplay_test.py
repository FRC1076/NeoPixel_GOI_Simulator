import unittest

import NeoDisplay as nd
 
class NeoDisplayTest(unittest.TestCase):
    def test_0_then_1_still_0(self):
        """
        Set pixel 0 and check render for an x in the right place
        """
        display = nd.NeoDisplay(8*8, width=8, height=8)
        display.set_pixels([0])
        renderlines = display.render().split('\n')
        # skip line 0, just look for the 'x' in line 1,
        # which I think is at character 2 on line 1.
        paydirt = renderlines[1][2]
        self.assertEqual(paydirt,'x', 'setting pixel 0 failed to render')

        display.set_pixels([1])
        renderlines = display.render().split('\n')
        paydirt = renderlines[2][2]
        self.assertEqual(paydirt,'x', 'setting pixel 1 failed to render'+str(renderlines))
        """
        check for damage
        """
        self.assertEqual(renderlines[1][2],'x', 'setting pixel 1 messed up pixel 0 render'+str(renderlines))       

    
if __name__ == '__main__':
    unittest.main()
