import boto3
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import sys

session = boto3.Session(profile_name='<AWS-PROFILE-NAME>')
ec2Client = boto3.client('ec2')

instance_type = sys.argv[1]
on_demand_price = sys.argv[2]
product_description = sys.argv[3]
start_time = sys.argv[4]
end_time = sys.argv[5]

start_year, start_month, start_date = map(int, start_time.split('-'))
end_year, end_month, end_date = map(int, end_time.split('-'))

spotPriceResponse = ec2Client.describe_spot_price_history(
    InstanceTypes=[instance_type],
    StartTime=datetime(start_year, start_month, start_date),
    EndTime=datetime(end_year, end_month, end_date),
    ProductDescriptions=[product_description]
)

spotPriceData = spotPriceResponse["SpotPriceHistory"]
spot_price_cleaned_data = []

for item in spotPriceData:
    temp_dict = {}
    temp_dict.update({"spot_price" : item["SpotPrice"]})
    temp_dict.update({"cost_percentage" : float(item["SpotPrice"])/float(on_demand_price) * 100})
    temp_dict.update({"availability_zone" : item["AvailabilityZone"]})
    temp_dict.update({"timestamp" : item["Timestamp"]})
    spot_price_cleaned_data.append(temp_dict)

spot_price_df = pd.DataFrame(spot_price_cleaned_data)

availability_zone_list = spot_price_df.availability_zone.unique()

fig,ax = plt.subplots()

for az in availability_zone_list:
    temp_df = spot_price_df.query('availability_zone=="' + az + '"')
    #temp_df.plot(x='timestamp', y='cost_percentage', kind='line')
    #plt.show()
    ax.plot(temp_df.timestamp, temp_df.cost_percentage, label=az)

fig.suptitle("Spot Price Trend - Instance : " + instance_type + " | Period : " + str(start_time) + " to " + str(end_time), fontsize=13)
ax.set_xlabel("Timestamp")
ax.set_ylabel("Spot Price as Percentage of On-Demand Price")
ax.legend(loc='best')
plt.show()
