# Failure Modes Reference

A catalog of common failure pathways to consider during Inversion Thinking.

## Categories

### 1. Input Attacks
- **Oversized Payload:** 10GB file upload crashes memory.
- **Malformed Input:** Invalid JSON/XML causes parser crash.
- **Boundary Values:** Empty strings, zero, MAX_INT, negative numbers.
- **Injection:** SQL, XSS, Command Injection via unsanitized input.

### 2. Authentication & Authorization
- **Privilege Escalation:** `?admin=true` in URL/body.
- **Broken Access Control:** User A accesses User B's data via ID enumeration.
- **Session Hijacking:** Predictable session tokens.
- **Missing Auth Check:** Endpoint skips authentication middleware.

### 3. State & Concurrency
- **Race Condition:** Two requests modify same resource simultaneously.
- **Deadlock:** Circular lock dependency halts system.
- **Stale Cache:** Cache returns outdated data after update.
- **Orphaned State:** Transaction fails mid-way, leaving partial data.

### 4. External Dependencies
- **Timeout:** External API takes 60s, your timeout is 30s.
- **Unavailability:** Database goes down, no retry/fallback.
- **Version Mismatch:** Dependency updates break API contract.
- **Rate Limiting:** External service returns 429, no backoff logic.

### 5. Resource Exhaustion
- **Memory Leak:** Objects never garbage collected.
- **Connection Pool Exhaustion:** All DB connections consumed.
- **Disk Full:** Logs/temp files fill storage.
- **Thread Starvation:** All threads blocked on I/O.

### 6. Infrastructure
- **Network Partition:** Service A cannot reach Service B.
- **Clock Skew:** Distributed timestamps become inconsistent.
- **DNS Failure:** Domain resolution fails.
- **Certificate Expiry:** HTTPS fails silently.

## Usage
When performing Inversion Thinking, scan this list and ask:
> "Which of these failure modes apply to my current design?"
