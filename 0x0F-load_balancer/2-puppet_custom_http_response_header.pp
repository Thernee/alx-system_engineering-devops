# Config for installing and setting up nginx server using puppet

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
    ensure  => 'file',
    content => "Ceci n'est pas une page",
}

# Configure Nginx by modifying the default site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \"\$HOSTNAME\";
    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /redirect_me {
        return 301 https://twitter.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
	internal;
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
