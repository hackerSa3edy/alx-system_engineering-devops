# Install and configure a nginx web server
# with a custom header

exec { 'update_repo':
    command  => 'apt-get -y update',
    provider => shell,
}

package { 'install_nginx':
    ensure  => 'installed',
    name    => 'nginx',
    require => Exec['update_repo'],
}

exec { 'Add_custom_header':
    command  => 'sed -i "s#root /var/www/html;#\0\n\tadd_header X-Served-By $(hostname);#g" /etc/nginx/sites-enabled/default',
    require  => Package['install_nginx'],
    provider => shell,
}

exec { 'overwrite_sites_enabled':
    command  => 'cp -f /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default',
    provider => shell,
    require  => Exec['Add_custom_header'],
}

service { 'start_nginx':
    ensure  => 'running',
    name    => 'nginx',
    require => Exec['overwrite_sites_enabled'],
}
