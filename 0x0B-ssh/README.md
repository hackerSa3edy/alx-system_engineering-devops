# Project: 0x0B. SSH

## Description

This project focuses on Secure Shell (SSH), a protocol used to securely connect to remote systems over a network. SSH provides a secure channel over an unsecured network by using a client-server architecture. This project covers the basics of SSH, including creating and using SSH keys, configuring SSH clients, and understanding the advantages of using SSH.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [What is a (physical) server - text](https://www.techtarget.com/searchdatacenter/definition/server)
- [What is a (physical) server - video](https://www.youtube.com/watch?v=YyF4J4qvPRA)
- [SSH essentials](https://www.ssh.com/academy/ssh/command)
- [SSH Config File](https://www.ssh.com/academy/ssh/config)
- [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
- [How Secure Shell Works](https://www.ssh.com/academy/ssh)
- [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc)

## Learning Objectives

### General

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## Tasks

| Task                                     | Description                                            | File                                                   |
| ---------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| 0. Use a private key                     | Connect to a server using a private key                | [0-use_a_private_key](./0-use_a_private_key)           |
| 1. Create an SSH key pair                | Create an SSH RSA key pair                             | [1-create_ssh_key_pair](./1-create_ssh_key_pair)       |
| 2. Client configuration file             | Configure the SSH client to use a specific private key | [2-ssh_config](./2-ssh_config)                         |
| 3. Client configuration file (w/ Puppet) | Configure the SSH client using Puppet                  | [100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp) |

## Additional Notes

- Ensure you have SSH installed and properly configured on your system.
- Test your SSH connections in a safe environment to avoid any unintended access issues.
- Refer to the resources provided for a deeper understanding of SSH and its configuration options.
- For enhanced security, always use strong, unique passphrases for your SSH keys.
