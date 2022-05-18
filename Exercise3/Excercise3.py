
from pytz import common_timezones, all_timezones
import pandas as pd
import datetime
import pytz
from datetime import timezone, datetime

#Create a schema object to consider the responseCode as integer value.
schema={
    "responseCode": int
}
#Read the CSV file.
gen = pd.read_csv("Jmeter_log1.jtl", dtype=schema, chunksize=10000000)
#Create a dataframe with filtering data with responseCode != 200
df = pd.concat((x.query("`responseCode` != 200") for x in gen), ignore_index=True)


# only considering the first 10 characters.
df['timeStamp'] = df['timeStamp'].astype(str).str[:10]
df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')

# Convert the time to a timezone-aware datetime object
df['timeStamp'] = df['timeStamp'].dt.tz_localize(timezone.utc)

# Convert the time from UTC to Pacific.
my_timezone = pytz.timezone('US/Pacific')
df['timeStamp'] = df['timeStamp'].dt.tz_convert(my_timezone)

#Create another dataframe with the required columns
outputdataframe = df[["timeStamp", "label", "responseCode", "responseMessage", "failureMessage"]]
print (outputdataframe)


# Create a for loop to read through another file  #Pending.