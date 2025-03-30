# COMP7940_chatbot

# Digital Ocean 
ssh root@134.xxx.xxx.xxx
source myenv/bin/activate

# [SET UP Supervisor for deployment]
sudo apt install supervisor
sudo nano /etc/supervisor/conf.d/movie.conf

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start movie
sudo supervisorctl stop movie
sudo supervisorctl status

cat /var/log/movie.out.log
cat /var/log/movie.err.log

==========================
# movie.conf

In your configuration file, there should be a configuration block that looks like this:
[program:movie]
command=/root/myenv/bin/python /root/movie.py  ; Adjust based on your setup
directory=/root/                                 ; Directory where your script resides
autostart=true                                   ; Start at supervisor startup
autorestart=true                                 ; Restart if the process crashes
stderr_logfile=/var/log/movie.err.log           ; Path for stderr log
stdout_logfile=/var/log/movie.out.log           ; Path for stdout log
user=your_username                               ; Optional: specify a user
environment=PATH="/root/myenv/bin"              ; Optional: specify environment variables

===========================