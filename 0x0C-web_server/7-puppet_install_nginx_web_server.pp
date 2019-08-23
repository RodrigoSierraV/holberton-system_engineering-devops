# install and configure an Nginx server using Puppet instead of Bash
exec { 'update':
command  => 'sudo apt update',
provider => shell,
} -> package {'nginx':
ensure => 'present',
}
-> file { '/tmp/holberton':
ensure  => 'present',
path    => '/var/www/html/index.html',
content => 'Holberton School',
}
-> file { '/etc/nginx/sites-available/default':
ensure => present,
}
-> file_line { 'Edit redirect':
ensure => present,
path   => '/etc/nginx/sites-available/default',
line   => 'server {
	rewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
match  => '^server {',
}
-> exec { 'restart':
command => '/usr/sbin/service nginx restart',
}
