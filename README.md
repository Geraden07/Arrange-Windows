#README
###Author: Steven B.
###September 2014

I own three monitors and commonly leave iTunes, CPU-Z, CPUID Hardware Monitor, Mumble (with it's Connect window open) and the Windows Resource Monitor open on my left screen. I got tired of constantly reopening and arranging all these windows into their normal positions so I wrote this script to do it for me.

The script begins by looking through the open processes list to see if the programs in question are running. If they aren't it will start any that are missing. Then if it needed to start one of the programs, it will wait for 10 seconds for the program to launch and load, then it will do the rearrangement. If it did not launch any programs (they are all already running) then the script skips the waiting and does the rearrangement immedietly.

I fought with Window's UAC for a little bit becuase although normally HWM, CPUZ, and Resource Monitor all require Admin rights to run, launching the script from an elevated command prompt was no issue for these programs. Counter-intuitively Mumble was having issue being started if it wasn't already running, claiming it needed elevated priviledge.

To avoid this, I created a shortcut that launches a copy of the Python.exe set to run as admin with the script passed as an argument. This seemed to solve all issues and the script has the priviledge to launch all of the processes in question if necessary as well as to move the windows to their proper places.
