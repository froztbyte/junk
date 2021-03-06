Mikrotik Rancid Things
======================

Hey, look at this. It's a Thing. With Stuff!!

This repo contains the parts you need to enable rancid to deal with Mikrotik routers, both the x86 and arm flavours.

Note: this isn't necessary anymore as of 2.3.8 (and perhaps an earlier version). The necessary information seems to have been merged into rancid upstream, and the device type is 'mikrotik'.

What's important here
---------------------

*  mtlogin - the mikrotik equivalent of clogin. used to do the actual login to the router (goes in /path/to/rancid/bin/)
*  mtrancid_x86 - contains the relevant command sequence bits relevant to x86 routers (goes in /path/to/rancid/bin/)
*  mtrancid_rb - contains the relevant command sequence bits relevant to routerboard routers (goes in /path/to/rancid/bin/)
*  rancid-fe - standard rancid-fe file, just with the mikrotik device type mappings added in (goes in /path/to/rancid/bin/)
*  router.db - sample router.db file
*  ssh.config - sample ssh config
*  clogin.rc - example login config file

Notes
-----

*  One modification added to force TERM to 'xterm', but I'm still doubtful as to whether it actually helps with the [timeout issue](http://forum.mikrotik.com/viewtopic.php?f=2&t=51312)

*  This entire repo is of course to be used with [Rancid](http://shrubbery.net/rancid/)

*  Setup information is not covered in here as the Rancid docs do that

Acknowledgements
----------------

The original code is all from [the Rancid list](http://www.gossamer-threads.com/lists/rancid/users/3826), this is just split up so that I can refer to it online in non-crappy format.

