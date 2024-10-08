# Project: 0x1A. Application Server

## Description

This project focuses on setting up and configuring an application server using Gunicorn and Nginx. An application server is a crucial component in web infrastructure, responsible for running application code and serving dynamic content. This project covers the basics of application servers, including installation, configuration, and management of Gunicorn and Nginx, as well as handling HTTP requests and responses.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Additional Notes](#additional-notes)

## Resources

### Read or watch

- [Application Server vs Web Server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04)
- [Running Gunicorn](https://docs.gunicorn.org/en/stable/run.html)
- [Be Careful with the Way Flask Manages Slash](https://stackoverflow.com/questions/21827324/flask-trailing-slash)
- [Upstart Documentation](http://upstart.ubuntu.com/cookbook/)

## Learning Objectives

### General

- Understand the difference between an application server and a web server
- Learn how to install and configure Gunicorn
- Learn how to install and configure Nginx
- Understand how to serve a Flask application using Gunicorn and Nginx
- Learn how to manage application server processes using Upstart

## Tasks

| Task                                 | Description                                                           | File                                                             |
| ------------------------------------ | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 2. Serve a page with Nginx           | Configure Nginx to serve a page                                       | [2-app_server-nginx_config](./2-app_server-nginx_config)         |
| 3. Add a route with query parameters | Add a route with query parameters to the application                  | [3-app_server-nginx_config](./3-app_server-nginx_config)         |
| 4. Let's do this for your API        | Configure the application server to serve an API                      | [4-app_server-nginx_config](./4-app_server-nginx_config)         |
| 5. Serve your AirBnB clone           | Configure the application server to serve an AirBnB clone application | [5-app_server-nginx_config](./5-app_server-nginx_config)         |
| 6. Deploy it!                        | Deploy the application using Gunicorn                                 | [gunicorn.service](./gunicorn.service)                           |
| 7. No service interruption           | Reload Gunicorn without downtime                                      | [4-reload_gunicorn_no_downtime](./4-reload_gunicorn_no_downtime) |

## Additional Notes

- Ensure you have the necessary permissions to install and configure software on your server.
- Test your configurations in a safe environment to avoid any unintended disruptions to your web services.
- Refer to the resources provided for a deeper understanding of application servers and their configuration.
- Regularly check and analyze your server logs to monitor the performance and security of your application server.
