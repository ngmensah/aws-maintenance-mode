# Project 2: AWS RDS Backup Automation and Resource Cleanup

## Overview

This project automates the process of placing AWS environments in "maintenance mode" by backing up all RDS databases and pausing or deleting non-critical resources. It’s ideal for saving costs without shutting down production.

## Features

- Backup all RDS databases using AWS CLI

- Python script for resource analysis

- Identify and pause costly resources

- Delete dev environment safely after backup

## Tools Used

- AWS CLI

- Python (with Boto3)

- Shell scripting

## File Structure

aws-maintenance-mode/
├── backup_rds.sh
├── cleanup.py
├── requirements.txt
├── deleted_resources_report.md
└── README.md

## Deliverables

- Backup scripts

- Python script for cost analysis

- PDF/Markdown report of deleted/paused resources
