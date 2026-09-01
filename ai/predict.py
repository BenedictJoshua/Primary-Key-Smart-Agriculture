import sys
import json
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# Training data
data = pd.DataFrame([
    {
        "soil_type": "Loamy",
        "ph": 6.5,
        "nitrogen": 90,
        "phosphorus": 45,
        "potassium": 40,
        "crop": "Rice",
    },
    {
        "soil_type": "Loamy",
        "ph": 6.0,
        "nitrogen": 80,
        "phosphorus": 40,
        "potassium": 35,
        "crop": "Rice",
    },
    {
        "soil_type": "Sandy",
        "ph": 6.8,
        "nitrogen": 60,
        "phosphorus": 30,
        "potassium": 50,
        "crop": "Groundnut",
    },
    {
        "soil_type": "Sandy",
        "ph": 7.0,
        "nitrogen": 55,
        "phosphorus": 35,
        "potassium": 45,
        "crop": "Groundnut",
    },
    {
        "soil_type": "Loamy",
        "ph": 6.2,
        "nitrogen": 70,
        "phosphorus": 50,
        "potassium": 40,
        "crop": "Maize",
    },
    {
        "soil_type": "Loamy",
        "ph": 6.7,
        "nitrogen": 75,
        "phosphorus": 45,
        "potassium": 45,
        "crop": "Maize",
    },
])


soil_mapping = {
    "Sandy": 0,
    "Loamy": 1,
    "Black": 2,
    "Red": 3,
    "Alluvial": 4,
}


data["soil_encoded"] = data["soil_type"].map(soil_mapping)

features = [
    "soil_encoded",
    "ph",
    "nitrogen",
    "phosphorus",
    "potassium",
]

X = data[features]
y = data["crop"]


# Train Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)


def predict_crop(input_data):
    soil_type = input_data.get("soil_type")
    ph = float(input_data.get("ph", 0))
    nitrogen = float(input_data.get("nitrogen", 0))
    phosphorus = float(input_data.get("phosphorus", 0))
    potassium = float(input_data.get("potassium", 0))

    soil_encoded = soil_mapping.get(soil_type, 1)

    input_df = pd.DataFrame([{
        "soil_encoded": soil_encoded,
        "ph": ph,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
    }])

    return model.predict(input_df)[0]


if __name__ == "__main__":
    try:
        input_data = json.load(sys.stdin)

        prediction = predict_crop(input_data)

        print(prediction)

    except Exception as error:
        print(f"Error: {error}")