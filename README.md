# NeoPixel_GOI_Simulator
Software simulator of NeoPixel display displaying Graphics Over Internet

This tool listens for GOI packets containing NeoPixel drawing directives.
And it displays them in a terminal window.   First version support mono-chrome
display with lights on '*' or off ' '.

Using a few VT100 escape sequences, we can do the screen refresh without too
much mess.     We could enhance with single character updates (using VT100
goto X,Y techniques), but first version will redraw the display.

If the clear:1 directive is received, the screen is cleared before any of the drawing
is done.

If you want to work on this project, you should know that is has a nested library in
it (from a different repository).   You can checkout the entire thing with:

          git clone https://github.com/FRC1076/NeoPixel_GOI_Simulator.git --recurse
          
If you leave the lib1076 folder alone (don't make changes to it in this context), things should
work okay.

