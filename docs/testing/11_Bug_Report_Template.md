# Bug Report Template

---

## Document Information

| Item | Details |
|------|---------|
| **Project Name** | Smart Agriculture Intelligence Portal with AI Assistance |
| **Team Name** | Primary Key |
| **Document** | Bug Report Template |
| **Version** | 1.0 |
| **Prepared By** | Quality Assurance Engineer |
| **Status** | Active Template |
| **Date** | August 2026 |

---

# 1. Purpose

This document provides a standardized template for reporting, tracking, and resolving software defects identified during testing. It ensures that every defect is documented consistently, making it easier for developers to reproduce, fix, and verify issues.

---

# 2. Bug Severity Levels

| Severity | Description |
|----------|-------------|
| Critical | Application crash, data loss, security vulnerability, or major system failure. |
| High | Core functionality fails with no available workaround. |
| Medium | Feature functions incorrectly, but a workaround exists. |
| Low | Minor UI, formatting, spelling, or cosmetic issue. |

---

# 3. Bug Priority Levels

| Priority | Description |
|----------|-------------|
| P1 - Critical | Fix immediately before further testing. |
| P2 - High | Fix in the current development sprint. |
| P3 - Medium | Fix in the next planned sprint. |
| P4 - Low | Fix if time permits before release. |

---

# 4. Bug Status Workflow

```
New
 ↓
Assigned
 ↓
In Progress
 ↓
Fixed
 ↓
Ready for Retest
 ↓
Closed
```

If the issue still exists after retesting:

```
Reopened
 ↓
Assigned
 ↓
Fixed
 ↓
Closed
```

---

# 5. Bug Report Format

| Field | Description |
|--------|-------------|
| Bug ID | Unique identifier (e.g., BUG001) |
| Module | Module where the issue was found |
| Reported By | QA Engineer |
| Assigned To | Responsible Developer |
| Date Reported | Date defect was identified |
| Severity | Critical / High / Medium / Low |
| Priority | P1 / P2 / P3 / P4 |
| Status | New / Assigned / In Progress / Fixed / Retest / Closed |
| Environment | Browser, OS, Device |
| Description | Summary of the issue |
| Preconditions | Required conditions before testing |
| Steps to Reproduce | Step-by-step process |
| Expected Result | Expected system behavior |
| Actual Result | Actual system behavior |
| Attachments | Screenshots, logs, videos (if available) |
| Remarks | Additional observations |

---

# 6. Sample Bug Report

| Field | Example |
|--------|---------|
| Bug ID | BUG001 |
| Module | User Authentication |
| Reported By | Quality Assurance Engineer |
| Assigned To | Backend Developer |
| Date Reported | 15-Aug-2026 |
| Severity | High |
| Priority | P1 |
| Status | New |
| Environment | Chrome 139, Windows 11 |
| Description | User cannot log in with valid credentials. |
| Preconditions | User account already exists. |
| Steps to Reproduce | 1. Open Login Page<br>2. Enter valid email and password<br>3. Click **Login** |
| Expected Result | User should be redirected to the dashboard. |
| Actual Result | "Invalid Credentials" message is displayed. |
| Attachments | Screenshot (to be attached during execution) |
| Remarks | Requires backend authentication review. |

---

# 7. Defect Summary Table

| Bug ID | Module | Severity | Priority | Status | Assigned To |
|---------|--------|----------|----------|--------|-------------|
| BUG001 | Authentication | High | P1 | Sample | Backend Developer |

> **Note:** This table will be updated continuously during testing.

---

# 8. Best Practices

- Report one defect per bug report.
- Use clear and reproducible steps.
- Include screenshots or logs whenever possible.
- Assign the defect to the correct module owner.
- Verify fixes before closing the bug.
- Update the status promptly after each review.

---

## Document Revision History

| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 1.0 | August 2026 | Initial Bug Report Template | Quality Assurance Engineer |