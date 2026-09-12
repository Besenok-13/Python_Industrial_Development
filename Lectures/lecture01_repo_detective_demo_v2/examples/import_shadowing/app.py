import importlib.util
import requests
print("requests module:", requests)
print("requests.__file__:", getattr(requests, "__file__", None))
print("find_spec:", importlib.util.find_spec("requests").origin)
print("VALUE:", getattr(requests, "VALUE", "<real requests has no VALUE>"))
print(requests.VALUE)

