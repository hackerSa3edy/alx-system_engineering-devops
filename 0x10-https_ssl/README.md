# Project: 0x10. HTTPS SSL

## Resources

#### Read or watch:

* [What is HTTPS?](https://intranet.alxswe.com/rltoken/XT1BAiBL3Jpq1bn1q6IYXQ)
* [What are the 2 main elements that SSL is providing](https://intranet.alxswe.com/rltoken/STj5WkAPACBxOvwB77Ycrw)
* [HAProxy SSL termination on Ubuntu16.04](https://intranet.alxswe.com/rltoken/asrMHTWJxWQ2x-Sn6snHow)
* [SSL termination](https://intranet.alxswe.com/rltoken/CKUICfppIWI6UC0coEMB8g)
* [Bash function](https://intranet.alxswe.com/rltoken/zPjZ7-eSSQsLFsGA16C1HQ)
## Learning Objectives

### General

* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means
## Tasks

| Task | File |
| ---- | ---- |
| 0. World wide web | [0-world_wide_web](./0-world_wide_web) |
| 1. HAproxy SSL termination | [1-haproxy_ssl_termination](./1-haproxy_ssl_termination) |
| 2. No loophole in your website traffic | [100-redirect_http_to_https](./100-redirect_http_to_https) |

### Certbot Commands Log
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
