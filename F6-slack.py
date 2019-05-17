import os
from slackclient import SlackClient


sc = SlackClient('XXX')

sc.api_call(
  "chat.postMessage",
  channel="#etl_Chris",
  as_user="true",
  text="ETL Success"
)



