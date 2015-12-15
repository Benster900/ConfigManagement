package { 'httpd':
	name => 'httpd',
	ensure => present,
}

service { 'httpd':
	ensure => running,
	enable => true,
	require => Package['httpd'],
}

package { 'nagios':
	name => 'nagios',
	ensure => present,
}
service { 'nagios':
	ensure => running,
	enable => true,
	require => Package['nagios']
}
