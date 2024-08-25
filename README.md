# Automated CI/CD Pipeline with GitHub and Jenkins Integration

## Project Overview

This project demonstrates the creation of a full stack to-do list application using Flask, with an automated CI/CD pipeline integrated with GitHub and Jenkins. The application is containerized using Docker and deployed on AWS EC2 instances. The pipeline ensures seamless updates to the production environment with each code commit.

## Features

- Full stack to-do list application built with Flask.
- Containerized with Docker.
- Automated deployment using Jenkins CI/CD pipeline.
- Multiple AWS EC2 instances for different environments (dev, test, prod).
- GitHub integration with web tokens for secure access.
- Automated Docker image updates and deployments on code commits.

## Architecture

1. **Application**: A Flask-based to-do list application.
2. **Docker**: Containerization of the Flask application.
3. **AWS EC2**: Separate instances for development, testing, and production.
4. **Jenkins**: CI/CD pipeline for automated builds, tests, and deployments.
5. **GitHub**: Repository for version control and CI/CD integration.

## Setup and Configuration

### Prerequisites

- Docker
- Jenkins
- AWS CLI
- GitHub account with web tokens

### Project Setup

## Clone the Repository**
 
   git clone <repository-url>
   cd <repository-directory>
Create Docker Image

##  Ensure Docker is installed and running.
Build the Docker image using the provided Dockerfile.
docker build -t <image-name> .

## Configure Jenkins
Install and set up Jenkins.
Create a new Jenkins pipeline job.
Configure the pipeline with your GitHub repository URL and credentials.
Set up Jenkins to build the Docker image and deploy to EC2 instances.
Deploy to AWS EC2

## Create and configure EC2 instances for dev, test, and prod environments.
Deploy the Docker container to each EC2 instance.
Ensure security groups and access controls are configured correctly.


## Jenkins automatically builds the Docker image with each code commit to GitHub.
Automated Deployment

## Jenkins deploys the Docker container to the appropriate EC2 instance based on the environment (dev, test, prod).
Updating Docker Images

The Dockerfile can be updated as needed. Jenkins will rebuild the Docker image and redeploy it automatically.
Development: Use the dev EC2 instance for development and testing.
Production: The prod EC2 instance is updated with each successful code commit to the master branch.
Troubleshooting
Jenkins Build Failures: Check Jenkins build logs for errors.
Deployment Issues: Ensure EC2 instances are running and properly configured.
Docker Issues: Verify Docker installation and check Docker logs.
Contribution
Feel free to submit issues or pull requests if you have any suggestions or improvements for the project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

