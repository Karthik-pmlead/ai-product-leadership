# Security Risks

## 1. Data Exposure Risk
- Webcam streams could be intercepted if deployed insecurely

## 2. WebRTC Signaling Risks
- Offer/answer endpoints vulnerable without authentication

## 3. Input Spoofing
- Video replay attacks could simulate alert conditions

## 4. Model Manipulation
- If ML models are added later, adversarial inputs could degrade performance

## 5. Mitigations
- HTTPS + secure WebRTC (DTLS-SRTP)
- Auth layer for signaling server (future)
- No persistent storage of raw video
