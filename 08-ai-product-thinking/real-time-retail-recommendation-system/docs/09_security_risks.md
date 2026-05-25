# 09 - Security Risks

## Overview

This system processes real-time user events and recommendation data. Even in MVP form, several security risks exist.

---

## 1. API Exposure Risks

### Risk
- Open REST endpoints (`/event`, `/recommendations`)
- No authentication layer

### Impact
- Fake event injection
- Manipulation of recommendation system

### Mitigation
- Add API authentication (JWT/API keys)
- Rate limiting per user

---

## 2. WebSocket Hijacking

### Risk
- Unauthorized clients connecting to `/ws`

### Impact
- Data leakage
- Real-time stream abuse

### Mitigation
- WebSocket token validation
- Origin checks

---

## 3. Event Injection Attacks

### Risk
- Malicious users sending fake events (spam clicks)

### Impact
- Skewed user profile
- Bad recommendations

### Mitigation
- Event validation layer
- anomaly detection (future)

---

## 4. Data Integrity Risks

### Risk
- Session data tampering
- inconsistent state updates

### Mitigation
- server-side authoritative state
- immutable event logs (future Kafka model)

---

## 5. Denial of Service (DoS)

### Risk
- high-frequency event simulation

### Impact
- memory overload (session_store grows)

### Mitigation
- rate limiting
- session TTL cleanup

---

## Summary

Security in MVP is minimal but designed to evolve toward production-grade controls.
