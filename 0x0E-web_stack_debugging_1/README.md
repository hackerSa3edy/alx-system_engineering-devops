# Project: 0x0E. Web Stack Debugging #1

## Description

This project focuses on debugging issues in a web stack, specifically related to Nginx. Web stack debugging involves identifying and resolving problems that occur within the various layers of a web application, including the server, network, and application layers. This project provides hands-on experience with common debugging tools and techniques used to diagnose and fix issues in a web stack.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [What is localhost](https://en.wikipedia.org/wiki/Localhost)
- [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
- [What is the hosts file](<https://en.wikipedia.org/wiki/Hosts_(file)>)
- [Netcat examples](https://nc110.sourceforge.io/)

## Learning Objectives

### General

- Understand the basics of web stack debugging
- Learn how to use common debugging tools such as `curl` and `sed`
- Identify and resolve issues in a web stack
- Understand the importance of logs and how to use them for debugging

## Tasks

| Task                       | Description                                                 | File                                               |
| -------------------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| 0. Nginx likes port 80     | Configure Nginx to listen on port 80 instead of 8080        | [0-nginx_likes_port_80](./0-nginx_likes_port_80)   |
| 1. Make it sweet and short | Simplify the fix for configuring Nginx to listen on port 80 | [1-debugging_made_short](./1-debugging_made_short) |

## Additional Notes

- Ensure you have the necessary permissions to access and modify the web server configuration.
- Test your debugging steps in a safe environment to avoid any unintended disruptions to your web services.
- Refer to the resources provided for a deeper understanding of web stack debugging and the tools used.
- Regularly check and analyze your server logs to monitor the performance and security of your web server.
