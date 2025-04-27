# DevOps Interview Q&A (Practice with Guess and Reveal)

---

## 1. Self Introduction
<details>
<summary>Click to reveal</summary>

I am a DevOps/Cloud Engineer with strong experience in CI/CD pipelines, containerization, Kubernetes, cloud services like AWS, and infrastructure as code tools like Terraform. I focus on building scalable, automated, and secure systems.

</details>

---

## 2. Explain Detailed CI-CD Pipeline
<details>
<summary>Click to reveal</summary>

A CI/CD pipeline automates building, testing, and deploying applications:
- CI: Code → Build → Test → Artifact.
- CD: Deploy → Staging/Prod.
Common tools: Jenkins, GitHub Actions, GitLab CI, ArgoCD.

</details>

---

## 3. Which Branching Strategy You Have Used in Your Company
<details>
<summary>Click to reveal</summary>

We used **Gitflow strategy**:
- `main` (Production ready)
- `develop` (Ongoing development)
- `feature/*` (New features)
- `release/*` (Prepare releases)
- `hotfix/*` (Urgent fixes)

</details>

---

## 4. How to Build and Deploy an Application Using Docker
<details>
<summary>Click to reveal</summary>

- Create a `Dockerfile`.
- Build: `docker build -t app:v1 .`
- Run: `docker run -d -p 8080:8080 app:v1`
- Push to a Docker registry if needed.

</details>

---

## 5. What is the Difference Between Feature Branch and Release Branch
<details>
<summary>Click to reveal</summary>

| Feature Branch | Release Branch |
|----------------|----------------|
| New features   | Finalize version |
| Merged into `develop` | Merged into `main` and `develop` |
| Short-lived    | More stable for QA |

</details>

---

## 6. Who Merges the Code in Your Team
<details>
<summary>Click to reveal</summary>

Developers raise a Pull Request (PR).  
After successful review and passing tests, Team Lead or Reviewer merges it to main branches.

</details>

---

## 7. What is Dockerfile, Docker Image, and Docker Containers
<details>
<summary>Click to reveal</summary>

- **Dockerfile:** Instructions to build a container image.
- **Docker Image:** Built artifact containing application.
- **Docker Container:** Running instance of an image.

</details>

---

## 8. Difference Between Docker ADD and Docker COPY
<details>
<summary>Click to reveal</summary>

- **COPY:** Copies local files/folders into container.
- **ADD:** Copies + auto-extracts archives and supports URLs.

</details>

---

## 9. How Many Pods Are Present in One Node and How Many Containers in One Pod
<details>
<summary>Click to reveal</summary>

- **Pods per Node:** Limited by node resources (CPU, RAM).
- **Containers per Pod:** One or more (usually one unless sidecar needed).

</details>

---

## 10. Efficient Way: Pod with One Container or Multiple Containers
<details>
<summary>Click to reveal</summary>

- **One container per pod** is efficient for simple apps.
- **Multiple containers per pod** used when containers are tightly coupled (e.g., sidecar pattern).

</details>

---

## 11. How to Measure Metrics in Kubernetes
<details>
<summary>Click to reveal</summary>

Use tools like:
- Prometheus + Grafana
- Metrics-server
- kube-state-metrics
They collect CPU, memory, and pod statuses.

</details>

---

## 12. What is Port of DNS, SSH, and HTTPS
<details>
<summary>Click to reveal</summary>

| Service | Port |
|---------|------|
| DNS     | 53   |
| SSH     | 22   |
| HTTPS   | 443  |

</details>

---

## 13. If You Have New EC2 and RDS How Can You Connect RDS with EC2
<details>
<summary>Click to reveal</summary>

- Ensure EC2 and RDS are in same VPC/Subnet.
- Configure RDS security group to allow EC2 access.
- Connect using RDS endpoint and database credentials.

</details>

---

## 14. Explain S3 Storage Classes
<details>
<summary>Click to reveal</summary>

| Storage Class | Purpose |
|---------------|---------|
| Standard      | Frequent access |
| Intelligent-Tiering | Auto-cost optimization |
| Standard-IA   | Infrequent access |
| One Zone-IA   | Lower cost, one AZ |
| Glacier       | Archiving |
| Glacier Deep Archive | Long-term archival |

</details>

---

## 15. Any Idea on AWS S3 Bucket Backup
<details>
<summary>Click to reveal</summary>

Backup options:
- Enable **Versioning**.
- Set **Lifecycle policies**.
- Use **Cross-Region Replication**.
- Use **AWS Backup service**.

</details>

---

## 16. How to Create AWS Lambda and How It Works
<details>
<summary>Click to reveal</summary>

- Create Lambda in AWS Console or CLI.
- Choose runtime (Python, Node.js, etc.)
- Add trigger (S3, API Gateway, etc.)
- Lambda runs your code automatically when triggered.

</details>

---

## 17. How to Store Terraform Statefile and Secure It
<details>
<summary>Click to reveal</summary>

- Store remotely in S3 bucket with encryption.
- Use **DynamoDB** for state locking.
- Apply strict **IAM policies** to restrict access.
- Enable **versioning** on S3 bucket.

</details>

---

## 18. I Stored Statefile in Remote and Current State is Different, Can I Update?
<details>
<summary>Click to reveal</summary>

Yes:
- Use `terraform refresh` to update local state.
- Or run `terraform plan` and `terraform apply` to sync remote state with infrastructure.

</details>

---
