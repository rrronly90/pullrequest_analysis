#remove and create temp dir
rm  -rf /tmp/deploy/
mkdir -p /tmp/deploy/

#copy the repo file to deployment directory
cp * /tmp/deploy/

#remove and existing credentials file from required location
rm -rf /tmp/deploy/credentials.json

#get file name of local file . and copy
file_loc=`cat config.py | grep "keypathlocal" | cut -d"=" -f2`

#get function name to deploy
functionname=`cat config.py | grep functionname | cut -d= -f2 | tr -d '"' `
echo $functionname


comm="sudo cp ${file_loc} /tmp/deploy/"
eval "$comm"
sudo chmod 777 /tmp/deploy/*

#deploy real time ingress cloud function
url="https:"`sudo gcloud functions deploy $functionname --entry-point get_data --runtime python38  --trigger-http --source=/tmp/deploy/ | grep "url: https:" | cut -d":" -f3`

#we need access token in order to create github webhook.
read -p "enter github access token:" access_token


#create webhook
python3 /tmp/deploy/createwebhook.py $url $access_token

#create required GCP resource for batch programming
gcloud pubsub topics create dailycron-topic
gcloud pubsub subscriptions create dailycron-sub --topic dailycron-topic
gcloud scheduler jobs create pubsub dailycron --schedule "0 23 * * 0" --topic dailycron-topic --message-body "Hello"

#remove unwanted resource for batch and move main.py
rm -rf /tmp/deploy/main.py
mv /tmp/deploy/batch_loads.py /tmp/deploy/main.py

#create function to process batch data , we should have used V2 with have 4 gb and 2 hrs of run time .
url_batch="https:"`sudo gcloud functions deploy batch_pull_reuqest --entry-point get_data --runtime python38  --trigger-topic dailycron-topic --source=/tmp/deploy/ | grep "url: https:" | cut -d":" -f3`



