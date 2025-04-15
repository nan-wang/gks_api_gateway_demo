
1. install `gcloud cli`
1. deploy the cloud functions
```
gcloud functions deploy listSmoothies --region us-central1 --trigger-http --entry-point listSmoothies --runtime python312 --no-allow-unauthenticated --source listSmoothies
```
1. deploy the cloud functions
```
```
1. enable API
```
$ gcloud services enable apigateway.googleapis.com
$ gcloud services enable servicemanagement.googleapis.com
$ gcloud services enable servicecontrol.googleapis.com
```
1. create API


## Reference
[Tutorial](https://beranger.medium.com/secure-google-cloud-functions-with-api-gateway-848f687963ae)
