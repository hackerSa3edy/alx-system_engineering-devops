# A manifest that kills a process named killmenow

exec { 'pkill -f killmenow':
  onlyif => 'pgrep -f killmenow',
  path   => '/usr/bin'
}
