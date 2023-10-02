# Config for installing and setting up nginx server using puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
  before  => Package['nginx'],
}

package { 'nginx':
  ensure  => installed,
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
  require => Package['nginx'],
}

file_line { 'redirect_me':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.twitter.com permanent;',
}

file_line { 'add_header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
