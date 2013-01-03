# buildbot.py

A very simple buildbot.

# What it does

This buildbot is meant to be extremely customizable and simple.

Right now, it depends on GitHub, as it uses GitHub's POST hooks to trigger.
In the future, it might be expandable to other repository hosting services,
such as BitBucket.

To use the buildbot, clone this repo, then create directory for each repo that
you want the buildbot to build, in the `repos/` directory.

For example, for the repo `rails/rails` the directory should be
`repos/rails/rails/` and there should be a file,
`repos/rails/rails/build.sh`.

Inside of this directory, there create a file called `build.sh`. This file is
what buildbot.py will execute in order to build the project.

This bash script can do anything -- it can build projects and upload the output
to a download mirror using `rsync` or `scp`, it can run tests and do something
based on the exit code (`$?` in bash) -- literally anything bash can do.

# Some tips

* We usually run this in tmux (screen works too)
* If you're uploading results to a server, we recommend creating a limited user
  account on that server, with just enough access to deploy the new files, and
  creating a new, unique, passwordless SSH keyset for use in deploying. Guard
  this key by guarding who has access to the buildbot server.
  * You can put put this key in the same directory as buildbot.py and use it
    in all of your scripts, that way if you ever have to change it, you only
    have to change it in one place.
  * We .gitignore `buildsys_id_rsa` and `buildsys_id_rsa.pub` for this purpose.
* By default, this runs on Flask's default port of :5000. Make sure both
  iptables and your router's firewall (if applicable) allow access to this port.
* If uploading results to somewhere, we recommend piping your build's output to
  a file, and uploading this output as well, for debugging later on.
* Also if uploading, you can get fancy with symlinks and create something that
  always points to the latest build. This means you can give out a single link
  that always contains the latest build.

# Installing

There are very few deps required to make this work - notably, Flask.

Install Flask and run the buildbot with `python buildbot.py` inside of tmux or
screen.

# License

3-BSD.

```
Copyright (c) 2013, Edge System Design, LLC.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
