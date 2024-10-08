# Project: 0x08. Networking Basics #1

## Description

This directory contains a series of scripts that demonstrate advanced networking concepts and operations. These scripts are designed to help users understand and practice more complex networking tasks, including understanding localhost, the 0.0.0.0 IP address, the hosts file, and displaying active network interfaces.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [What is Localhost](https://www.hostinger.com/tutorials/what-is-localhost)
- [What is 0.0.0.0](https://www.lifewire.com/what-is-0-0-0-0-2625920)
- [Understanding the Hosts File](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/)
- [Netcat Examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)

## Learning Objectives

### General

- Understand what localhost and the 127.0.0.1 IP address are
- Understand what the 0.0.0.0 IP address is
- Learn about the `/etc/hosts` file and its purpose
- Learn how to display your machine’s active network interfaces

## Tasks

| Task                           | Description                                                               | File                                                                 |
| ------------------------------ | ------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 0. Change your home IP         | Write a script that configures an interface to have a specific IP address | [0-change_your_home_IP](./0-change_your_home_IP)                     |
| 1. Show attached IPs           | Write a script that displays all active IP addresses on the machine       | [1-show_attached_IPs](./1-show_attached_IPs)                         |
| 2. Port listening on localhost | Write a script that listens on port 98 on localhost                       | [100-port_listening_on_localhost](./100-port_listening_on_localhost) |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each concept and its practical applications.
