# Config for installing and setting up nginx server using puppet

exec {'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx by modifying the default site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \"${hostname}\";
    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /redirect_me {
        return 301 https://twitter.com/;
    }

}\n",
  require => Package['nginx'], # Ensure Nginx package is installed before applying this configuration
}

# Ensure Nginx service is running and reload the configuration when changed
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/nginx/sites-enabled/default'],
}
