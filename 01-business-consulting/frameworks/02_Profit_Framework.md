## 02 - Profit Framework

#### Profit = (Revenue - Cost)

### Diagram 1: Top-Level Overview (1 Level Deep)
Layer 1: What is happening?

```mermaid
flowchart TD
    Profit[Profit] --> Revenue[Revenue]
    Profit --> Costs[Costs]

    Revenue --> Price[Price]
    Revenue --> Quantity[Quantity]

    Costs --> Fixed[Fixed Costs]
    Costs --> Variable[Variable Costs]
```

### Diagram 2: Expanded View (2nd Level)
Layer 2: Why it is happening?

---
#### Deep dive into Revenue drivers

## 1️⃣ Revenue -> Price

```mermaid
flowchart TD
    Price[Price] --> Internal[Internal]
    Price --> External[External]

```
---

## 2️⃣ Revenue -> Quantity

```mermaid
flowchart TD
    Quantity[Quantity] --> Customer[Customer]
    Quantity[Quantity] --> Competitors[Competitors]
    Quantity[Quantity] --> MarketTrends[MarketTrends]
    Quantity[Quantity] --> Company[Company]

```

---
#### Deep dive into Cost drivers

## 1️⃣ Cost -> Fixed

```mermaid
flowchart TD
    Cost[Cost] --> FixedCost[FixedCost]
    Cost[Cost] --> VariableCost[VariableCost]

    FixedCost[FixedCost] --> Capacity[Capacity]
    
    VariableCost[VariableCost] --> Inputs[Inputs]
    VariableCost[VariableCost] --> Efficiency[Efficiency]
    VariableCost[VariableCost] --> Scale[Scale]
    VariableCost[VariableCost] --> External[External]

```
---

