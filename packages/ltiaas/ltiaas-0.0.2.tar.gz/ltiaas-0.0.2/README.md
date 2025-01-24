# LTIAAS SDK

```python
from ltiaas import LTIAASLaunch, LineItem

client = LTIAASLaunch(
    domain="admin-us.ltiaas.com",
    api_key="-------------------",
    ltik="----------------------",
)

print(client.get_id_token())

print(client.get_memberhips())

print(client.get_line_items())

lineitem = LineItem(label="Created with the SDK", score_maximum=100, tag="sdk")
print(client.create_line_item(lineitem=lineitem))
```