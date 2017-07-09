# kernel-upgrade

To upgrade to the latest kernel of ubuntu and derivatives
In my case Linux mint 

Fetch the latest kernel from http://kernel.ubuntu.com/~kernel-ppa/mainline/

Similar works exist 

1. ukuu  -- https://github.com/linux-dntt1/ukuu (my fork)  --  vala and shell
2. Linux Kernel Utilities   https://github.com/linux-dntt1/linux-kernel-utilities (my fork) -- shell 
3. Linux mint - mintupdate - https://github.com/linux-dntt1/mintupdate (my fork)- python 







Added 1.py as a test mechnism 
based on https://github.com/linux-dntt1/mintupdate/blob/master/usr/lib/linuxmint/mintUpdate/checkKernels.py




Progress

-> Idea into reality started
-->  Coding in python
---> apt plugin added
----> customizing  apt to list all  available kernel


Todo/Partially done

: Directly use ubuntu kernel source
: Parse the ubuntu kernel source 
: Download data based on parsed file
: Install only the relevant kernel 


Issue

: As apt list only safe kernels and not the latest kernel so need an alternative way to list that

example : run --> python 1.py

output will start as : 4.10.x  and not as 4.12 which is the latest


