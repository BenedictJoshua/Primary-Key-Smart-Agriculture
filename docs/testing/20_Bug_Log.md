# Bug Log

## Project Information

**Project:** Smart Agriculture Intelligence Portal with AI Assistance

**Team:** Primary Key

**Prepared By:** Quality Assurance Engineer

**Date:** August 2026

---

# Summary

| Bug ID | Module | Severity | Status |
|--------|--------|----------|--------|
| BUG-AI-001 | AI Prediction | Medium | Open |
| BUG-AI-002 | AI Prediction | High | Open |
| BUG-AI-003 | AI Prediction | Medium | Open |
| BUG-AI-004 | AI Prediction | Medium | Open |
| BUG-CB-001 | AI Chatbot | Low | Open |
| BUG-CB-002 | AI Chatbot | Medium | Open |
| BUG-CB-003 | AI Chatbot | Low | Open |

---

# BUG-AI-001

**Title:** Incorrect README Execution Command

**Module:** AI Prediction

**Severity:** Medium

**Priority:** Medium

### Description

The README instructs users to execute:

```bash
python src/predict.py
```

However, the actual file is located at:

```bash
python predict.py
```

### Expected Result

README should provide the correct execution command.

### Actual Result

Execution fails with:

```
No such file or directory
```

**Status:** Open

---

# BUG-AI-002

**Title:** Negative Input Values Accepted

**Module:** AI Prediction

**Severity:** High

### Steps

```
python predict.py -1 -1 -1 -10 -20 -5 -100
```

### Expected

Application should reject invalid agricultural values.

### Actual

```
Prediction Result: mothbeans
```

**Status:** Open

---

# BUG-AI-003

**Title:** Extreme Input Values Accepted

**Module:** AI Prediction

**Severity:** Medium

### Steps

```
python predict.py 9999 9999 9999 9999 9999 9999 9999
```

### Expected

Display validation error.

### Actual

```
Prediction Result: mothbeans
```

**Status:** Open

---

# BUG-AI-004

**Title:** Internal Exception Displayed

**Module:** AI Prediction

**Severity:** Medium

### Steps

```
python predict.py abc 42 43 20.8 82 6.5 202
```

### Expected

Friendly validation message.

### Actual

```
could not convert string to float
```

**Status:** Open

---

# BUG-CB-001

**Title:** AI Fallback Not Configured

**Module:** AI Chatbot

**Severity:** Low

### Description

HF_API_TOKEN is not configured.

### Actual

```
HF_API_TOKEN is not set
```

**Status:** Open

---

# BUG-CB-002

**Title:** Weather Questions Unsupported

**Severity:** Medium

### Example

```
Does it rain today?
```

### Actual

```
AI fallback isn't configured.
```

**Status:** Open

---

# BUG-CB-003

**Title:** General Knowledge Questions Unsupported

**Severity:** Low

### Example

```
Who is the Prime Minister of India?
```

### Actual

```
AI fallback isn't configured.
```

**Status:** Open