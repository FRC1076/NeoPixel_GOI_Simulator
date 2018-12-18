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
