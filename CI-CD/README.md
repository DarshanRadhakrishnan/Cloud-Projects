# AWS CI/CD Pipeline with Testing & EC2 Deployment

## 📋 Project Overview

This project demonstrates a production-ready AWS CI/CD pipeline for a simple **Flask Todo API**. It showcases:

- **Branch-based workflows**: Different pipelines for PR validation vs. production deployment
- **Automated testing**: Unit tests that must pass before deployment
- **Infrastructure as Code**: CodeBuild, CodePipeline, and CodeDeploy integration
- **EC2 deployment**: Automated deployment to Amazon Linux 2 EC2 instances
- **Intentional failure scenarios**: To understand pipeline debugging and failure handling

## 🏗️ High-Level Architecture

```
GitHub Repository
├── Feature Branch (PR)
│   └── → CodePipeline (PR Pipeline)
│       └── → CodeBuild (Unit Tests Only)
│           └── ✓ PASS/✗ FAIL (No Deployment)
│
└── Main Branch (Push)
    └── → CodePipeline (Main Pipeline)
        ├── → CodeBuild (Unit Tests)
        │   └── ✓ PASS → Continue
        │   └── ✗ FAIL → Stop Pipeline
        │
        └── → CodeDeploy
            └── → EC2 Instance
                ├── Download code
                ├── Install dependencies
                └── Start application
```

## 📂 Repository Structure

```
CI-CD/
├── app/
│   └── app.py                 # Flask application with Todo API
├── tests/
│   └── test_app.py           # Unit tests using pytest
├── scripts/
│   ├── start_server.sh       # Deployment start script
│   └── stop_server.sh        # Deployment stop script
├── requirements.txt           # Python dependencies
├── buildspec.yml             # CodeBuild configuration
├── appspec.yml               # CodeDeploy configuration
└── README.md                 # This file
```

## 🚀 Application Features

### Flask Todo API Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|------------|
| GET | `/health` | Health check | 200 |
| GET | `/todos` | Get all todos | 200 |
| POST | `/todos` | Create new todo | 201 |
| GET | `/todos/<id>` | Get specific todo | 200/404 |
| PUT | `/todos/<id>` | Update todo | 200/404 |
| DELETE | `/todos/<id>` | Delete todo | 200/404 |

### Example Usage

**Health Check:**
```bash
curl http://localhost:5000/health
```

**Create Todo:**
```bash
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn AWS CI/CD"}'
```

**Get All Todos:**
```bash
curl http://localhost:5000/todos
```

## ✅ Phase 1: Simple App (Completed)

**What was done:**
- Created a **Python Flask application** with basic Todo CRUD operations
- Kept logic simple to focus on pipeline, not business logic
- Used in-memory storage (no database) for simplicity
- Implemented core endpoints for basic API functionality

**Why Flask?**
- Lightweight and easy to understand
- Perfect for learning CI/CD without complex app logic
- Quick to deploy on EC2

## 📦 Phase 2: Repository Structure (Completed)

**What was done:**
- Created industry-standard directory layout
- Organized code, tests, and deployment scripts
- Added all required AWS configuration files

**Key files:**

### `buildspec.yml`
- Defines CodeBuild process
- Installs dependencies via `pip`
- Runs unit tests with `pytest`
- Fails the pipeline if tests fail
- Caches pip packages for speed

### `appspec.yml`
- Defines CodeDeploy process
- Specifies file destinations on EC2
- Sets permissions for deployed files
- Defines lifecycle hooks:
  - **ApplicationStart**: Runs `start_server.sh`
  - **ApplicationStop**: Runs `stop_server.sh` (for rollbacks)

### `scripts/start_server.sh`
- Creates Python virtual environment
- Installs requirements
- Launches Flask app on port 5000
- Verifies app health

### `scripts/stop_server.sh`
- Gracefully stops the application
- Used during rollbacks or updates

## 🧪 Unit Tests

Located in `tests/test_app.py`

**Test Coverage:**
- ✓ Health check returns 200
- ✓ Get empty todos list
- ✓ Create todo successfully
- ✓ Create todo with missing title (error handling)
- ✓ Get todos after creation
- ✓ Get single todo by ID
- ✓ Get non-existent todo (404)
- ✓ Update todo
- ✓ Delete todo

**Run tests locally:**
```bash
pip install -r requirements.txt
pytest tests/ -v
```

## 🔄 Pipeline Workflows (For Next Phases)

### Pipeline A: Pull Request Validation
- **Trigger**: PR to main branch
- **Stages**:
  1. Source: Fetch PR code from GitHub
  2. Build: Run unit tests with CodeBuild
- **Outcome**: 
  - ✓ PASS → Allow merge
  - ✗ FAIL → Block merge

### Pipeline B: Production Deployment
- **Trigger**: Push to main branch
- **Stages**:
  1. Source: Fetch main branch code
  2. Build: Run unit tests
  3. Deploy: CodeDeploy to EC2
- **Outcome**:
  - ✓ Tests pass + Deploy succeeds → App running on EC2
  - ✗ Tests fail → Stop here (no deployment)
  - ✗ Deploy fails → CodeDeploy auto-rollback

## 🛠️ Prerequisites (For Phases 3+)

1. **AWS Account**
   - IAM user with `AdministratorAccess`
   - AWS CLI configured locally

2. **GitHub**
   - Repository forked/cloned
   - Personal Access Token for CodePipeline integration

3. **EC2 Instance** (Amazon Linux 2, t2.micro)
   - SSH key pair created
   - Security group allows:
     - Port 22 (SSH)
     - Port 5000 (Flask app)
   - Python 3 installed
   - CodeDeploy agent installed

4. **IAM Roles**
   - CodeBuild service role
   - CodeDeploy service role
   - EC2 instance profile

## 📊 CI/CD Benefits

| Aspect | Benefit |
|--------|---------|
| **Code Quality** | Automated tests prevent bugs in production |
| **Consistency** | Same deployment process every time |
| **Speed** | Minutes to deploy vs. hours manual |
| **Auditability** | Every change tracked and logged |
| **Safety** | Rollback on failure, not manual recovery |
| **Learning** | Understand real DevOps practices |

## 🎯 What You'll Learn

- ✓ How CI/CD pipelines work end-to-end
- ✓ CodeBuild for automated testing
- ✓ CodeDeploy for infrastructure automation
- ✓ CodePipeline orchestration
- ✓ Debugging failed pipelines from logs
- ✓ Branch-based workflow strategies
- ✓ Infrastructure automation best practices

## 📝 Next Steps

This foundation enables learning:
- **Phase 3**: EC2 Setup and CodeDeploy Agent
- **Phase 4**: Creating CodeBuild projects
- **Phase 5**: Setting up CodePipeline
- **Phase 6**: Testing failure scenarios
- **Phase 7**: Understanding rollbacks

## 📚 Useful AWS Documentation

- [CodeBuild Documentation](https://docs.aws.amazon.com/codebuild/)
- [CodeDeploy Documentation](https://docs.aws.amazon.com/codedeploy/)
- [CodePipeline Documentation](https://docs.aws.amazon.com/codepipeline/)
- [buildspec.yml Reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)
- [appspec.yml Reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/app-spec-ref.html)

# CI/CD Pipelines – Common Misconceptions & Clear Answers

This section documents common doubts and misconceptions I had while learning CI/CD pipelines, along with correct explanations.  
Reading this helps avoid repeating the same confusion in the future.

---

## 1. Is CI/CD file-wise? Does it deploy individual files?

**❌ Misconception:**  
CI/CD works file by file. If many files exist, CI/CD becomes useless.

**✅ Reality:**  
CI/CD works **commit-wise**, not file-wise.

- A pipeline always pulls the **entire repository**
- Tests, build, and deployment run on the **whole project snapshot**
- Even if you change one file, the entire app is validated

**Key takeaway:**  
> CI/CD operates on commits (project state), not individual files.

---

## 2. If I work only on Auth and DB is not ready, won’t tests fail every time?

**❌ Misconception:**  
CI/CD requires the full application (DB, services, everything) to be completed before deployment.

**✅ Reality:**  
CI/CD validates **intentional scope**, not completeness.

- You test **only what you have implemented**
- Unfinished dependencies (DB, payment, etc.) are:
  - Mocked
  - Skipped
  - Tested later

**Key takeaway:**  
> CI/CD does not wait for the product to be complete; it waits for the current feature to be correct.

---

## 3. Do we need to write tests for everything from day one?

**❌ Misconception:**  
All test files for all services must exist before CI/CD can work.

**✅ Reality:**  
Tests are written **incrementally**, just like code.

Typical progression:
- Early stage → Unit tests only
- Mid stage → Unit + Integration tests
- Final stage → Unit + Integration + End-to-End tests

Unwritten features **do not require tests yet**.

---

## 4. If some tests are not ready, will CI/CD block everything?

**❌ Misconception:**  
Incomplete tests make CI/CD unusable.

**✅ Reality:**  
CI/CD can be designed to:
- Run only selected tests
- Skip specific tests
- Separate pipelines (PR vs main)

Examples:
- PR pipeline → Unit tests only
- Main pipeline → Unit + Deploy

**Key takeaway:**  
> CI/CD blocks bad code, not incomplete features.

---

## 5. What exactly gets deployed? All files?

**❌ Misconception:**  
CI/CD deploys raw source files directly.

**✅ Reality:**  
CI/CD deploys **artifacts**, such as:
- Build folders (`dist/`, `build/`)
- Docker images
- Compiled binaries
- Packaged applications

Deployment targets (EC2, ECS, etc.) receive **artifacts**, not loose files.

---

## 6. Will CI/CD tell me exactly what code caused an error?

**❌ Misconception:**  
CI/CD only says “pipeline failed” without details.

**✅ Reality:**  
CI/CD provides **precise debugging information**:
- Failed stage (build/test/deploy)
- Error logs
- Stack traces
- File name and line number
- Expected vs actual values

**Key takeaway:**  
> CI/CD failures are more informative than local failures if logs are read properly.

---

## 7. Does CI/CD deploy only after the entire project is finished?

**❌ Misconception:**  
Deployment happens only at the very end of development.

**✅ Reality:**  
CI/CD supports **incremental deployment**.

- Features are deployed as they become ready
- Services can be deployed independently
- Early versions are valid deployments

---

## 8. Is CI/CD useless without strong application code?

**❌ Misconception:**  
CI/CD value depends on complex application logic.

**✅ Reality:**  
CI/CD value depends on:
- Pipeline design
- Test strategy
- Failure handling
- Rollback understanding

Even a simple “Hello World” app can teach **advanced CI/CD concepts**.

---

## 9. What does a CI/CD pipeline actually validate?

**❌ Misconception:**  
CI/CD validates completeness of the system.

**✅ Reality:**  
CI/CD validates:
- Code correctness
- Test pass status
- Build success
- Deployment reliability

**One-line truth:**  
> CI/CD validates correctness of the current state, not completeness of the final product.

---

## 10. When does CI/CD become truly useful?

CI/CD becomes powerful when:
- Tests exist for implemented features
- Pipelines are separated (PR vs main)
- Failures are intentional and understood
- Logs are actively analyzed
- Rollbacks are tested

---

## Final Mental Model (Never Forget)

> CI/CD pipelines automate validation and deployment of the entire application state for each commit, using incremental testing and controlled deployments to prevent bad code from reaching production.

---

