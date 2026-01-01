# 🚀 AWS CI/CD Pipeline Project - Phases Documentation

---

## 📊 Project Overview

This document tracks the progress of building a production-grade AWS CI/CD pipeline for a Flask Todo API. The pipeline automates testing and deployment to EC2 instances.

**Project Goal**: Separate PR validation (testing only) from production deployment (test + deploy to EC2)

---

## ✅ Phase 1: Simple App ✓ COMPLETED

### 📋 What Was Done

Created a lightweight **Python Flask Todo API** that focuses on pipeline learning, not complex business logic.

### 🎯 Features Implemented

✅ **6 RESTful API Endpoints**
- `GET /health` - Health check
- `GET /todos` - List all todos
- `POST /todos` - Create new todo
- `GET /todos/<id>` - Get specific todo
- `PUT /todos/<id>` - Update todo
- `DELETE /todos/<id>` - Delete todo

✅ **In-Memory Storage**
- No database required
- Simple to understand and deploy
- Perfect for learning CI/CD

✅ **Error Handling**
- 400 errors for missing fields
- 404 errors for not found resources
- Proper HTTP status codes

### 📁 Deliverables

```
app/
├── __init__.py
└── app.py (141 lines - Flask application)
```

### 🔗 Key Code Snippet

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
todos = {}

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    # ... create todo logic
```

---

## ✅ Phase 2: Repository Structure ✓ COMPLETED

### 📋 What Was Done

Organized code into **industry-standard directory layout** with all AWS CI/CD configuration files.

### 🎯 Features Implemented

✅ **Standard Project Structure**
```
CI-CD/
├── app/              # Application code
├── tests/            # Unit tests
├── scripts/          # Deployment scripts
├── buildspec.yml     # CodeBuild config
├── appspec.yml       # CodeDeploy config
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

✅ **Unit Tests (10 tests)**
- Health endpoint validation
- CRUD operations testing
- Error handling verification
- 100% pass rate

✅ **Configuration Files**
- `buildspec.yml` - CodeBuild pipeline stages
- `appspec.yml` - CodeDeploy lifecycle hooks
- `requirements.txt` - Flask + pytest dependencies

✅ **Deployment Scripts**
- `start_server.sh` - Application startup
- `stop_server.sh` - Graceful shutdown

### 📁 Deliverables

```
tests/
└── test_app.py (10 unit tests)

scripts/
├── start_server.sh
└── stop_server.sh

buildspec.yml
appspec.yml
requirements.txt
.gitignore
README.md
```

---

## ✅ Phase 3: EC2 Setup ✓ COMPLETED

### 📋 What Was Done

Launched and configured an **Amazon Linux 2 EC2 instance** as the deployment target, with all required runtimes and the CodeDeploy agent installed.

### 🎯 Features Implemented

✅ **EC2 Instance Provisioned**
- **AMI**: Amazon Linux 2 (free tier eligible)
- **Instance Type**: t2.micro (free tier)
- **Key Pair**: SSH access configured
- **Security Group**: Ports 22 (SSH) & 5000 (Flask app) open

✅ **Runtime Installed**
- Python 3 installed and verified
- pip3 (package manager) installed
- curl installed for health checks
- git installed for repository cloning

### 📸 Phase 3 Evidence - Ruby & Dependencies Installation

![Ruby Installation](./phases-screenshots/phase3-ruby-install.png)

**Output shows:**
```
Package                     Version              Size
=====================================================
Installing:
ruby3.2                     3.2.8-184.amzn2023   41 KB
ruby3.2-default-gems        3.2.8-184.amzn2023   33 KB
ruby3.2-libs                3.2.8-184.amzn2023   3.9 MB
ruby3.2-rubygem-io-console  0.6.0-184.amzn2023   24 KB
ruby3.2-rubygem-json        2.6.3-184.amzn2023   52 KB
ruby3.2-rubygem-psych       5.0.1-184.amzn2023   50 KB
...
Total size: 2.8 M
Installed size: 13 M
```

✅ **CodeDeploy Agent Installed**
- Downloaded agent installer
- Installed automatically
- Running as system service

### 📸 Phase 3 Evidence - CodeDeploy Agent Installation

![CodeDeploy Installation](./phases-screenshots/phase3-codedeploy-install.png)

**Installation Output:**
```
Installing:
codedeploy-agent             noarch               1.8.0-17    @commandline    2.8 MB

Transaction Summary
=====================================================
Install 1 Package

Total size: 2.8 M
Installed size: 13 M

Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        : codedeploy-agent-1.8.0-17.noarch
  Running scriptlet: codedeploy-agent-1.8.0-17.noarch
  Installing       : codedeploy-agent-1.8.0-17.noarch
  Running scriptlet: codedeploy-agent-1.8.0-17.noarch
  Complete!
```

✅ **CodeDeploy Agent Running**
- Service status: **Active (running)**
- Process: codedeploy-agent master (PID: 27071)
- Memory: 66.5 MB
- CPU: 1.236s
- Auto-enabled on boot

### 📸 Phase 3 Evidence - CodeDeploy Agent Running Status

![CodeDeploy Agent Status](./phases-screenshots/phase3-codedeploy-status.png)

**Service Status Output:**
```
● codedeploy-agent.service - AWS CodeDeploy Host Agent
   Loaded: loaded (/usr/lib/systemd/system/codedeploy-agent.service; enabled; preset: disabled)
   Active: active (running) since Thu 2026-01-01 06:16:48 UTC; 45s ago
   Main PID: 27071 (ruby)
   Tasks: 3 (limit: 1067)
   Memory: 66.5M
   CPU: 1.236s
   CGroup: /system.slice/codedeploy-agent.service
     ├─27071 "codedeploy-agent: master 27071"
     └─27073 "codedeploy-agent: InstanceAgent::Plugins::CodeDeployPlugin::C...

Jan 01 06:16:47 ip-172-31-12-24.ec2.internal systemd[1]: Starting codedeploy-agent.service...
Jan 01 06:16:48 ip-172-31-12-24.ec2.internal systemd[1]: Started codedeploy-agent.service.
```

✅ **Application Directory Created**
- `/home/ec2-user/app` directory ready
- Proper permissions set
- Ready for CodeDeploy to push code

### 🔑 Key Accomplishments

| Component | Status | Notes |
|-----------|--------|-------|
| EC2 Instance | ✅ Running | Amazon Linux 2, t2.micro |
| SSH Access | ✅ Configured | Port 22 open, key-based auth |
| Python Runtime | ✅ Installed | Python 3.x ready |
| CodeDeploy Agent | ✅ Running | Service active, auto-start enabled |
| App Directory | ✅ Created | `/home/ec2-user/app` ready |
| Security Group | ✅ Configured | Ports 22 & 5000 open |

---

## ✅ Phase 4: IAM Roles & Policies ✓ COMPLETED

### 📋 What Was Done

Created **4 IAM roles with proper permissions** to allow AWS services to communicate and perform their functions.

### 🎯 Features Implemented

✅ **EC2-CodeDeploy-Role**
- **Purpose**: Allows EC2 instance to receive deployments
- **Permissions**: `AmazonEC2RoleforAWSCodeDeploy`
- **Attached To**: EC2 instance via instance profile
- **Status**: ✅ Configured & Attached

✅ **CodeBuild-Role**
- **Purpose**: Allows CodeBuild to run tests and build projects
- **Permissions**: 
  - `CodeBuildAdminAccess` (manage CodeBuild)
  - `AmazonEC2FullAccess` (EC2 operations)
- **Status**: ✅ Created

✅ **CodeDeploy-Role**
- **Purpose**: Allows CodeDeploy service to deploy code to EC2
- **Permissions**: `AWSCodeDeployRoleForEC2`
- **Status**: ✅ Created

✅ **CodePipeline-Role**
- **Purpose**: Allows CodePipeline to orchestrate the CI/CD workflow
- **Permissions**: 
  - Inline policy with CodePipeline, CodeBuild, CodeDeploy, S3, and EC2 full access
  - `AmazonS3FullAccess` (artifact storage)
- **Status**: ✅ Created with inline policies

### 🔐 Permission Architecture

```
GitHub Repo Push
    ↓
CodePipeline (uses CodePipeline-Role)
    ├─→ Fetches source code
    ├─→ Triggers CodeBuild (passes CodeBuild-Role)
    │     └─→ Runs tests
    │     └─→ Creates artifacts
    ├─→ Triggers CodeDeploy (passes CodeDeploy-Role)
    │     └─→ Uses EC2-CodeDeploy-Role to communicate with EC2
    │     └─→ Deploys code to /home/ec2-user/app
    └─→ Artifact stored in S3 bucket
```

### 📝 IAM Roles Summary

| Role | Service | Permissions | Status |
|------|---------|-------------|--------|
| EC2-CodeDeploy-Role | EC2 | CodeDeploy Agent permissions | ✅ |
| CodeBuild-Role | CodeBuild | Build & EC2 access | ✅ |
| CodeDeploy-Role | CodeDeploy | Deployment permissions | ✅ |
| CodePipeline-Role | CodePipeline | Pipeline orchestration | ✅ |

### 🔧 Implementation Method

**Roles created using:**
- AWS IAM Console (UI-based) for discovery and verification
- AWS CLI for efficient policy attachment and automation

### 📋 Phase 4 Checklist

- [x] EC2-CodeDeploy-Role created
- [x] EC2-CodeDeploy-Role attached to EC2 instance
- [x] CodeBuild-Role created with permissions
- [x] CodeDeploy-Role created with permissions
- [x] CodePipeline-Role created with inline policies
- [x] All roles visible in IAM Console
- [x] Trust relationships configured correctly

---

## 📈 Overall Progress

```
Phase 1: Simple App              ✅ COMPLETED
Phase 2: Repository Structure    ✅ COMPLETED
Phase 3: EC2 Setup               ✅ COMPLETED
Phase 4: IAM Roles & Policies    ✅ COMPLETED
─────────────────────────────────────────────
Phase 5: CodeBuild Project       ⏳ NEXT
Phase 6: CodePipeline Setup      ⏳ TODO
Phase 7: Failure Testing         ⏳ TODO
Phase 8: Debugging & Logging     ⏳ TODO
Phase 9: Rollback Testing        ⏳ TODO
Phase 10: Final Documentation    ⏳ TODO
```

**Completion**: 40% ✅ (4 of 10 phases)

---

## 🎯 What's Ready

✅ Flask application deployed-ready  
✅ Unit tests passing (10/10)  
✅ EC2 instance running with CodeDeploy agent  
✅ IAM roles configured for inter-service communication  
✅ All configurations (buildspec.yml, appspec.yml) in place

---

## 🚀 Next Phase: Phase 5 - CodeBuild Project

### What's Next

- Create CodeBuild project in AWS Console
- Connect to GitHub repository
- Configure to use buildspec.yml
- Test the build pipeline manually
- Verify tests run automatically

### Expected Outcome

CodeBuild will automatically:
1. Clone code from GitHub
2. Install dependencies (`pip install -r requirements.txt`)
3. Run unit tests (`pytest tests/`)
4. Report pass/fail status

---

## 📚 Key Learnings

### Phase 1-2 Learnings
- ✅ How to structure a CI/CD-ready Flask application
- ✅ Writing testable code with proper separation
- ✅ Industry-standard project organization

### Phase 3 Learnings
- ✅ EC2 instance provisioning and configuration
- ✅ Security groups and network configuration
- ✅ IAM instance profiles and EC2 integration
- ✅ CodeDeploy agent architecture and lifecycle

### Phase 4 Learnings
- ✅ IAM role and policy management
- ✅ Service-to-service authentication (trust relationships)
- ✅ Inline vs managed policies
- ✅ Principle of least privilege in permissions

---

## 📞 Important URLs & Resources

- **AWS CodeBuild Docs**: https://docs.aws.amazon.com/codebuild/
- **AWS CodeDeploy Docs**: https://docs.aws.amazon.com/codedeploy/
- **AWS CodePipeline Docs**: https://docs.aws.amazon.com/codepipeline/
- **buildspec.yml Reference**: https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html
- **appspec.yml Reference**: https://docs.aws.amazon.com/codedeploy/latest/userguide/app-spec-ref.html

---

## 🎓 Summary

**Completed**: 4 critical foundation phases for AWS CI/CD pipeline  
**Status**: Ready to move to CodeBuild and pipeline automation  
**Timeline**: 4 phases completed, 6 remaining  
**Infrastructure**: Production-ready EC2 + IAM setup  

**Ready for Phase 5! 🚀**
