# COMP7940_chatbot
-use Python 3.10.16



# DEPLOY ONCE ONLY !!! (Digital Ocean)
## Need SSH KEY and connect to Digital Ocean !!
Log in to your DigitalOcean account.
Go to the "Settings" in your DigitalOcean control panel.
Navigate to the "Security" tab.
Click on the "Add SSH Key" button.
Paste your public key into the provided text area.
Give it a title so you can identify it later, then click "Add SSH Key."

## Connect to Droplet (Digital Ocean)
ssh root@134.199.209.4

sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install virtualenv
scp app/movie.py root@your_droplet_ip:/root/
scp app/ChatGPT_HKBU.py root@your_droplet_ip:/root/
scp app/config.init root@your_droplet_ip:/root/
pip3 install -r requirements.txt

# RUN THE PROGRAM
python3 movie.py

# CONNECT TO DROPLET (Digital Ocean)
ssh root@your_droplet_ip
source myenv/bin/activate

# RUN THE PROGRAM
python3 movie.py

# SET UP Supervisor for REMOTE DEPLOYMENT (ONCE ONLY!!!)
sudo apt install supervisor
sudo nano /etc/supervisor/conf.d/movie.conf

========================== 
## movie.conf (ONCE ONLY!!!)

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
## UPDATE AND RUN DEPLOYMENT (By supervisor)

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start movie
sudo supervisorctl stop movie
sudo supervisorctl status

cat /var/log/movie.out.log
cat /var/log/movie.err.log