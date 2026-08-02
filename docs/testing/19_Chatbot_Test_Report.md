# Chatbot Test Report

## Module

AI Smart Agriculture Chatbot

---

## Test Cases

| Scenario | Status |
|----------|--------|
| Greeting | ✅ Pass |
| Identity | ✅ Pass |
| Crop Recommendation | ✅ Pass |
| Agriculture Questions | ✅ Pass |
| Date | ✅ Pass |
| Time | ✅ Pass |
| Special Characters | ✅ Pass |
| Numeric Input | ✅ Pass |
| Weather Questions | ❌ Fail |
| General Knowledge Questions | ❌ Fail |

---

## Bugs Found

- BUG-CB-001
- BUG-CB-002
- BUG-CB-003

---

## QA Conclusion

The chatbot performs effectively for agriculture-related queries and crop recommendations. General-purpose AI responses are unavailable because the Hugging Face API fallback is not configured. This limits the chatbot's ability to answer weather and general knowledge questions.