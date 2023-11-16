# Modifying Nginx request limits
exec { 'Request Limit':
  command     => '/usr/bin/env sed -i s/15/4000/ /etc/default/nginx',
}

exec { 'Restart Nginx':
  command     => '/usr/bin/env service nginx restart',
}
