# Project: 0x13. Firewall

## Description

This project focuses on understanding and configuring firewalls. Firewalls are essential for network security as they control the incoming and outgoing network traffic based on predetermined security rules. This project provides hands-on experience with configuring firewall rules to secure a network.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [What is a Firewall?](https://www.cloudflare.com/learning/firewall/what-is-a-firewall/)
- [How Firewalls Work](https://www.howtogeek.com/342077/how-do-firewalls-work/)
- [UFW - Uncomplicated Firewall](https://help.ubuntu.com/community/UFW)
- [Introduction to iptables](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)
- [Port Forwarding](https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/)

## Learning Objectives

### General

- Understand what a firewall is and its purpose
- Learn how to configure basic firewall rules
- Understand the concept of port forwarding
- Learn how to use UFW (Uncomplicated Firewall) for firewall management
- Understand how to use iptables for more advanced firewall configurations

## Tasks

| Task                              | Description                                                                       | File                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 0. Block all incoming traffic but | Configure a firewall rule to block all incoming traffic except for specific ports | [0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but) |
| 1. Port forwarding                | Configure port forwarding to redirect traffic from one port to another            | [100-port_forwarding](./100-port_forwarding)                           |

## Additional Notes

- Ensure you have the necessary permissions to execute the commands.
- Test the firewall rules in a safe environment to avoid any unintended disruptions to your network.
- Refer to the resources provided for a deeper understanding of each concept and its practical applications.
- Regularly review and update your firewall rules to maintain network security.
