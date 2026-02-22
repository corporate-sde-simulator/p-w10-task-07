# DATA-205: Debug Student Grade Calculator (Full Stack)

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 31 · **Story Points:** 8
**Reporter:** QA Team · **Assignee:** You (Intern)
**Labels:** `debugging`, `python`, `sql`, `full-stack`
**Task Type:** Debugging

---

## Description

The student grade calculator has bugs at every layer: the SQL query, the business
logic, and the response formatting. No markers — find them from the symptoms.

## Symptoms

1. Students with no grades show average of None instead of 0
2. Letter grade boundaries are wrong (89.5 should be 'A', getting 'B')
3. The GPA calculation doesn't weight by credit hours
4. Class rank is sorted ascending instead of descending

## Acceptance Criteria

- [ ] Students with no grades get average 0, not None
- [ ] Grade boundaries: A >= 90, B >= 80, C >= 70, D >= 60, F < 60
- [ ] GPA weighted by credit hours
- [ ] Rank sorted highest GPA first
- [ ] All tests pass
