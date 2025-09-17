#loops 
# for condition:
#     code block

# name = "perry"
# for leter in name:
#     print(leter)

# list = ["cameroon", "usa", "china", "congo"]
# for country in list:
#     print(country)
# num = (1,3,7)
# for i in num:
#     print(i)
# for i in range(3):
#     print(i)
# for i in range(2,6):
#     print(i)
# for i in range(1,20,2):
#     print(i)

# student_scores = {"john":20, "mark": 70, "eva":80, "luke":90, "perry":50}
# for student, scores in student_scores.items():
#     if scores >= 80:
#         print(f"{student}: A")
#     elif scores >= 70 :
#         print(f"{student}: B")
#     elif scores >= 60 :
#         print(f" {student}: C")
#     elif scores >= 50 :
#         print(f" {student}: D")
#     else:
#         print(f"{student}: F")



# code generated on cloud9 while building resources 
import boto3 

# iam = boto3.client('iam')

# response = iam.list_users()
# for user in response["Users"]:
#     print(f'{user["UserName"]}')

# buckets = boto3.client('s3')
# response = buckets.list_buckets()
# for bucket in response['Buckets']:
#     print(f'{bucket["Name"]}')
    
# s3 = boto3.client('s3')
# existing_buckets = [bucket["Name"] for bucket in s3.list_buckets()["Buckets"]]
# # #print(existing_buckets)

# for bucket in existing_buckets:
#     if bucket == "perry-iam-demo":
#         print(bucket)

# s3 = boto3.client('s3')
# bucket_names = ["firsthfjfldhhd", "secondgdhdjsgdjf"]
# for bucket in bucket_names:
#     s3.delete_bucket(
#         Bucket = bucket)
#     print(f"{bucket} deleted")
#     if bucket  in existing_buckets:
#         print((f'{bucket} already exist'))
#     else:
#         s3.create_bucket(
#             Bucket = bucket)
#         print(f"bucket {bucket} created")
ec2 = boto3.client('ec2')
instance_name = ["web1", "web2"]
for name in instance_name:
    response = ec2_client.run_instances(
        imageId= ,
        MinCount =,
        MaxCount = ,
        KeyName = , 
        InstanceType = )
