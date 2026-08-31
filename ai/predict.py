import sys
import json
from model import predict_crop

data = json.loads(sys.stdin.read())

result = predict_crop(
    data["soil_type"],
    float(data["ph"]),
    float(data["nitrogen"]),
    float(data["phosphorus"]),
    float(data["potassium"])
)

print(result)