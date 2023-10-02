# Config for nginx server

exec {'nginx':
       command => '/bin/apt-get -y update',
       command => '/bin/apt-get -y install nginx',
    }


