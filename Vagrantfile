# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |v|
    v.name = "pelican_nest"
  end

      
  config.vm.box = "ubuntu/trusty64"

  config.vm.provision "shell", path: "./scripts/vagrant/provision.sh"
  
  # Run this after the machine is 'upped'
  # (regenerate blog)
  config.trigger.after :up do
    info "Regenerating blog ..."
    run_remote  "bash /vagrant/scripts/vagrant/after_up.sh"
  end

  # Run this before the machine is halted
  config.trigger.before :halt do
    run_remote  "bash /vagrant/scripts/vagrant/before_halt.sh"
  end

  # This correctly forwards the development server 
  config.vm.network "forwarded_port", guest: 8000, host: 8080
end
