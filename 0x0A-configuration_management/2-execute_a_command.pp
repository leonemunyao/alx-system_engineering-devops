# Create a manifest that kills a process named killmenov
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}