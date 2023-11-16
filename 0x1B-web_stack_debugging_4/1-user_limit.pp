# Modifying open files limits
exec { 'Fix file limit':
  command => '/usr/bin/env sed -i "s/4/4000/; s/5/4000/" /etc/security/limits.conf'
}
