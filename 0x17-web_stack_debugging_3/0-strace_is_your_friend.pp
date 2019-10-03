#Fix error in .php extension

exec { 'strace':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin:/usr/bin'
}
