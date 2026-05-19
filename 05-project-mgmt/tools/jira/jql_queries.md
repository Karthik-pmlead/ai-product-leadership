# 🔍 jql_queries.md

# Common Jira JQL Queries

## Active Sprint Issues

```sql
project = AI AND sprint in openSprints()
```

## High Priority Bugs

```sql
project = AI AND priority = High AND type = Bug
```

## Unassigned Stories

```sql
project = AI AND assignee is EMPTY
```

## Blocked Tasks

```sql
project = AI AND status = Blocked
```
