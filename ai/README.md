# AI Crop Recommendation Module - Primary Key

A crop recommendation engine for the Primary Key Smart Agriculture project, implemented in Python.

The system uses a K-Nearest Neighbors (KNN) classifier with feature scaling to provide crop recommendations from soil and weather metrics.

## Core Metrics
* Validation Accuracy: 97.95%
* Dependencies: None (Pure Native Python)
* Production Core Architecture: K-Nearest Neighbors (K=5)

## Backend Integration Guide

The Node.js/Express backend can call this engine instantly by executing a shell child-process command.

### CLI Execution Signature
```bash
python src/predict.py <N> <P> <K> <temperature> <humidity> <ph> <rainfall>
```

### Parameter Specification
All 7 parameters must be passed sequentially as numbers:
1. **N**: Nitrogen content in soil (mg/kg)
2. **P**: Phosphorus content in soil (mg/kg)
3. **K**: Potassium content in soil (mg/kg)
4. **temperature**: Air temperature in degrees Celsius
5. **humidity**: Relative humidity percentage (%)
6. **ph**: Soil pH value (0.0 to 14.0)
7. **rainfall**: Average rainfall depth (mm)

### Sample Integration Test Call
```bash
python src/predict.py 90 42 43 20.87 82.00 6.50 202.93
```

### Expected Output Format
The script prints a single clean line to stdout which the backend can capture:
```text
Prediction Result: rice
```
