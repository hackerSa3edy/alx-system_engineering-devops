# Project: 0x14. MySQL

## Description

This project focuses on understanding and configuring MySQL databases, including setting up primary-replica clusters and implementing robust database backup strategies. MySQL is a widely-used relational database management system that helps in managing and organizing data efficiently. This project provides hands-on experience with MySQL setup, configuration, and maintenance.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [What is a Primary-Replica Cluster?](https://www.digitalocean.com/community/tutorials/understanding-mysql-replication)
- [MySQL Primary-Replica Setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
- [Build a Robust Database Backup Strategy](https://www.mysqltutorial.org/mysql-backup.aspx)

## Learning Objectives

### General

- Understand the main role of a database
- Learn what a database replica is
- Understand the purpose of a database replica
- Know why database backups need to be stored in different physical locations
- Learn what operations should be regularly performed to ensure that your database backup strategy works

## Tasks

| Task                                                  | Description                                         | File                                                                                                                               |
| ----------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 4. Setup a Primary-Replica infrastructure using MySQL | Configure a primary-replica setup using MySQL       | [4-mysql_configuration_primary](./4-mysql_configuration_primary), [4-mysql_configuration_replica](./4-mysql_configuration_replica) |
| 5. MySQL backup                                       | Implement a backup strategy for your MySQL database | [5-mysql_backup](./5-mysql_backup)                                                                                                 |

## Additional Notes

- Ensure you have the necessary permissions to execute the commands.
- Test the configurations in a safe environment to avoid any unintended disruptions to your database.
- Refer to the resources provided for a deeper understanding of each concept and its practical applications.
- Regularly review and update your database backup strategies to maintain data integrity and availability.
