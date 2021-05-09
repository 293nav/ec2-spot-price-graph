# ec2-spot-price-graph
Python Script to generate graph based on the EC2 Spot Price History Data. 

### Description
A simple python script to generate a graph displaying the selected EC2 instance's spot price as percentage of is on-demand price for the provided time period.

### Setup
List of libraries used in the script
- boto3
- datetime
- pandas
- matplotlib
- sys

Install boto3, pandas and matplotlib

To use this script you need to have an active AWS account with access to CLI credentials of an IAM user with access to decribe-spot-price-history command.

Configure the AWS Credentials in your local machine using the shared credentials file method. The script will automatically pick up the credentials information from the shared credentials file.

Once you have installed all the required libraries and configured your AWS CLI credentials, you are good to use this script to generate spot price trend graphs

### Arguments to the Script
The script takes 5 arguments
1. Instance Type
2. On Demand Price
3. Product Description
4. Report Start Date
5. Report End Date

All the 5 arguements are mandatory.

### Examples
`python3 main.py m5.16xlarge 3.072 "Linux/UNIX" "2021-03-09" "2021-05-10"`
