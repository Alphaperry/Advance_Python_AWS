# while loops

# counter = 1
# while counter <= 7:
#     print("how are you")
#     counter += 1

# user_name = input("enter your name: ")
# password = input("enter your password: ")
# coerrect_user_name = "perry"
# coerrect_password = "perry123"

# while user_name == coerrect_user_name and password == coerrect_password:
#     print("access granted")
#     if user_name != coerrect_user_name or password != coerrect_password:
#         print("access not granted")

# while True:
#     if user_name == coerrect_user_name and password == coerrect_password:
#         print("access granted")
#         break
#     else:
#         user_name = input("enter your name: ")
#         password = input("enter your password: ")

# counter = 0
# while counter <= 5:
#     counter += 1
#     while user_name == coerrect_user_name and password == coerrect_password:
#         print("access granted")
#         user_name = input("enter your name: ")
#         password = input("enter your password: ")

#     else:
#         print("access not granted")
#         user_name = input("enter your name: ")
#         password = input("enter your password: ")

# user_name = input("enter your name: ").lower()
# password = input("enter your password: ").lower()
# counter = 3
# while counter:
#     if user_name == "perry" and password == "perry123":
#         print('access granted')
#         break
#     else:
#         print("wrong credentials")
#         print(f"you have {counter} tries left")
#         user_name = input("enter your name: ").lower()
#         password = input("enter your password: ").lower()
#     counter -=1
# print("you don not have tries left")

# for num in range(1,11):
#     print(num)

# for num in range(1,11):
#     print(num)
#     if num == 5:
#         break

# for num in range(1,11):
#     if num == 3:
#         continue
#     print(num)

# for num in range(1,11):
#     if num == 3:
#         num +=3
#         print(num)
#     else:
#         print(num)

# count = 0 
# while count < 5:
#     if count == 3:
#         pass
#     else:
#         print(count)
#     count += 1

#code from cloud 9
import boto3
import time
ec2 = boto3.client('ec2')
instances = ec2.run_instances(
    ImageId = "ami-0360c520857e3138f",
    MinCount = 1,
    MaxCount = 1,
    InstanceType = "t2.micro")
instance_id = instances["Instances"][0]["InstanceId"]
print(f"new instance {instance_id}")
instance_id = "i-012f15e1322ce1268"
state = ""
while state != "running":
    response = ec2.describe_instances(InstanceIds = [instance_id])
    state = response["Reservations"][0]["Instances"][0]["State"]["Name"]
    print(f"the instance {instance_id} is {state}")
    print("sleeping for 6s")
    time.sleep(5)
    
    