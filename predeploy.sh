rm  -rf /tmp/deploy/
mkdir -p /tmp/deploy/
cp * /tmp/deploy/
rm -rf /tmp/deploy/credentials.json
file_loc=`cat config.py | grep "keypathlocal" | cut -d"=" -f2`
functionname=`cat config.py | grep functionname | cut -d= -f2 | tr -d '"' `
echo $functionname


comm="sudo cp ${file_loc} /tmp/deploy/"
eval "$comm"
sudo chmod 777 /tmp/deploy/*

url="https:"`sudo gcloud functions deploy $functionname --entry-point get_data --runtime python37  --trigger-http --source=/tmp/deploy/ | grep "url: https:" | cut -d":" -f3`

read -p "enter github access token:" access_token

python3 /tmp/deploy/createwebhook.py $url $access_token


gcloud pubsub topics create dailycron-topic
gcloud pubsub subscriptions create dailycron-sub --topic dailycron-topic
gcloud scheduler jobs create pubsub dailycron --schedule "0 23 * * 0" --topic dailycron-topic --message-body "Hello"


rm -rf /tmp/deploy/*
eval "$comm"
cp batch_loads.py /tmp/deploy/
cp requirements.txt /tmp/deploy/
url_batch="https:"`sudo gcloud functions deploy pull_batch --entry-point get_data --runtime python37  --trigger- --source=/tmp/deploy/ | grep "url: https:" | cut -d":" -f3`
url_batch="https:"`sudo gcloud functions deploy batch_pull_reuqest --entry-point get_data --runtime python37  --trigger-topic dailycron-topic --source=/tmp/deploy/ | grep "url: https:" | cut -d":" -f3`



