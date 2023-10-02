# Config for installing and setting up nginx server using puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
  before  => Package['nginx'], # Ensure update happens before installing nginx
}

package { 'nginx':
  ensure => 'installed',
}

# Step 3: Modify Nginx configuration to add a custom HTTP header
file_line { 'http_header':
  path   => '/etc/nginx/nginx.conf',
  line   => "add_header X-Served-By \"${hostname}\";",
  notify => Exec['restart_nginx'], # Notify the nginx service to restart when the file changes
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['http_header'], # Restart when the configuration file changes
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true, # Only run when explicitly notified
}
