import boto3

# 1. Create connections to S3 and SNS
s3 = boto3.resource('s3')
sns = boto3.client('sns')

# 2. Define Variables (YOU MUST CHANGE THESE TO MATCH YOUR AWS ACCOUNT)
bucket_name = 'dctsales--use1-az4--x-s3'  # <--- REPLACE THIS with your actual bucket name
source_folder = 'customer details/'
destination_folder = 'sr1/'
# The prefix we are looking for in the filenames (e.g., sr1_file.csv)
sr_prefix = 'sr1' 

# 3. Paste your SNS Topic ARN here (from the AWS Console > SNS)
topic_arn = 'arn:aws:sns:us-east-1:492267599260:demo1:b270f810-9462-4d8c-9678-4d9e47d06ed7' # <--- REPLACE THIS

# Flag to track if we actually moved anything
files_moved = False

# 4. Access the Bucket
bucket = s3.Bucket(bucket_name)

# 5. Loop through objects in the source folder
# We filter for files that are in the source folder AND start with the sr_prefix
for obj in bucket.objects.filter(Prefix=source_folder + sr_prefix):
    
    # Construct the full path for the new destination
    # This takes the filename (e.g., sr1_data.csv) and puts it in the destination folder
    destination_key = destination_folder + obj.key.split('/')[-1]
    
    # Define the source dictionary required by boto3
    copy_source = {
        'Bucket': bucket_name,
        'Key': obj.key
    }
    
    # 6. Copy the file to the new folder
    bucket.copy(copy_source, destination_key)
    
    # 7. Delete the old file from the source folder
    obj.delete()
    
    # Print what happened so we can see it in the terminal
    print(f"Moved file {obj.key} to {destination_key}")
    
    # Mark that we have successfully moved at least one file
    files_moved = True

# 8. Send Email Notification via SNS if files were moved
if files_moved:
    sns.publish(
        TopicArn=topic_arn,
        Message='Sales Rep 1, you have new files to validate in your folder.',
        Subject='New Files for Validation'
    )
    print("SNS Notification sent.")
else:
    print("No files found starting with 'sr1' to move.")