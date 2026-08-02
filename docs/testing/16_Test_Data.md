# Test Data Document

---

## Document Information

| Item | Details |
|------|---------|
| **Project Name** | Smart Agriculture Intelligence Portal with AI Assistance |
| **Team Name** | Primary Key |
| **Document** | Test Data |
| **Version** | 1.0 |
| **Prepared By** | Quality Assurance Engineer |
| **Status** | Draft |
| **Date** | August 2026 |

---

# 1. Purpose

This document defines the sample data that will be used during functional, API, database, AI, chatbot, and integration testing.

---

# 2. User Test Data

| Test User | Email | Password | Role |
|-----------|-------|----------|------|
| Farmer 1 | farmer1@test.com | Farmer@123 | Farmer |
| Farmer 2 | farmer2@test.com | Farmer@123 | Farmer |
| Admin | admin@test.com | Admin@123 | Administrator |

---

# 3. Crop Test Data

| Crop | Soil Type | Season | Water Requirement |
|------|-----------|--------|-------------------|
| Rice | Clay | Kharif | High |
| Wheat | Loamy | Rabi | Medium |
| Maize | Sandy Loam | Kharif | Medium |
| Cotton | Black Soil | Kharif | Medium |
| Groundnut | Sandy | Summer | Low |

---

# 4. Weather Test Data

| Temperature | Humidity | Rainfall | Expected Condition |
|-------------|----------|----------|--------------------|
| 28°C | 70% | 50 mm | Suitable for Rice |
| 35°C | 45% | 0 mm | Dry Climate |
| 22°C | 85% | 90 mm | Heavy Rain |

---

# 5. Market Price Test Data

| Crop | Price (₹/Quintal) |
|------|------------------:|
| Rice | 2400 |
| Wheat | 2250 |
| Maize | 2100 |
| Cotton | 6500 |
| Groundnut | 5800 |

---

# 6. AI Recommendation Inputs

| Soil | Season | Temperature | Expected Output |
|------|--------|-------------|-----------------|
| Clay | Kharif | 28°C | Rice |
| Loamy | Rabi | 20°C | Wheat |
| Sandy | Summer | 34°C | Groundnut |

---

# 7. Chatbot Test Prompts

| Prompt | Expected Behaviour |
|--------|--------------------|
| Which crop is best for clay soil? | Recommend Rice |
| What is today's weather? | Return weather details |
| Show market price of wheat | Display wheat prices |
| How can I improve soil fertility? | Provide agricultural guidance |
| Hello | Greeting response |
| asdf123## | Gracefully handle invalid input |

---

# 8. Invalid Test Data

| Scenario | Expected Result |
|----------|-----------------|
| Empty username | Validation message |
| Empty password | Validation message |
| Invalid email | Reject input |
| SQL Injection attempt | Reject request |
| Extremely long text | Handle safely |

---

## Document Revision History

| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 1.0 | August 2026 | Initial Test Data Document | Quality Assurance Engineer |