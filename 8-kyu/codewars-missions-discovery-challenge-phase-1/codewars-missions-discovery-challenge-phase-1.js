function submitProposal() {
  return {
    // === YOUR PROPOSAL ===
    problem_title: "Stagnant Quality Feedback Loop for Kata",
    category: "kata_quality",
    problem_statement: "Codewars lacks a formalized, transparent, and actionable system for the community to report, triage, and resolve kata quality issues (e.g., broken tests, ambiguous descriptions, flawed solution validations). Currently, the process relies on scattered GitHub issues, informal Discord threads, and manual author intervention, which often leads to issues going unaddressed for years. This creates a stagnant feedback loop where known problems persist, frustrate users, and degrade the platform's reputation as a reliable learning resource. The root cause is not individual broken kata, but the absence of a structured, visible workflow that empowers the community to maintain and improve the kata corpus collectively.",
    who_affected: "This problem affects every user who interacts with kata, but the impact varies: new users encounter broken or poorly explained kata that erode confidence; experienced users waste time on flawed challenges; kata authors are unaware of issues or overwhelmed by unstructured feedback; and the platform as a whole suffers from a growing 'technical debt' of unmaintained content that discourages engagement and retention across all user segments.",
    evidence: "The problem is widely acknowledged across community channels. A 2021 Codewars Census comment stated, 'The issue with kata not being updated is a huge problem' (https://github.com/Codewars/codewars.com/issues/1346). The #kata-discussions channel on Discord frequently contains threads where users report broken kata, with common replies being 'this has been an issue for months' or 'the author is inactive.' For example, the kata 'IP Validation' (kata: 515de9ae9dcfc65eb6000001) has a longstanding GitHub issue (https://github.com/Codewars/codewars.com/issues/1581) about its test cases that remained unresolved for over two years. My personal experience and that of many others include encountering kata with known, unaddressed issues, leading to wasted time and frustration. The sheer volume of unmerged pull requests on the official GitHub repo for kata issues further demonstrates the bottleneck in the current process.",
    feasibility_score: 3,
​
    // === ABOUT YOU ===
    role: "Senior Software Engineer",
    experience_years: "10+",
​
    // === YOUR PROCESS ===
    worked_solo_or_team: "solo",
    ai_tools_used: ["Claude"],
    primary_ai_tool: "Claude",
    ai_usage_percent: 30,
    where_ai_helped: ["ideation", "writing"],
    where_ai_fell_short: "While Claude helped structure my thoughts and ensure the proposal met the character count requirements, it lacked the deep, specific knowledge of Codewars' internal community culture and historical feedback loops that are only gained from years of participation. Its suggestions for solutions were generic and didn't account for the platform's unique constraints.",
    other_tools_used: "VS Code, GitHub",
    time_spent_minutes: 45
  };
}