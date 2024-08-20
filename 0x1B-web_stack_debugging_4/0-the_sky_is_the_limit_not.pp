#0-the_sky_is_the_limit_not.pp set open file limit higher
exec { 'set limit to 2000':
  path    => '/bin',
  command => "sed -i 's/15/4096/' /etc/default/nginx"
}
exec { 'reboot nginx':
  command => '/usr/sbin/service nginx restart'
}
