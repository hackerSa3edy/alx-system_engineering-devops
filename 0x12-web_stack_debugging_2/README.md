# Project: 0x12. Web Stack Debugging #2

## Description

This project focuses on debugging issues in a web stack. Web stack debugging involves identifying and resolving problems that occur within the various layers of a web application, including the server, network, and application layers. This project provides hands-on experience with common debugging tools and techniques used to diagnose and fix issues in a web stack.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Introduction to strace](https://www.redhat.com/sysadmin/strace)
- [How to Use strace](https://www.tecmint.com/strace-command-in-linux/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [How to Manage Nginx Processes](https://www.digitalocean.com/community/tutorials/how-to-manage-nginx-processes)
- [Linux Process Management](https://www.geeksforgeeks.org/process-management-in-linux/)

## Learning Objectives

### General

- Understand the basics of web stack debugging
- Learn how to use common debugging tools such as `strace`
- Identify and resolve issues in a web stack
- Understand the importance of logs and how to use them for debugging
- Learn how to manage and debug Nginx processes

## Tasks

| Task                            | Description                                                     | File                                                       |
| ------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------- |
| 0. Run software as another user | Write a script that runs a command as another user              | [0-iamsomeoneelse](./0-iamsomeoneelse)                     |
| 1. Run Nginx as Nginx           | Write a script that configures Nginx to run as the `nginx` user | [1-run_nginx_as_nginx](./1-run_nginx_as_nginx)             |
| 2. 7 lines or less              | Write a script that fixes a given issue in 7 lines or less      | [100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less) |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each concept and its practical applications.
- Regularly check and analyze your server logs to monitor the performance and security of your web server.
