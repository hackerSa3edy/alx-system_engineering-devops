## Moving Local Screenshots to the Sandbox Environment using SFTP

This document describes the steps involved in using the SFTP command-line tool to move local screenshots to the sandbox environment.

**Prerequisites:**

* SFTP client installed and configured on your local machine.
* SSH access to the sandbox environment with valid credentials.
* Directory containing your local screenshots.

**Steps:**

**1. Navigate to the directory containing your screenshots:**

Open a terminal window and navigate to the directory containing your local screenshots using the `cd` command.

Example:

```
cd ~/Pictures/Screenshots
```

**2. Connect to the sandbox environment using SFTP:**

Use the `sftp` command followed by the username and hostname of the sandbox environment.

Example:

```
sftp username@sandbox.example.com
```

**3. Enter your password when prompted.**

**4. Change to the target directory in the sandbox environment:**

Navigate to the desired directory in the sandbox environment where you want to move the screenshots.

Example:

```
sftp> cd /alx/alx-system_engineering-devops/command_line_for_the_win/
```

**5. Upload the local screenshots:**

Use the `put` command followed by the local file path and the desired filename in the sandbox environment.

Example:

```
sftp> put 0-first_9_tasks.png
sftp> put 1-next_9_tasks.png
sftp> put 2-next_9_tasks.png
```

**6. Verify the uploaded files:**

Use the `ls` command to list the files in the current directory and confirm the presence of the uploaded screenshots.

Example:

```
sftp> ls
```

**7. Disconnect from the SFTP session:**

Use the `exit` command to close the SFTP connection.

Example:

```
sftp> exit
```

**Additional Notes:**

* You can use the `*` wildcard to upload multiple files with similar names.
* You can use the `-r` flag with the `put` command to upload an entire directory recursively.
* For enhanced security, consider using SSH key-based authentication instead of password authentication.
