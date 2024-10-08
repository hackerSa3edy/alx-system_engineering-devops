# Project: 0x0C. Web Server

## Description

This project focuses on setting up and configuring a web server using Nginx. A web server is a crucial component in web development, responsible for serving web pages to users. This project covers the basics of web servers, including installation, configuration, and management of Nginx, as well as handling HTTP requests and responses.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://www.nginx.com/resources/wiki/)
- [How to Configure Nginx](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/)
- [Child process concept page](https://nodejs.org/en/docs/guides/anatomy-of-an-http-transaction/)
- [Root and sub domain](https://www.cloudflare.com/learning/dns/glossary/subdomain/)
- [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [HTTP redirection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections)
- [Not found HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)
- [Logs files on Linux](https://www.loggly.com/ultimate-guide/linux-logging-basics/)

## Learning Objectives

### General

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

## Tasks

| Task                                    | Description                                    | File                                                                           |
| --------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------ |
| 0. Transfer a file to your server       | Transfer a file to your server using SCP       | [0-transfer_file](./0-transfer_file)                                           |
| 1. Install nginx web server             | Install and configure Nginx on your web server | [1-install_nginx_web_server](./1-install_nginx_web_server)                     |
| 2. Setup a domain name                  | Configure a domain name for your web server    | [2-setup_a_domain_name](./2-setup_a_domain_name)                               |
| 3. Redirection                          | Configure Nginx to perform a redirection       | [3-redirection](./3-redirection)                                               |
| 4. Not found page 404                   | Configure a custom 404 page in Nginx           | [4-not_found_page_404](./4-not_found_page_404)                                 |
| 5. Install Nginx web server (w/ Puppet) | Install and configure Nginx using Puppet       | [7-puppet_install_nginx_web_server.pp](./7-puppet_install_nginx_web_server.pp) |

## Additional Notes

- Ensure you have the necessary permissions to install and configure software on your server.
- Test your configurations in a safe environment to avoid any unintended disruptions to your web services.
- Refer to the resources provided for a deeper understanding of web servers and Nginx configuration.
- Regularly check and analyze your server logs to monitor the performance and security of your web server.
