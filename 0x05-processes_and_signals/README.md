# Project: 0x05. Processes and Signals

## Description

This project focuses on understanding and managing processes and signals in a Unix-like operating system. Processes are instances of running programs, and signals are a form of inter-process communication used to notify processes of events. This project provides hands-on experience with various commands and techniques to manage processes and handle signals.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Linux Processes](https://www.tutorialspoint.com/unix/unix-processes.htm)
- [Linux Signals](https://www.tutorialspoint.com/unix/unix-signals-traps.htm)
- [Process Management in Unix](https://www.geeksforgeeks.org/process-management-in-unix/)
- [Understanding Signals](https://www.gnu.org/software/libc/manual/html_node/Signals.html)
- [kill Command](https://man7.org/linux/man-pages/man1/kill.1.html)

## Learning Objectives

### General

- Understand what a process is and how to manage processes in Unix-like operating systems
- Learn how to use commands like `ps`, `pgrep`, `pkill`, `kill`, `top`, and `htop` to manage processes
- Understand what a signal is and how signals are used for inter-process communication
- Learn how to send and handle signals using commands like `kill` and `trap`
- Understand the different types of signals and their default behaviors

## Tasks

| Task                            | Description                                                                                                                                                       | File                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 0. What is my PID               | Write a Bash script that displays its own PID                                                                                                                     | [0-what-is-my-pid](./0-what-is-my-pid)                             |
| 1. List your processes          | Write a Bash script that displays a list of currently running processes                                                                                           | [1-list_your_processes](./1-list_your_processes)                   |
| 2. Show your Bash PID           | Write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process                                  | [2-show_your_bash_pid](./2-show_your_bash_pid)                     |
| 3. Show your Bash PID made easy | Write a Bash script that displays the PID, along with the process name, of processes whose name contains the string `bash`                                        | [3-show_your_bash_pid_made_easy](./3-show_your_bash_pid_made_easy) |
| 4. To infinity and beyond       | Write a Bash script that displays `To infinity and beyond` indefinitely                                                                                           | [4-to_infinity_and_beyond](./4-to_infinity_and_beyond)             |
| 5. Don't stop me now!           | Write a Bash script that stops `4-to_infinity_and_beyond` process                                                                                                 | [5-dont_stop_me_now](./5-dont_stop_me_now)                         |
| 6. Stop me if you can           | Write a Bash script that stops `4-to_infinity_and_beyond` process using `kill`                                                                                    | [6-stop_me_if_you_can](./6-stop_me_if_you_can)                     |
| 7. Highlander                   | Write a Bash script that displays `To infinity and beyond` indefinitely, with a `sleep 2` in between each iteration, and stops after receiving a `SIGTERM` signal | [7-highlander](./7-highlander)                                     |
| 8. Beheaded process             | Write a Bash script that kills the process `7-highlander`                                                                                                         | [8-beheaded_process](./8-beheaded_process)                         |
| 9. Process and PID file         | Write a Bash script that creates the file `/var/run/myscript.pid` containing its PID and displays `To infinity and beyond` indefinitely                           | [100-process_and_pid_file](./100-process_and_pid_file)             |
| 10. Manage my process           | Write a Bash script that manages the `100-process_and_pid_file` script, starting and stopping it as needed                                                        | [101-manage_my_process](./101-manage_my_process)                   |
| 11. Zombie                      | Write a C program that creates 5 zombie processes                                                                                                                 | [102-zombie.c](./102-zombie.c)                                     |
| 12. Screencast                  | Create a screencast demonstrating the execution of the previous tasks                                                                                             | [103-screencast](./103-screencast)                                 |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each concept and its practical applications.
- Regularly review and update your scripts to maintain compatibility with the latest system updates.
