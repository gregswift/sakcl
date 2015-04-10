sakcl
=====

SSH AuthorizedKeysCommand Lookup tool

Background
----------

Recent versions of OpenSSH's server support running a command to look up a users authorized_keys file.  This script is intended to be used for that purpose.  Its a verys simple wrapper that allows you to host the authorized_keys file on a web server named after the user.  However, this can offer some interesting flexibility.

Config Parameters
-----------------
The only required parameter in sakcl.conf is *url_template*.  This is a string that will be formatted by python. All association for formatting is name based.  {user} is required somewhere in the url, and will be passed to the script as the first argument when calling the command.

Additional variables for the url_template can be added to the config file and they will be passed into the formatting of the url like this: url.format(**config)

See http://docs.python.org/2/library/string.html#format-examples

Example Configurations
----------------------

If everyone created a repository called 'ssh_config' in their github account that had a file named authorized_keys, the following configuration would return their keys.

    url_template=https://github.com/{user}/ssh_config/raw/master/authorized_keys

For a team you may create a repository in their org called 'ssh_authorized_keys' that has a branch for each tier of their internal environments like this:

    url_template=https://github.com/myteam/ssh_authorized_keys/raw/{branch}/{user}
    branch=staging

Example Usage
-------------
    # sakcl gregswift
    ssh-rsa A5AGSD6ASD65DF56SD6F56SDAF556ASD4F56ASD4F564ASDF4ASD5F46A5S4DF56ASD4F653G3L3L3LL3L3L== gregswift

Installation
------------

This is a work in progress.  Even though its python script i should probably drop the setup.py. For now:

1. cp sakcl /usr/sbin/
2. chmod 755 /usr/sbin/sakcl
3. cp sakcl.conf /etc/
4. Configure /etc/sakcl.conf
5. Set 'AuthorizedKeysCommand /usr/sbin/sakcl' in /etc/ssh/sshd_config
6. Restart sshd
