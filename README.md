Serverless Email Sentiment Inbox
An Intelligent, Event-Driven Email Processing System on AWS

# Overview
aws-serverless-email-sentiment-inbox is a fully serverless, intelligent email inbox built on AWS that automatically analyzes the sentiment of incoming emails and routes, escalates, or flags them based on urgency and tone.
This project demonstrates the real-world potential of serverless architectures by combining storage, compute, AI/ML, and monitoring services—without managing any servers.
The system is ideal for:
Automated customer support inboxes
Complaint & escalation systems
Feedback analysis pipelines
AI-powered email triage systems
 Key Capabilities
 Automatic Email Ingestion
 AI-Based Sentiment Analysis
 Smart Routing Based on Tone
 Fully Serverless & Event-Driven
 Built-in Logging & Monitoring
 Low Cost, High Scalability
 How It Works (High-Level Flow)
Email Received
Incoming emails are stored in an Amazon S3 bucket as .txt or .json objects.
Event Trigger
Uploading a new email triggers an AWS Lambda function via S3 event notifications.
Sentiment Analysis
Lambda sends the email body to Amazon Comprehend to detect sentiment:
POSITIVE
NEGATIVE
NEUTRAL
MIXED
Decision Logic
Based on sentiment:
 Negative → Escalate / Flag urgent
 Positive → Auto-acknowledge / Archive
 Neutral → Route to standard support queue
Monitoring
All actions and results are logged to Amazon CloudWatch for observability and debugging.

# Architecture
┌────────────┐
│   Email    │
│  Source    │
└─────┬──────┘
      ↓
┌────────────┐
│ Amazon S3  │  ← Email stored as object
└─────┬──────┘
      ↓ (Event Trigger)
┌────────────┐
│ AWS Lambda │
└─────┬──────┘
      ↓
┌───────────────────┐
│ Amazon Comprehend │
└─────┬─────────────┘
      ↓
┌────────────┐
│ CloudWatch │
└────────────┘

# AWS Services Used
Service	Purpose
Amazon S3	Stores incoming emails
AWS Lambda	Processes emails and runs logic
Amazon Comprehend	Detects sentiment using NLP
Amazon CloudWatch	Logs and monitors execution
IAM	Secure access control


#  Project Structure
aws-serverless-email-sentiment-inbox/
├── lambda/
│   └── lambda_function.py      # Core email processing logic
├── architecture/
│   └── architecture.png        # System architecture diagram
├── README.md                   # Project documentation
└── .gitignore
🧠 Sentiment-Based Routing Logic
Sentiment	Action
NEGATIVE	Escalate / Flag as urgent
POSITIVE	Auto-acknowledge / Archive
NEUTRAL	Route to support queue!

MIXED	Manual review

# Output

Cloudwatch logs

<img width="1176" height="675" alt="Screenshot 2026-01-17 at 11 01 11 AM" src="https://github.com/user-attachments/assets/6a35ea95-4690-41bb-9dc5-ad1a199769f4" />






