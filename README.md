# Automated CI/CD Pipeline with GitHub and Jenkins Integration

## Features

- Production-ready Django web application.
- Containerized with Docker.
- Automated deployment using Jenkins CI/CD pipeline.
- Multiple AWS EC2 instances for different environments (dev, test, prod).
- GitHub integration with secure personal access tokens.
- Automated Docker image builds and deployments triggered on code commits.

## Architecture

1. **Application**: A Django-based to-do list web application.
2. **Docker**: Containerization of the Django application.
3. **AWS EC2**: Separate EC2 instances for development, staging, and production.
4. **Jenkins**: Orchestrates the CI/CD pipeline for automated builds, tests, and deployments.
5. **GitHub**: Hosts the version-controlled code and triggers Jenkins via webhooks.

## Code Set-up

1. Use a Django full stack web application to deploy.
2. Build the Docker image using the provided Dockerfile.
3. `docker build -t <image-name> .`
4. Install and configure Jenkins on an AWS EC2 instance.
5. Create a new Jenkins pipeline job.
6. Configure the pipeline with your GitHub repository URL and credentials.
7. Add a `Jenkinsfile` to define build, test, and deployment stages.
8. Set up SSH key-based access from Jenkins to your target EC2 instances.
9. Ensure security groups and IAM roles are configured correctly.
10. On each GitHub push, Jenkins builds the Docker image and redeploys the application.
11. Updates to the Dockerfile automatically trigger a rebuild and redeployment.
12. Development: The dev EC2 instance is used for testing and validation.
13. Production: The prod EC2 instance is updated after successful builds on the main/master branch.

## Troubleshooting

1. **Jenkins Build Failures**: Check Jenkins logs and verify Docker installation and permissions.
2. **Deployment Issues**: Ensure the target EC2 instance is accessible and has Docker installed.
3. **Docker Issues**: Use `docker logs` to inspect issues and verify that ports are correctly exposed.

## Contribution

Feel free to fork this repository, raise issues, or submit pull requests to enhance the project. Ideas for improvements, scalability, and security are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
