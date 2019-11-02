#!/usr/bin/env bash

# NOTICE: For Ubuntu 16.04 LTS and 18.04 LTS ONLY

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

version=$(lsb_release -r -s)  # Detects Ubuntu version to install correct version of MongoDB
if [[ "${version}" = "16.04" ]]; then
   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
fi
if [[ "${version}" = "18.04" ]]; then
   echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
fi

sudo apt-get update
sudo apt-get install -y mongodb-org

mongod --dbpath ./results --logpath ./results/log/mongodb.log --replSet monitoring_replSet &

sleep 1s

return_code=1
while [[ ${return_code} -ne 0 ]]
do
   mongo --eval "rs.initiate()" 2>/dev/null
   return_code=$?
   sleep 0.5s
done

if pgrep mongod > /dev/null ; then
   mongo_process=$(pgrep mongod)
   kill ${mongo_process}
fi
