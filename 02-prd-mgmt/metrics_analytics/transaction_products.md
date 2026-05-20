# Transaction Metrics

## Overview

Transaction products focus on users completing valuable actions such as purchases, bookings, payments, or orders. These metrics help measure how efficiently intent turns into completed transactions [web:235][web:238][web:242].

## Core metrics

| Metric | What it measures | Why it matters | Notes |
|---|---|---|---|
| Conversion Rate | Percentage of users who complete a transaction. | Core transaction efficiency. | Critical in checkout and payment flows. |
| Funnel Conversion | Progress through transaction steps. | Shows where users advance or drop. | Track by step and cohort. |
| Funnel Drop-off Rate | Percentage of users lost at each step. | Identifies friction. | Very useful in checkout flows. |
| Checkout Completion Rate | Percentage of users who begin checkout and complete purchase. | Shows how well the checkout works. | Also called checkout conversion rate [web:238][web:239]. |
| Checkout Abandonment Rate | Percentage of users who start checkout but do not finish. | Reveals purchase friction. | One of the most important e-commerce metrics [web:235][web:238]. |
| Cart Abandonment Rate | Percentage of users who add items to cart but do not buy. | Measures purchase hesitation. | Distinct from checkout abandonment. |
| Payment Success Rate | Successful payments divided by attempted payments. | Transaction reliability. | Important for fintech and commerce [web:242]. |
| Payment Failure Rate | Failed payment attempts. | Detects technical or trust issues. | Track by payment method. |
| Authorization Rate | Card, UPI, or bank authorization success. | Payment approval quality. | Important in payment systems. |
| Order Success Rate | Orders successfully placed and confirmed. | Transaction integrity. | Useful in commerce and delivery. |
| Refund Rate | Percentage of transactions refunded. | Quality and trust signal. | Watch by product and cohort. |
| Chargeback Rate | Disputed transactions over total transactions. | Fraud and risk control. | Critical for payments. |
| Average Order Value (AOV) | Average value of a completed order. | Monetization per transaction. | Strong e-commerce metric. |
| GMV | Gross merchandise value. | Total transaction volume. | Useful for marketplaces. |
| Take Rate | Platform revenue as a percentage of GMV. | Marketplace monetization. | Common in platform businesses. |
| Net Revenue | Revenue after refunds, discounts, and fees. | True business performance. | Better than gross in many cases. |
| Revenue per Transaction | Average revenue per completed transaction. | Monetization efficiency. | Useful in commerce and fintech. |
| Transaction Volume | Number of completed transactions. | Throughput measure. | Important for payments and commerce. |
| Transaction Frequency | How often users transact. | Repeat usage. | Good indicator of habit. |
| Repeat Purchase Rate | Percentage of users who buy again. | Loyalty and retention. | Strong for commerce. |
| Time to Complete Transaction | Time from intent to completion. | Speed and UX. | Lower is better. |
| Drop-off by Step | Users lost at each step. | Funnel diagnosis. | Essential for PRD analysis. |
| Failed Transaction Recovery Rate | Successful recovery after failure. | Trust and resilience. | Great metric for payments. |
| Settlement Time | Time to settle funds or orders. | Operational efficiency. | Important in fintech and logistics. |
| Dispute Resolution Time | Time to resolve transaction disputes. | Support and trust. | Affects satisfaction. |
| Fraud Rate | Fraudulent transactions as a share of total. | Risk control. | Critical for payments. |

## Use cases

| Product type | Most relevant metrics |
|---|---|
| E-commerce | Checkout Completion Rate, Cart Abandonment Rate, AOV, Refund Rate |
| Payments | Payment Success Rate, Authorization Rate, Fraud Rate, Chargeback Rate |
| Marketplace | GMV, Take Rate, Transaction Volume, Repeat Purchase Rate |
| Booking / travel | Funnel Conversion, Checkout Abandonment Rate, Time to Complete Transaction |

## Practical tips

| Tip | Why it helps |
|---|---|
| Track each step of the funnel | Helps isolate where users drop off. |
| Separate cart abandonment from checkout abandonment | They measure different friction points. |
| Break metrics by channel and device | Mobile and web behavior can differ. |
| Pair conversion with speed and failure metrics | Conversion alone can hide broken experiences. |

## Interview use

In 
