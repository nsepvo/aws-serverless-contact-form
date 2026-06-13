# AWS Serverless Contact Form

A fully serverless contact form built on AWS that processes user messages and sends email notifications using API Gateway, AWS Lambda, and Amazon SES. The frontend is deployed using AWS Amplify, with monitoring handled via CloudWatch.

---

## Live Demo

https://staging.d2vpf59fscl1pp.amplifyapp.com/

---

## Overview

This project implements a fully serverless contact form system without requiring any server management.

## AWS Services Used

- AWS Amplify – Frontend hosting and deployment
- Amazon API Gateway – REST API endpoint for requests
- AWS Lambda – Backend logic and request processing
- Amazon SES – Email delivery service
- Amazon CloudWatch – Logging and monitoring

---

When a user submits the form:

- The frontend sends a POST request to API Gateway
- API Gateway triggers a Lambda function
- Lambda validates and processes the request data
- AWS SES sends the email to a verified recipient
- CloudWatch logs execution, errors, and performance metrics

---

## Design Decisions

- Serverless-first architecture to eliminate server management
- Lambda-based processing for scalability and stateless execution
- SES for reliable and low-cost email delivery
- API Gateway as a secure public-facing endpoint
- CloudWatch for built-in observability and debugging

---

## Key Learnings

- Designing serverless architectures using AWS services
- API Gateway and Lambda integration patterns
- Email delivery workflows using Amazon SES
- Frontend deployment with AWS Amplify
- Observability using CloudWatch logs and metrics

---

## Summary

This project demonstrates a serverless contact form built using AWS managed services. It focuses on simplicity and helping me gain hands-on experience with serverless architecture, deployment, monitoring, and email workflows.

## Contact

Open to internship and graduate opportunities in software engineering and cloud computing.

- Email: nevenspooner03@gmail.com
- LinkedIn: https://www.linkedin.com/in/neven-spooner/
