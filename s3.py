import boto3

s3 = boto3.client("s3", region_name="REGION")

bucket_name = "harsha-lambda-trigger-2026"

# s3.create_bucket(
#     Bucket=bucket_name,
#     CreateBucketConfiguration={
#         "LocationConstraint": "REGION"
#     }
# )
# print("Bucket created:", bucket_name)

s3.upload_file(
    "upload10.jpg",
    bucket_name,
    "upload10.jpg"
)


print("Image uploaded successfully")
