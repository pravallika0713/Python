import boto3

# Create an S3 client
s3 = boto3.client('s3')

def create_s3():
# Bucket name (replace with your desired bucket name)
    bucket_name = 'second-bucket-pravs'

    # Create bucket
    try:
        response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
                    'LocationConstraint': 'ca-central-1'
                })
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

#Upload a file to the S3 bucket.
def upload_files_s3():

    try:
        s3.upload_file('example.txt','second-bucket-pravs','example.txt')
        print("uploaded successfully")
    except Exception as e:
        print(f"Error is {e}")

#List objects in the S3 bucket.
def list_s3():

    try:
        response = s3.list_objects(Bucket='second-bucket-pravs')
        s3_obj_list =[ Content['Key'] for Content in response['Contents']]
        return(s3_obj_list)
    except Exception as e:
        print(f"Error is {e}")
#Download an object from the S3 bucket

def downlad_obj_s3():
    obj_list= list_s3()
    for obj in obj_list:
        with open('obj', 'wb') as data:
            s3.download_fileobj('second-bucket-pravs', obj, data)

    print(obj)

#Delete an object from the S3 bucket.
def delete_obj_s3():
    obj_list= list_s3()
    for obj in obj_list:
        s3.delete_object(
    Bucket='second-bucket-pravs',
    Key=obj)
    print("deleted successfully")
        
#delete_obj_s3()

def delete_buckets():
    response = s3.list_buckets()
    bucket_list = [bucket['Name'] for bucket in response['Buckets']]
    for item in bucket_list:
        s3.delete_bucket(Bucket=item)
        print(f"deleted {item} successfully")

#delete_buckets()


#list_s3()
#downlad_obj_s3()