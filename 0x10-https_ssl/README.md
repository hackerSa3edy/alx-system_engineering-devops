# Project: 0x10. HTTPS SSL

## Description

This directory contains a series of tasks that demonstrate the implementation and management of HTTPS and SSL in web servers. HTTPS (HyperText Transfer Protocol Secure) is an extension of HTTP that uses SSL/TLS to encrypt data between the client and server, ensuring secure communication. These tasks are designed to help users understand the importance of HTTPS, how to set it up, and how to manage SSL termination.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Certbot Commands Log](#certbot-commands-log)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)
- [What are the 2 main elements that SSL is providing](https://www.instantssl.com/ssl-certificate-products/ssl.html)
- [HAProxy SSL termination on Ubuntu16.04](https://www.haproxy.com/blog/haproxy-ssl-termination/)
- [SSL termination](https://www.nginx.com/resources/glossary/ssl-termination/)
- [Bash function](https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-8.html)

## Learning Objectives

### General

- Understand the two main roles of HTTPS SSL
- Learn the purpose of encrypting traffic
- Understand what SSL termination means

## Tasks

| Task                                   | Description                                                                                                       | File                                                       |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 0. World wide web                      | Configure your domain zone so that the subdomain `www` points to your load-balancer IP (LB)                       | [0-world_wide_web](./0-world_wide_web)                     |
| 1. HAproxy SSL termination             | Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www` | [1-haproxy_ssl_termination](./1-haproxy_ssl_termination)   |
| 2. No loophole in your website traffic | Configure HAproxy to automatically redirect HTTP traffic to HTTPS                                                 | [100-redirect_http_to_https](./100-redirect_http_to_https) |

## Certbot Commands Log

```bash
sudo apt update
sudo apt install snapd
sudo apt-get remove certbot
sudo apt-get install certbot
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d example.com -d www.example.com
sudo ls /etc/letsencrypt/live/your_domain_name
sudo mkdir -p /etc/haproxy/certs
DOMAIN='example.com' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs
sudo nano /etc/haproxy/haproxy.cfg
```

## Additional Notes

- Ensure you have the necessary permissions to execute the commands.
- Test the configuration in a safe environment to avoid any unintended disruptions to your web services.
- Refer to the resources provided for a deeper understanding of each concept and its practical applications.
