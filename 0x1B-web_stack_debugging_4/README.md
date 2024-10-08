# Project: 0x1B. Web Stack Debugging #4

## Description

This project focuses on advanced web stack debugging techniques. Web stack debugging involves identifying and resolving problems that occur within the various layers of a web application, including the server, network, and application layers. This project provides hands-on experience with common debugging tools and techniques used to diagnose and fix issues in a web stack, particularly focusing on performance and user limits.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Introduction to strace](https://linux.die.net/man/1/strace)
- [Understanding Linux CPU Load](https://scoutapm.com/blog/understanding-load-averages)
- [Linux Performance Tuning](https://www.tecmint.com/linux-performance-monitoring-and-tuning/)
- [Managing Linux User Limits with ulimit](https://www.baeldung.com/linux/ulimit-command)

## Learning Objectives

### General

- Understand advanced web stack debugging techniques
- Learn how to use `strace` for debugging
- Understand how to monitor and tune Linux performance
- Learn how to manage user limits using `ulimit`

## Tasks

| Task                                               | Description                                                   | File                                                             |
| -------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------- |
| 0. Sky is the limit, let's bring that limit higher | Increase the maximum number of file descriptors for a process | [0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp) |
| 1. User limit                                      | Configure user limits for processes                           | [1-user_limit.pp](./1-user_limit.pp)                             |

## Additional Notes

- Ensure you have the necessary permissions to access and modify system configurations.
- Test your debugging steps in a safe environment to avoid any unintended disruptions to your web services.
- Refer to the resources provided for a deeper understanding of advanced web stack debugging and performance tuning.
- Regularly check and analyze your server logs to monitor the performance and security of your web server.
