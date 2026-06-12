# AWS Serverless Contact Form

A fully serverless contact form built on AWS that processes user messages and sends email notifications using API Gateway, AWS Lambda, and Amazon SES. The frontend is deployed using AWS Amplify, with monitoring handled via CloudWatch.

---

## Live Demo

https://staging.d2vpf59fscl1pp.amplifyapp.com/

---

## Architecture

User submissions flow through a serverless AWS pipeline:

Frontend (AWS Amplify)
        ↓
API Gateway (REST API)
        ↓
AWS Lambda (request handler + validation)
        ↓
Amazon SES (email delivery)
        ↓
Recipient Email Inbox

---

## Monitoring Flow

AWS Lambda + API Gateway
        ↓
CloudWatch Logs & Metrics

---

## Overview

This project implements a fully serverless contact form system without requiring any server management.

When a user submits the form:

- The frontend sends a POST request to API Gateway
- API Gateway triggers a Lambda function
- Lambda validates and processes the request data
- AWS SES sends the email to a verified recipient
- CloudWatch logs execution, errors, and performance metrics

---

## AWS Services Used

- AWS Amplify – Frontend hosting and deployment
- Amazon API Gateway – REST API endpoint for requests
- AWS Lambda – Backend logic and request processing
- Amazon SES – Email delivery service
- Amazon CloudWatch – Logging and monitoring

---

## Key Features

- Fully serverless architecture (no infrastructure management)
- Event-driven backend processing
- Secure email delivery via AWS SES
- Input validation at the Lambda layer
- Scalable and cost-efficient design
- Centralised logging and monitoring

---

## Project Structure

/frontend
  - Static frontend (HTML/CSS/JS form)
  - Amplify deployment configuration

/lambda
  - Handler function (Python/Node.js)
  - Input validation logic
  - SES email sending integration

README.md

---

## How It Works

1. User fills out the contact form on the frontend
2. Form sends a POST request to API Gateway
3. API Gateway triggers AWS Lambda
4. Lambda extracts and validates the request payload
5. SES sends an email containing the message content
6. CloudWatch records logs for debugging and monitoring

---

## Design Decisions

- Serverless-first architecture to eliminate server management
- Lambda-based processing for scalability and stateless execution
- SES for reliable and low-cost email delivery
- API Gateway as a secure public-facing endpoint
- CloudWatch for built-in observability and debugging

---

## Security Considerations

- IAM roles restrict Lambda permissions to only required AWS services
- SES uses verified sender identities
- API Gateway acts as a controlled public interface
- No exposed backend servers or persistent instances

---

## Future Improvements

- Add rate limiting and spam protection
- Add CAPTCHA verification to the form
- Store submissions in DynamoDB for history tracking
- Add admin dashboard for message management
- Improve retry handling for failed SES deliveries

---

## Summary

This project demonstrates a production-style serverless contact system using AWS managed services. It focuses on scalability, simplicity, and minimal operational overhead while providing a fully functional email submission pipeline.
