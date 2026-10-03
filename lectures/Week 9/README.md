# Lecture 9 - Git Workflows, Containers, and CI/CD

**Source:** [CPE334 Lecture 9 PDF](<CPE334_Lecture09 - Git workflows_containers_CI_CD.pdf>)

**Course:** CPE 334 Software Engineering, Semester 1/2026

## Topics covered

- Branching conventions: GitFlow, GitHub Flow, and Trunk-Based Development; choosing and adapting a workflow to the team and product.
- Merge conflicts and integration strategies, including merge, rebase, squash, and interactive rebase; commit quality and `.gitignore`.
- Containers and Docker: images, containers, Dockerfiles, registries, networking, storage, and common commands.
- Container orchestration and Kubernetes concepts, capabilities, objects, and `kubectl` workflows.
- Infrastructure as Code (IaC), including declarative versus imperative approaches and common tools.
- Continuous Integration, Continuous Delivery, and Continuous Deployment; pipeline stages and common CI/CD tools.
- GitHub Actions: workflows, events, jobs, runners, services, steps, actions, and workflow files.
- Code review and code-analysis tooling, including linters, quality metrics, and security scanners.
- Continuous Delivery practices, Tekton pipelines and triggers, and supplemental social-coding and CI-tool examples.

## Connection to Lab 4

The lecture reinforces Lab 4's required GitHub Issues, feature branches, pull requests, peer review, staged integration, and final regression workflow. Its CI/CD material can inform how the team automates and verifies tests.

Docker, Kubernetes, IaC, and Tekton are useful concepts for understanding build and deployment environments, but the lecture does not by itself add implementation requirements to TokTickIT. The [Lab 4 handout](../../labs/Lab04/Lab_04_Labsheet.pdf) remains authoritative for the sprint scope; it explicitly excludes production-scale cloud operations and other unapproved features.

This README is a study index, not a replacement for the lecture slides or an amendment to the Lab 4 rubric.
