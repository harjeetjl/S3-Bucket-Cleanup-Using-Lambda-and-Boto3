import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    bucket_name = 'prashant-batch10'
    s3_client = boto3.client('s3')
    
    retention_period = timedelta(days=30)
    current_time = datetime.now(timezone.utc)
    
    deleted_objects = []
    retained_objects = []
    scanned_objects = []

    print(f"Starting cleanup process in bucket: {bucket_name}")

    paginator = s3_client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)

    for page in page_iterator:
        if 'Contents' not in page:
            continue

        for obj in page['Contents']:
            key = obj['Key']
            last_modified = obj['LastModified']
            file_age = current_time - last_modified

            scanned_objects.append(f"{key} (LastModified: {last_modified}, Age: {file_age.days} days)")

            if file_age > retention_period:
                try:
                    s3_client.delete_object(Bucket=bucket_name, Key=key)
                    deleted_objects.append(key)
                    print(f"Deleted: {key} (Age: {file_age.days} days)")
                except Exception as e:
                    print(f"Error deleting {key}: {e}")
            else:
                retained_objects.append(key)
                print(f"Retained: {key} (Age: {file_age.days} days)")

    summary = {
        'statusCode': 200,
        'body': {
            'total_files_scanned': len(scanned_objects),
            'files_deleted': deleted_objects,
            'files_retained': retained_objects
        }
    }

    print("Cleanup completed.")
    return summary
