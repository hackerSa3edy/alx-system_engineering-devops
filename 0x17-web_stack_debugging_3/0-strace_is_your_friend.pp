# Puppet script to correct the file name from class-wp-locale.phpp to class-wp-locale.php
# Fixes Apache 500 error

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
