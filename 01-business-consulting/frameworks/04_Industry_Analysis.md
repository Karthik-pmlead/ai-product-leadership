# Industry Analysis Framework

This framework provides a structured approach to **analyzing an industry**, covering market dynamics, competition, structure, economics, and external factors, with a focus on **future outlook**.

---

## Framework Overview

The analysis is broken down into five key components:

1. **Market Dynamics** – Understand current market and future trends  
2. **Industry Structure** – Identify key players, suppliers, buyers, and future shifts  
3. **Competition** – Assess rivalry, potential entrants, and substitutes  
4. **Economics** – Evaluate cost structures, margins, and pricing power  
5. **External Factors** – Consider regulation, economy, and technology  

---

### How to Use
 - Start top-down: Market Dynamics → Industry Structure → Economics → External factors
 - Include future outlook to anticipate opportunities and threats
 - Apply MECE logic for all categories
 - Identify high-impact areas for strategic decisions

## Industry Analysis

```mermaid
flowchart LR
    Industry[Industry Analysis] --> MarketDynamics[Market Dynamics]
    Industry --> IndustryStructure[Industry Structure]
    Industry --> Competition[Competition]
    Industry --> Economics[Economics]
    Industry --> External[External Factors]

    %% Market Dynamics
    MarketDynamics --> Current[Current: size, growth, segments]
    MarketDynamics --> Future[Future: trends, outlook]

    %% Future Market Outlook
    Future --> PlayerMovement[Players Entering / Exiting]
    Future --> M&A[Mergers & Acquisitions]
    Future --> Barriers[Barriers to Entry / Exit]

    %% Industry Structure
    IndustryStructure --> Competitors[Competitors]
    IndustryStructure --> Suppliers[Suppliers]
    IndustryStructure --> Buyers[Buyers]

    %% Competition
    Competition --> Rivalry[Rivalry]
    Competition --> NewEntrants[New Entrants]
    Competition --> Substitutes[Substitutes]

    %% Economics
    Economics --> CostStructure[Cost Structure]
    Economics --> Margins[Margins / Pricing Power]

    %% External Factors
    External --> Regulation[Regulation]
    External --> Economy[Economy: interest rates, inflation]
    External --> Technology[Technology]
