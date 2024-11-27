# Automated CI/CD Pipeline with GitHub and Jenkins Integration
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

## Code Set-up

1. git clone https://github.com/rohantikotekar/Automated-CI-CD-pipeline-with-GitHub-and-Jenkins-Integration.git
2. Build the Docker image using the provided Dockerfile.
3. docker build -t <image-name> .
4. Install and set up Jenkins.
5. Create a new Jenkins pipeline job.
6. Configure the pipeline with your GitHub repository URL and credentials.
7. Set up Jenkins to build the Docker image and deploy to EC2 instances.
8. Deploy the Docker container to each EC2 instance.
9. Ensure security groups and access controls are configured correctly.
10. Jenkins automatically builds the Docker image with each code commit to GitHub.
11. The Dockerfile can be updated as needed. Jenkins will rebuild the Docker image and redeploy it automatically.
12. Development: Use the dev EC2 instance for development and testing.
13. Production: The prod EC2 instance is updated with each successful code commit to the master branch.

## Troubleshooting
1. Jenkins Build Failures: Check Jenkins build logs for errors.
2. Deployment Issues: Ensure EC2 instances are running and properly configured.
3. Docker Issues: Verify Docker installation and check Docker logs.

## Contribution

Feel free to submit issues or pull requests if you have any suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

