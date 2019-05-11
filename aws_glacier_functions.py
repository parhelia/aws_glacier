import boto3
import json

#defaults
accountId = '-'
vautlName = yourVaultName

client=boto3.client('glacier')

def describe_vault():
	response=client.describe_vault(
		accountId=accountId,
		vaultName=vaultName
	)
	print(response)

# retrieves inventory of the specified vaultName
def start_inventory_retrieval(vaultName):
	client.initiate_job(
		accountId=accountId,
		vaultName=vaultName,
		jobParameters = {'Type'='inventory-retrieval'}
		)

# once the job has succeeded
def get_job_output(vaultName, jobId):
	response=client.get_job_output(
		vaultName=vaultName,
		jobId=jobId
		)

	data = json.loads(response['body'].read())
	print(json.dumps(data, indent=4, sort_keys=True))