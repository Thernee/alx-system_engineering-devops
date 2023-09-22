# install flask from pip3

exec { 'flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep 2.1.0',
}