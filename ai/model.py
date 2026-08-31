import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Training dataset
data = {
    "soil_type": ["Loamy", "Loamy", "Sandy", "Clay", "Loamy", "Sandy"],
    "ph": [6.5, 6.2, 6.8, 6.0, 6.7, 7.0],
    "nitrogen": [90, 80, 40, 70, 85, 35],
    "phosphorus": [45, 40, 25, 35, 42, 20],
    "potassium": [40, 35, 30, 45, 38, 25],
    "crop": ["Rice", "Rice", "Groundnut", "Maize", "Rice", "Groundnut"]
}

df = pd.DataFrame(data)

# Encode soil type
soil_mapping = {
    "Sandy": 0,
    "Loamy": 1,
    "Clay": 2
}

df["soil_encoded"] = df["soil_type"].map(soil_mapping)

# Features and target
X = df[
    ["soil_encoded", "ph", "nitrogen", "phosphorus", "potassium"]
]

y = df["crop"]

# Train Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)


def predict_crop(soil_type, ph, nitrogen, phosphorus, potassium):
    soil_encoded = soil_mapping.get(soil_type)

    if soil_encoded is None:
        return "Unknown soil type"

    input_data = pd.DataFrame([{
        "soil_encoded": soil_encoded,
        "ph": ph,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium
    }])

    prediction = model.predict(input_data)[0]

    return prediction


if __name__ == "__main__":
    result = predict_crop(
        "Loamy",
        6.5,
        90,
        45,
        40
    )

    print("AI Recommended Crop:", result)