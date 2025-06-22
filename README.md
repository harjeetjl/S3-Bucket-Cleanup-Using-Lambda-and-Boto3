# Automated S3 Bucket Cleanup with AWS Lambda and Boto3

This project implements an automated cleanup mechanism for Amazon S3 buckets using an AWS Lambda function. The function removes files older than 30 days, helping manage storage and maintain bucket hygiene.

---

## Overview

This solution uses a Python-based AWS Lambda function integrated with the Boto3 SDK. It scans a target S3 bucket, identifies files older than 30 days, and deletes them. This process can be triggered manually or scheduled using CloudWatch Events (EventBridge).

---

## Project Details

### Bucket Name
- `harjeet-s3-cleanup-bucket`

### Lambda Function
- **Name:** `S3CleanupFunction_harjeet`
- **Runtime:** Python 3.x
- **Trigger:** Manual or Scheduled (via EventBridge)
- **Code:** Scans the bucket, calculates object age, deletes objects older than 30 days, and logs results

### IAM Role
- **Name:** `harjeet_lambda_s3_cleanup_role`
- **Policy Attached:** `AmazonS3FullAccess`

---

## Tools & Technologies

- AWS S3  
- AWS Lambda  
- AWS IAM  
- Python 3.x  
- Boto3 SDK  

---

## Setup Instructions

### Step 1: Create S3 Bucket

1. Go to the S3 Console
2. Create a bucket named `harjeet-s3-cleanup-bucket`
3. Upload test files with varying last modified dates

### Step 2: Configure IAM Role

1. Create a new IAM role: `harjeet_lambda_s3_cleanup_role`
2. Attach the policy: `AmazonS3FullAccess`
3. Allow Lambda service to assume this role

### Step 3: Deploy Lambda Function

1. Create a Lambda function: `S3CleanupFunction_harjeet`
2. Choose Python 3.x as the runtime
3. Assign the IAM role created earlier
4. Paste the Python code into the Lambda editor
5. Deploy and test the function

**Reference Code:**  
[S3CleanupFunction_harjeet.py](https://github.com/harjeetjl/S3-Bucket-Cleanup-Using-Lambda-and-Boto3/blob/main/S3CleanupFunction_harjeet.py)

---

## Testing Process

- The function was manually invoked via the AWS Lambda console
- S3 bucket contents were validated before and after execution:
  - Files older than 30 days were removed
  - Files within the retention period remained intact

---

## Screenshots

Screenshots included in the repository:

- S3 bucket contents (before cleanup)
![image](https://github.com/user-attachments/assets/4b9f73f1-57af-4417-85a5-0a8be73dc46d)
![image](https://github.com/user-attachments/assets/05f55924-4006-4b49-b3b4-d39a0febeddc)

- IAM role setup and attached policy
![image](https://github.com/user-attachments/assets/9aa5f576-ecb5-4b40-bfb3-a2237c7b4bef)
 
- Lambda function configuration
![image](https://github.com/user-attachments/assets/113ee85f-7635-4255-81e4-0146269a5e32)

- Test run logs
![image](https://github.com/user-attachments/assets/9cede31d-70b2-4808-bf05-36ed6316e700)

- S3 bucket contents (after cleanup)  
![image](https://github.com/user-attachments/assets/3887513a-58b5-4041-a95d-69456e0ac971)

---
