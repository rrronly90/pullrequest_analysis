rm  -rf /tmp/deploy/
mkdir -p /tmp/deploy/
cp * /tmp/deploy/
rm -rf /tmp/deploy/credentials.json
file_loc=`cat config.py | grep "key" | cut -d"=" -f2`

comm="sudo cp ${file_loc} /tmp/deploy/"
eval "$comm"
sudo chmod 777 /tmp/deploy/*
