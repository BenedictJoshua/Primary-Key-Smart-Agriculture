import os
import math

def load_csv_data(data_path="data/Crop_recommendation.csv"):
    """
    Manually parses the agricultural dataset using pure native Python.
    Scans multiple fallback paths to prevent directory routing errors.
    """
    base_dir = os.path.dirname(__file__)
    possible_paths = [
        data_path,
        os.path.join(base_dir, "data", "Crop_recommendation.csv"),
        os.path.join(base_dir, "Crop_recommendation.csv"),
        "data/Crop_recommendation.csv",
        "../data/Crop_recommendation.csv",
        "./data/Crop_recommendation.csv",
        "Crop_recommendation.csv",
    ]
    
    resolved_path = None
    for p in possible_paths:
        if os.path.exists(p):
            resolved_path = p
            break
            
    if resolved_path is None:
        raise FileNotFoundError(f"Error: Could not locate 'Crop_recommendation.csv' in any expected folders.")
        
    features = []
    labels = []
    
    with open(resolved_path, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise ValueError("The dataset file is empty.")
            
        header = [h.strip() for h in lines[0].strip().split(',')]
        
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            row = line.split(',')
            
            row_features = [float(val) for val in row[:-1]]
            row_label = row[-1].strip()
            
            features.append(row_features)
            labels.append(row_label)
            
    return features, labels, header[:-1]

def pseudo_shuffle_data(features, labels, seed=42):
    """
    Shuffles features and labels inline using a deterministic custom randomizer.
    This resolves sequential data bias without requiring the random library.
    """
    n = len(features)
    combined = list(zip(features, labels))
    
    for i in range(n - 1, 0, -1):
        seed = (1103515245 * seed + 12345) % (2**31)
        j = seed % (i + 1)
        combined[i], combined[j] = combined[j], combined[i]
        
    shuffled_features, shuffled_labels = zip(*combined)
    return list(shuffled_features), list(shuffled_labels)

def calculate_mean_and_std(features):
    """
    Computes column-wise means and standard deviations for Feature Scaling.
    """
    num_rows = len(features)
    num_cols = len(features[0]) if num_rows > 0 else 0
    
    means = [0.0] * num_cols
    stds = [0.0] * num_cols
    
    for row in features:
        for col in range(num_cols):
            means[col] += row[col]
    means = [m / num_rows for m in means]
    
    for row in features:
        for col in range(num_cols):
            stds[col] += (row[col] - means[col]) ** 2
    stds = [math.sqrt(s / num_rows) for s in stds]
    
    return means, stds

def scale_features(features, means, stds):
    """
    Applies Standard Scaling (Z-score normalization) to prevent feature scale bias.
    """
    scaled = []
    for row in features:
        scaled_row = []
        for col in range(len(row)):
            val = (row[col] - means[col]) / stds[col] if stds[col] != 0 else 0.0
            scaled_row.append(val)
        scaled.append(scaled_row)
    return scaled

def train_test_split_manual(features, labels, test_size=0.2):
    """
    Splits records manually into deterministic Train and Test sets.
    """
    split_idx = int(len(features) * (1.0 - test_size))
    return (
        features[:split_idx],  # X_train
        features[split_idx:],  # X_test
        labels[:split_idx],    # y_train
        labels[split_idx:]     # y_test
    )

class PurePythonKNN:
    """
    A robust, zero-dependency K-Nearest Neighbors Classifier.
    """
    def __init__(self, k=5):
        self.k = k
        self.X_train = []
        self.y_train = []
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        
    def _euclidean_distance(self, row1, row2):
        distance = 0.0
        for i in range(len(row1)):
            distance += (row1[i] - row2[i]) ** 2
        return math.sqrt(distance)
        
    def predict_single(self, sample_row):
        distances = []
        for i in range(len(self.X_train)):
            dist = self._euclidean_distance(sample_row, self.X_train[i])
            distances.append((dist, self.y_train[i]))
            
        distances.sort(key=lambda x: x)
        k_neighbors = [distances[i] for i in range(self.k)]
        
        votes = {}
        for dist, label in k_neighbors:
            votes[label] = votes.get(label, 0) + 1
            
        return max(votes, key=votes.get)

    def evaluate(self, X_test, y_test):
        correct = 0
        for i in range(len(X_test)):
            pred = self.predict_single(X_test[i])
            if pred == y_test[i]:
                correct += 1
        return correct / len(X_test)

if __name__ == "__main__":
    print("Initializing Custom Pure Python AI Processing Engine...")
    
    try:
        raw_X, raw_y, feature_names = load_csv_data()
        shuffled_X, shuffled_y = pseudo_shuffle_data(raw_X, raw_y)
        means, stds = calculate_mean_and_std(shuffled_X)
        scaled_X = scale_features(shuffled_X, means, stds)
        
        X_train, X_test, y_train, y_test = train_test_split_manual(scaled_X, shuffled_y)
        
        model = PurePythonKNN(k=5)
        model.fit(X_train, y_train)
        
        accuracy = model.evaluate(X_test, y_test)
        print(f"Dataset successfully parsed. Feature dimensions: {len(feature_names)}")
        print(f"Samples split - Training size: {len(X_train)}, Testing size: {len(X_test)}")
        print(f"Production Model Verification Accuracy: {accuracy * 100:.2f}%")
        
    except Exception as e:
        print(f"Execution failed: {e}")
