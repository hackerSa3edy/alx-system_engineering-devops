# Project: 0x0A. Configuration Management

## Description

This project focuses on configuration management using Puppet. Configuration management is essential for maintaining consistency across systems, automating repetitive tasks, and ensuring that systems are configured correctly. Puppet is a powerful tool that allows you to define the desired state of your systems and automatically enforce that state.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://puppet.com/docs/puppet/latest/types/file.html)
- [Puppet's Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Learning Objectives

### General

- Understand the purpose and benefits of configuration management
- Learn the basics of Puppet and its declarative language
- Understand how to use Puppet to manage files, packages, and services
- Learn how to write and apply Puppet manifests
- Understand the importance of idempotency in configuration management

## Tasks

| Task                 | Description                    | File                                               |
| -------------------- | ------------------------------ | -------------------------------------------------- |
| 0. Create a file     | Create a file using Puppet     | [0-create_a_file.pp](./0-create_a_file.pp)         |
| 1. Install a package | Install a package using Puppet | [1-install_a_package.pp](./1-install_a_package.pp) |
| 2. Execute a command | Execute a command using Puppet | [2-execute_a_command.pp](./2-execute_a_command.pp) |

## Additional Notes

- Ensure you have Puppet installed and properly configured on your system.
- Test your Puppet manifests in a safe environment before applying them to production systems.
- Use Puppet lint to check your manifests for syntax and style issues.
- Refer to the official Puppet documentation for more advanced usage and best practices.
