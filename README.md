# pyEdge

pyEdge is an open source Python library to control the OWI-535 Robotic Arm Edge via USB.

It consists of two parts, a native serial writer written in C which will need to be compiled, and the Python library itself. 

Make sure `gcc`, `pkg-config`, and `libusb` are installed (if you are on Mac OS X, then install Xcode's command line tools from Apple's website, then install Homebrew, and run `brew install pkg-config libusb`).

Now it's time to build the serial writer. Run: ``gcc -lusb-1.0 source.c -o source``.

You will end up with a binary named `source`, this will help write serial commands natively to the edge via USB. Simply include `pyEdge.py` via import, ensure the compiled `source` is always in the same directory as `pyEdge.py`, and start hacking away. Open up `pyEdge.py` to see a list of functions available. 

We got the C serial writer code and protocol here. This is a great resource: http://notbrainsurgery.livejournal.com/38622.html?page=1
