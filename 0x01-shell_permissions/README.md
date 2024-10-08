# 0x01-shell_permissions

## Description

This directory contains a series of scripts that demonstrate basic shell permissions and their usage. These scripts are designed to help users understand and practice fundamental shell operations related to file and directory permissions, user management, and privilege escalation.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Linux File Permissions](https://www.guru99.com/file-permissions.html)
- [Understanding Linux File Permissions](https://linuxhandbook.com/linux-file-permissions/)
- [Linux Users and Groups](https://www.tecmint.com/add-users-in-linux/)
- [Sudo Command in Linux](https://www.sudo.ws/man/1.8.15/sudo.man.html)

## Learning Objectives

### General

- Understand the basic concepts of file and directory permissions
- Learn how to change file and directory permissions using `chmod`
- Understand how to change file and directory ownership using `chown` and `chgrp`
- Learn how to manage users and groups in a Linux system
- Understand the use of the `sudo` command for privilege escalation

## Tasks

| Task                    | Description                                                                                                                                         | File                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 0. My name is Betty     | Create a script that switches the current user to the user `betty`                                                                                  | [0-iam_betty](./0-iam_betty)                                     |
| 1. Who am I             | Write a script that prints the effective username of the current user                                                                               | [1-who_am_i](./1-who_am_i)                                       |
| 2. Groups               | Write a script that prints all the groups the current user is part of                                                                               | [2-groups](./2-groups)                                           |
| 3. New owner            | Write a script that changes the owner of the file `hello` to the user `betty`                                                                       | [3-new_owner](./3-new_owner)                                     |
| 4. Empty!               | Write a script that creates an empty file called `hello`                                                                                            | [4-empty](./4-empty)                                             |
| 5. Execute              | Write a script that adds execute permission to the owner of the file `hello`                                                                        | [5-execute](./5-execute)                                         |
| 6. Multiple permissions | Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`               | [6-multiple_permissions](./6-multiple_permissions)               |
| 7. Everybody!           | Write a script that adds execution permission to the owner, the group owner, and the other users, to the file `hello`                               | [7-everybody](./7-everybody)                                     |
| 8. James Bond           | Write a script that sets the permission to the file `hello` as follows: Owner - no permission, Group - no permission, Other users - all permissions | [8-James_Bond](./8-James_Bond)                                   |
| 9. John Doe             | Write a script that sets the mode of the file `hello` to `-rwxr-x-wx`                                                                               | [9-John_Doe](./9-John_Doe)                                       |
| 10. Look in the mirror  | Write a script that sets the mode of the file `hello` the same as `olleh`'s mode                                                                    | [10-mirror_permissions](./10-mirror_permissions)                 |
| 11. Directories         | Write a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users      | [11-directories_permissions](./11-directories_permissions)       |
| 12. More directories    | Create a script that creates a directory called `my_dir` with permissions 751 in the working directory                                              | [12-directory_permissions](./12-directory_permissions)           |
| 13. Change group        | Write a script that changes the group owner to `school` for the file `hello`                                                                        | [13-change_group](./13-change_group)                             |
| 14. Owner and group     | Write a script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory        | [100-change_owner_and_group](./100-change_owner_and_group)       |
| 15. Symbolic links      | Write a script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively                                         | [101-symbolic_link_permissions](./101-symbolic_link_permissions) |
| 16. If only             | Write a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`                                    | [102-if_only](./102-if_only)                                     |
| 17. Star Wars           | Write a script that will play the StarWars IV episode in the terminal                                                                               | [103-Star_Wars](./103-Star_Wars)                                 |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts.
- Test the scripts in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each command and its options.
