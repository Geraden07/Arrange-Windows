#Author Steven B.
#The following code is liscensed under GPL v3
#https://www.gnu.org/licenses/gpl-3.0.html
import subprocess
import win32gui
import sys
import os
import time

# New Layout
#                Window name                 Window placement           Process name        Launch command
windowInfo = [  ( 'CPU-Z ',                 ( -436, 638,  -29, 1043),   'cpuz.exe',         "C:/Program Files/CPUID/CPU-Z/cpuz.exe"),
                ( 'iTunes',                 (-1920,   0, -960, 1040),   'iTunes.exe',       "C:/Program Files/iTunes/iTunes.exe"),
                ( 'Resource Monitor',       ( -441,  -1, -207,  645),   'perfmon.exe',      "C:/Windows/system32/perfmon.exe /res"),
                ( 'CPUID HWMonitor',        ( -967,  -1, -427, 1048),   'HWMonitor.exe',    "C:/Program Files/CPUID/HWMonitor/HWMonitor.exe")#,
                #( 'Mumble -- 1.2.8',        ( -520, 708,  -22, 1074),   'mumble.exe',       "C:/Program Files (x86)/Mumble/mumble.exe"),
                #( 'Mumble Server Connect',  ( -520, 738,  -22, 1074),   '',                 "")
            ]

# Classic Layout
#                Window name                 Window placement           Process name        Launch command
#windowInfo = [  ( 'CPU-Z ',                 ( -962, 633, -555, 1043),   'cpuz.exe',         "C:/Program Files/CPUID/CPU-Z/cpuz.exe"),
                #( 'iTunes',                 (-1920,   0, -960, 1040),   'iTunes.exe',       "C:/Program Files/iTunes/iTunes.exe"),
                #( 'Resource Monitor',       ( -441,  -1, -207,  700),   'perfmon.exe',      "C:/Windows/system32/perfmon.exe /res"),
                #( 'CPUID HWMonitor',        ( -967,  -1, -427,  641),   'HWMonitor.exe',    "C:/Program Files/CPUID/HWMonitor/HWMonitor.exe")#,
                #( 'Mumble -- 1.2.8',        ( -520, 708,  -22, 1074),   'mumble.exe',       "C:/Program Files (x86)/Mumble/mumble.exe"),
                #( 'Mumble Server Connect',  ( -520, 738,  -22, 1074),   '',                 "")
            #]



def checkIfRunning():
    """Function that checks if the processes are running and if they aren't
    it starts them
    Returns 10 if it started a process and 0 if no process needed starting"""
    #processList = subprocess.check_output(['tasklist', '/fo', 'csv']).split('\n')
    processList = subprocess.check_output(['tasklist', '/fo', 'csv']).decode("utf-8").split('\r\n')
    processesFound = []
    sleepValue = 0

    #Loop through processes
    for x in processList:
        x = x.replace('"', '').split(',')
        #x = x.replace(b'"', b'').split(b',')

        #Loop through and test if they are in our WindowInfo list
        for y in windowInfo:
            if (x[0] == y[2] and x[0] != ''):
                processesFound.append(y[2])

    #Loop through our windowInfo and start processes not in the processesFound
    for x in windowInfo:
        if not x[2] in processesFound and x[2] != '':
            #print "Starting %s" % (x[2],)
            print("Starting {}".format(x[2]))
            try:
                subprocess.Popen(x[3])
                sleepValue = 5
            #except Exception, e:
            except Exception as e:
                #print "Could not start %s" % (x[3],)
                #print e
                print("Could not start {}".format(x[3]))
                print(e)
    #print "Running check complete"
    print("Running check complete")
    return sleepValue


def relocate(hwnd, locTuple):
    """Function that takes a window's handle hwnd and a location tuple and
    moves the window to that location"""

    windowName = win32gui.GetWindowText(hwnd)
    #print ("Relocating %s..." % (windowName,)),
    print("Relocating {}...".format(windowName))

    newWindowPlacement = win32gui.GetWindowPlacement(hwnd)
    workList = list(newWindowPlacement)
    workList[4] = locTuple
    newWindowPlacement = tuple(workList)

    try:
        win32gui.SetWindowPlacement(hwnd, newWindowPlacement)
        #print "Success!"
        print("Success!")
    except:
        #print "Lack priviledge to move %s" % (windowName,)
        print("Lack priviledge to move {}".format(windowName))


def callback(hwnd, extra):
    """A callback function that is called for each window the win32gui
    encounters in it's EnumWindow call"""
    #Ignore handles that aren't visible
    if win32gui.IsWindowVisible(hwnd) != 1:
        return

    print(win32gui.GetWindowText(hwnd))

    #Loop through windowInfo and relocate if hwnd's text matches
    for x in windowInfo:
        if win32gui.GetWindowText(hwnd) == x[0]:
            relocate(hwnd, x[1])


def main():
    #print "Checking that all programs are running..."
    print("Checking that all programs are running...")
    sleepValue = checkIfRunning()
    if sleepValue == 10:
        #print "Waiting for processes to finish their startups..."
        print("Waiting for processes to finish their startups...")
    for x in range(sleepValue):
        #print x
        print(x)
        time.sleep(1)
    #print "Relocating windows..."
    print("Relocating windows...")
    win32gui.EnumWindows(callback, None)
    #print "Done"
    print("Done")
    #raw_input()
    #input()


if __name__ == '__main__':
    main()
