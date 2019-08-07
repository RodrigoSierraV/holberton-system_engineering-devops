#manifest that kills a process named killmenow.
#Requirements:
#Must use the exec Puppet resource
#Must use pkill

exec { 'killmenow':
    path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command  => 'pkill killmenow',
    provider => 'shell',
}
