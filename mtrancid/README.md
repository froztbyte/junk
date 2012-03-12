Mikrotik Rancid Things
======================

Hey, look at this. It's a Thing. With Stuff!!

This repo contains the parts you need to enable rancid to deal with Mikrotik routers, both the x86 and arm flavours.

What's important here
---------------------

*  mtlogin - the mikrotik equivalent of clogin. used to do the actual login to the router
*  mtrancid_x86 - contains the relevant command sequence bits relevant to x86 routers
*  mtrancid_rb - contains the relevant command sequence bits relevant to routerboard routers
*  rancid-fe - standard rancid-fe file, just with the mikrotik device type mappings added in
*  router.db - sample router.db file
*  ssh.config - sample ssh config
*  clogin.rc - example login config file

Notes
-----

One modification added to force TERM to 'xterm', but I'm still doubtful as to whether it actually helps with the [timeout issue](http://forum.mikrotik.com/viewtopic.php?f=2&t=51312)

Acknowledgements
----------------

The original code is all from [the Rancid list](http://www.gossamer-threads.com/lists/rancid/users/3826), this is just split up so that I can refer to it online in non-crappy format.

