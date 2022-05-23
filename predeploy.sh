rm  -rf /tmp/deploy/
mkdir -p /tmp/deploy/
cp * /tmp/deploy/
rm -rf /tmp/deploy/credentials.json
file_loc=`cat config.py | grep "keypathlocal" | cut -d"=" -f2`
functionname=`cat config.py | grep "functionname" | cut -d"=" -f2`

comm="sudo cp ${file_loc} /tmp/deploy/"
eval "$comm"
sudo chmod 777 /tmp/deploy/*

url=echo "https:"`sudo gcloud functions deploy functionname --entry-point get_data --runtime python37  --trigger-http --source=/tmp/deploy/ | grep "url: https:" | cut -d":" -f3`

echo $url
read -p "enter github access token:" access_token

python3 /tmp/deploy/createwebhook.py $url $access_token
