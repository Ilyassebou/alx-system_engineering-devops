# Install Flask package from pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
