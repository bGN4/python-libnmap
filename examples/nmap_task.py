#!/usr/bin/env python

from libnmap.process import NmapProcess
from time import sleep

def mycallback(nmaptask):
    nmaptask = nmap_proc.current_task
    if nmaptask:
        print "Task {0} ({1}): ETC: {2} DONE: {3}%".format(nmaptask.name,
                                                           nmaptask.status,
                                                           nmaptask.etc,
                                                           nmaptask.progress)

nmap_proc = NmapProcess(targets="scanme.nmap.org",
                        options="-sV",
                        event_callback=mycallback)
nmap_proc.run()
print nmap_proc.stdout
print nmap_proc.stderr
