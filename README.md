Log Analysis Utility (Python)

1. Project Overview

In large-scale IT environments, keeping track of active users across multiple workstations is critical for security audits and resource management. This project provides a lightweight Python utility to process system logs and generate real-time reports on user activity.

The Problem: Manual auditing of login/logout logs is time-consuming and prone to human error, especially when events are recorded out of chronological order.

The Solution: A Python script that automatically sorts events, tracks state per machine, and handles inconsistencies in data (like missing login events).

2. Technical Toolkit

Language: Python 3

Data Structures: Dictionaries (for machine mapping), Sets (for unique user tracking)

Key Concepts: Object-Oriented Programming (OOP), Data Sorting, Error Handling

3. The Process

Data Structuring: Created an Event class to standardise how log data is handled.

Chronological Sorting: Implemented a sorting algorithm to ensure logs are processed in the correct order, regardless of how they were received.

State Management: Used Python Sets to store active users. Sets were chosen because they automatically handle duplicates and provide high-performance lookups.

Reporting: Developed a clean reporting function that filters out idle machines to provide a focused view for system administrators.

4. Key Insights

Efficiency: Automated a process that would take minutes of manual searching into a sub-second script execution.

Robustness: Added logic to handle "logout" events for users not previously recorded as logged in, preventing script crashes during data gaps.

5. How to Run

Ensure you have Python installed.

Download log_analysis.py.

Run the script via terminal: python log_analysis.py.
