# Install and configure an Nginx server.
# perform a 301 redirect when querying /redirect_me.

package { 'nginx':
  ensure   => latest,
  provider => apt,
}

file { 'nginx_index.html':
  ensure  => file,
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
  require => Package['nginx'],
}


$redir_conf = '\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}'
$cmd = "sed -i \"53i\\ ${redir_conf}\" /etc/nginx/sites-enabled/default &> /dev/null"

exec { 'redirect_path':
  command => $cmd,
  path    => '/usr/bin',
  require => Package['nginx'],
}
