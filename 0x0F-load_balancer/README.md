# Project: 0x0F. Load Balancer

## Description

This project focuses on setting up and configuring a load balancer using HAProxy. Load balancing is a crucial component in web infrastructure, ensuring high availability and reliability by distributing incoming traffic across multiple servers. This project covers the basics of load balancing, including installation, configuration, and management of HAProxy, as well as adding custom HTTP headers.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Introduction to Load Balancing and HAProxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [HAProxy Documentation](http://www.haproxy.org/#docs)
- [Debian/Ubuntu HAProxy Packages](https://haproxy.debian.net/)

## Learning Objectives

### General

- Understand the basics of load balancing
- Learn how to install and configure HAProxy
- Understand how to distribute traffic across multiple web servers
- Learn how to add custom HTTP headers using HAProxy

## Tasks

| Task                                    | Description                                                    | File                                                                                 |
| --------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 0. Double the number of webservers      | Configure HAProxy to distribute traffic across two web servers | [0-custom_http_response_header](./0-custom_http_response_header)                     |
| 1. Install your load balancer           | Install and configure HAProxy on your server                   | [1-install_load_balancer](./1-install_load_balancer)                                 |
| 2. Add a custom HTTP header with Puppet | Use Puppet to add a custom HTTP header in HAProxy              | [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp) |

## Additional Notes

- Ensure you have the necessary permissions to install and configure software on your server.
- Test your configurations in a safe environment to avoid any unintended disruptions to your web services.
- Refer to the resources provided for a deeper understanding of load balancing and HAProxy configuration.
- Regularly check and analyze your server logs to monitor the performance and security of your load balancer.
