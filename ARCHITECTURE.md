## Data Layer - Day 11+
1. db_client/: Direct DB access for test setup/teardown only
2. Rule: Steps may call db_client for Given setup. Never for Then assertions.
3. Rationale: 100x faster than API for bulk data. But assertions must use API to avoid schema coupling.
4. Prod: DB access forbidden. API only.

## Future Hooks - Day 11+
1. environment.py: Created when we need before_all/after_scenario for driver mgmt
2. Will handle: WebDriver factory, API client sessions, Allure attach on fail
3. Will enable: --steps-dir filtering + tag-based suite selection
4. Rule: No hooks until first real test runs. YAGNI applies.

## Refactor Plan: Day 11
1. Split steps/ by domain when >10 scenarios
2. Add db_client/ when first test needs >3 API calls for setup
3. Add environment.py when first WebDriver is created

**Day 2 Status**: Architecture designed. Folder rules + split strategy + CI optimization + DB layer documented.