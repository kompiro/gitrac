GiTrac
======

Distributed and integrated ticket system like git commands.

usage
-----

gitrac [command] [options]

commands:

- init (URL)
  
  Initialized repository and set some configs.
  If you want to push and pull commands, 
  please add URL and install TracXMLRPC Plugin to your Trac site.
  
  URL's format is followed.
  http://[USERNAME]:[PASSWORD]@[PROJECT_URL]/login/xmlrpc
  Example:
    http://kompiro:test@localhost/test/login/xmlrpc

  WARNING:
    Currently, This command supports only Basic Authentication.

- add [summary]
  
  added titled summary's ticket to local repository.

- rm [id](NOT IMPREMENTED)

  removed local's ticket.
  if you choosed remote's ticket, gitrac returns error.

- list
  
  listed local repository's tickets

- push
 
  pushed tickets to remote repository.
  current supports only defect.

- pull(NOT IMPREMENTED)

  pulled tickets from remote repository.

License
-------

EPL License

##### author #####
written by Hiroki Kondo(aka kompiro)

