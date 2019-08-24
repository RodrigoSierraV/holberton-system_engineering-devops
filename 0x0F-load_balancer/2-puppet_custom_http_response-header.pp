# install and configure an Nginx server using Puppet instead of Bash
exec { 'update':
command  => 'sudo apt update',
provider => shell,
} -> package {'nginx':
ensure => 'present',
}
-> file { '/etc/nginx/nginx.conf':
ensure => present,
}
-> file_line { 'Edit redirect':
ensure => present,
path   => '/etc/nginx/nginx.conf',
line   => "http {
	add_header X-Served-By ${hostname};",
match  => '^http {',
}
-> exec { 'restart':
command => '/usr/sbin/service nginx restart',
}
