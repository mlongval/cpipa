cpipa
=====

This is the README file for CPIPA

CPIPA stands for  C urrent 
                  P ublic 
                  IP 
                  A ddress

The program is "scratch-the-itch-ware", and is released under the GPL v2.

It came out of my need to get back to my home server, when the server is behind a dynamic IP address.

Here is how I thought I would use it:

Consider 2 computers:  The SERVER (my home computer that I want to get into via SSH) and the REMOTE computer
(the laptop that I am using at work, or somewhere else....)

Have the SERVER check it's external Public IP address every 30 minutes, and write that IP address
to a file on my Dropbox account.  Let's call the file:  "server_ip_address.txt"

If the SERVER is updating that file every 30 mins, then to get into the server from my REMOTE computer, all 
I have to do is check the "server_ip_address.txt" file which is now in the Dropbox folder on my REMOTE computer,
via the magic of Dropbox.  I can then SSH into the SERVER using that info.

Thats essentially it....

I know I could simply get a domain name from a place like no-ip.com but I am too cheap to pay.... 

Mike
mlongval _at_ gmail _dot_ com
