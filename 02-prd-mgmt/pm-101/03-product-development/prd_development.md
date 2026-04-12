#### Topics
1. Influencing without authority
2. Development methodologies, tools and processes
3. User stories and non user requirements
4. Managing backlogs and stakeholder expectations

### Influence without Authority
**5Cs**
1. Company
2. Competitors
3. Customer
4. Channels
5. Costs

**4Ps**
1. Product
2. Place
3. Price
4. Promotion

### Know the company
- **Mission**
    - Amazon's mission is to be Earth's most customer-centric company. 

- **Vision**
    - Amazon’s vision is to build a place where customers can find and discover anything they want to buy online, with a focus on selection, price, and convenience.

- **Strategy**
    - Strategy = Goal + Direction + Choices
    - Strategy → Big picture direction
    - Plan → Steps to execute strategy
    - Tactics → Specific actions
      - Eg
        - Goal → Reach destination
        - Strategy → Take the fastest highway route
        - Tactics → Drive, refuel, follow GPS

**Mission Statement:** Describe your business' current purpose
**Vision Statement:** This represents your business' desired future and what you look like when you are ultimately successful.

- Dive deep into understanding
    - who the target customers are,
    - customer's unmet needs
    - competitors
    - create value
    - how company grows

- How is product launched, sold, revenue generated, success measured

### Know the market
- **Segmentation**
    - demographic, behavioral, need based
- market size
- market growth
- Identify potential adjacent market

- Define target customer using segmentation techniques
- Understand the trends, evolving market and growth

### Know the product
- **Test the product**
- How is the product performing
- This will help to better understand the features, and roadmap
- Form opinions based on product working knowledge and data

#### Build Trust
- Building relationships takes time
- Know the team, peers
- Have open communication, foster collaboration
- Learn how the teams communicate, get things done
- What is the impact of solving the problem on product strategy and goals

#### Storytelling
- Make it engaging for the
- audience to believe in the problem,
- the proposed solution and
- impact of solving it

**DACI matrix**
- Driver - Move the project forward
- Approver - Final say on the product (Architect)
- Contributor - Expertise
- Informed - Stay updated on the progress

### Methodologies
1. Waterfall
2. Agile - Respond to evolving customer needs
3. Kanban - Visualize the progress of work. Limit the # of work items

#### Agile
- **Scrum:** Defined set of guidelines that different team members need to perform
- **Dynamics:** Communication between development team and product managers
- **Tools:** Project management tool to capture requirements
- **version control:** GitHub
- **Deployment:** GitActions/Jenkins
  
**Scrum Image**


#### Crafting user stories (requirements)
- User story is a short and concise feature description written from user perspective.
    - As a [type of user], I want [goal] so that [benefit].
    - Eg: As a shopper, I want to filter products by price range so that I can quickly find items within my budget.
    - As a student, I want to track my course progress so that I know how much I’ve completed and what remains.

- **INVEST**
    - Independent - Not dependent on another story
    - Negotiable - 
    - Valuable - Provides value to customer
    - Estimated - work can be estimated
    - Small - tested by scrum team

    - Eg: As a shopper, I want to filter products by price range so that I can quickly find items within my budget.
        - Independent: Can be built separately from search or sorting
        - Negotiable: UI/UX (slider, dropdown) can vary
        - Valuable: Saves time and improves shopping experience
        - Estimable: Straightforward logic and UI
        - Small: Focuses only on price filtering
        - Testable: Check if filtering returns correct results

#### Acceptance Criteria
- Acceptance Criteria:
    - User can select a minimum and maximum price
    - Products displayed fall within the selected range
    - Filter updates results instantly or on apply
    - If no products match, a “No results found” message is shown
    - Filter can be cleared/reset

5. Phase gate

### Non user stories
- These a items that don’t directly describe user value but are still important, and they focus on technical, operational, or supporting work rather than user-facing functionality.
- Performance: Response time, latency
- Scalability: Scale up/down
- Reliability and disaster recovery
- Browser compatibility

#### Framework to prioritize backlog for sprint planning
- What work items should a sprint contain?
    - 5% -> High priority - App crash
    - 75% -> Metric movers - Roadmap features
    - 10% -> stakeholder requests - address tech debt
    - 10% -> Customer delights

#### RICE
   - Reach
   - Impact
   - Confidence
   - Effort

**Feature: Password reset via email**
   - Reach: 500 users/month
   - Impact: 3 (high impact)
   - Confidence: 80% (0.8)
   - Effort: 2 person-weeks
       - RICE score: R*I*C/E = 500*3*.8/2 = 600

### Other prioritization frameworks

- Why learn so many prioritization frameworks?
    - A product manager needs to juggle a lot of tasks.
    - RIC/E might not be suited in all cases.

**When to Use What?**
   - Roadmap planning -> MoSCow
       - Must have – Critical for launch
       - Should have – Important but not urgent
       - Could have – Nice to have
       - Won’t have – Not now

   - Early stage → ICE, Value vs Effort
   - Data-driven → RICE, WSJF
   - WSJF Weighted Shortest Job First
   - Cost of delay/Job size

   - Customer-focused → Kano, Opportunity Scoring
       - Kano model
       - Basic Needs – Expected (login, checkout)
       - Performance Needs – More = better (speed, battery life)
       - Delighters – Unexpected features (AI suggestions)
