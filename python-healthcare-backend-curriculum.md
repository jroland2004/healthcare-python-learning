# Python Backend Developer Curriculum
## Healthcare Data Analytics & API Development

**Student**: Jason  
**Background**: RN with 20 years IT leadership experience  
**Goal**: Transition to healthcare technology roles combining clinical and technical expertise  
**Time commitment**: ~8 hours/week  
**Environment**: macOS, VS Code  
**Target deployment**: AWS (free tier)

---

## Curriculum Overview

This curriculum takes you from Python novice to job-ready backend developer with healthcare data specialization. Given your 8 hours per week, expect approximately 6-7 months to complete all phases.

| Phase | Focus | Duration | Hours |
|-------|-------|----------|-------|
| 1 | Python Fundamentals | 5 weeks | 40 |
| 2 | Environment & Tooling | 2 weeks | 16 |
| 3 | Databases & SQL | 4 weeks | 32 |
| 4 | Data Analytics with Pandas | 4 weeks | 32 |
| 5 | Data Visualization & Dashboards | 3 weeks | 24 |
| 6 | API Development with FastAPI | 5 weeks | 40 |
| 7 | Testing & Code Quality | 2 weeks | 16 |
| 8 | Containerization & Deployment | 3 weeks | 24 |
| 9 | Capstone Project | 4 weeks | 32 |

**Total**: ~32 weeks / 256 hours

---

## Healthcare Datasets You'll Use

Throughout this curriculum, you'll work with real public healthcare data:

1. **CMS Medicare Provider Data** - Hospital quality metrics, provider information
   - https://data.cms.gov/

2. **CDC WONDER** - Public health statistics, mortality data, disease surveillance
   - https://wonder.cdc.gov/

3. **Synthea** - Synthetic but realistic patient records (FHIR-compliant)
   - https://synthetichealth.github.io/synthea/

4. **Hospital Readmissions** - 30-day readmission rates by hospital
   - Available through CMS

5. **NPPES NPI Registry** - National provider identifier database
   - https://npiregistry.cms.hhs.gov/

---

# Phase 1: Python Fundamentals
**Duration**: 5 weeks (~40 hours)  
**Goal**: Write confident, idiomatic Python code

## Week 1: Getting Started & Core Syntax

### Learning objectives
- Install and configure Python on macOS
- Understand variables, data types, and basic operators
- Write simple programs with user input and output

### Environment setup

**Install Homebrew** (macOS package manager):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Install Python via Homebrew**:
```bash
brew install python@3.12
```

**Verify installation**:
```bash
python3 --version
```

**Configure VS Code**:
1. Install the "Python" extension by Microsoft
2. Install the "Pylance" extension for better code intelligence
3. Open Command Palette (Cmd+Shift+P) → "Python: Select Interpreter" → Choose Python 3.12

### Topics to study
- Variables and assignment
- Data types: int, float, str, bool
- Basic operators: arithmetic, comparison, logical
- String formatting (f-strings)
- Input/output with `input()` and `print()`
- Comments and code readability

### Practice exercises
1. Write a program that converts patient temperature from Fahrenheit to Celsius
2. Create a BMI calculator that takes height and weight as input
3. Build a simple dose calculator that adjusts medication based on patient weight

### Resources
- Python official tutorial, sections 1-3: https://docs.python.org/3/tutorial/
- "Automate the Boring Stuff" Chapter 1: https://automatetheboringstuff.com/2e/chapter1/

---

## Week 2: Control Flow & Data Structures

### Learning objectives
- Use conditional statements to make decisions
- Implement loops for repetitive tasks
- Work with lists and dictionaries

### Topics to study
- if/elif/else statements
- Comparison and boolean logic
- while loops
- for loops and range()
- Lists: creation, indexing, slicing, methods
- Dictionaries: key-value pairs, accessing, updating
- Tuples and when to use them
- Basic list comprehensions

### Practice exercises
1. Create a triage priority classifier that categorizes patients based on vital signs
2. Build a program that tracks a list of patients and their room assignments
3. Write a medication interaction checker using a dictionary of drug interactions

### Healthcare mini-project: Vital Signs Monitor
Create a program that:
- Accepts patient vital signs (heart rate, blood pressure, temperature, O2 sat)
- Stores them in a dictionary
- Evaluates each against normal ranges
- Outputs warnings for any abnormal values
- Allows adding multiple patients to a list

---

## Week 3: Functions & Modules

### Learning objectives
- Write reusable functions
- Understand scope and parameters
- Import and use modules

### Topics to study
- Function definition with `def`
- Parameters and arguments
- Return values
- Default parameters
- Variable scope (local vs global)
- Importing modules (math, random, datetime)
- Creating your own modules

### Practice exercises
1. Create functions for common nursing calculations (drug dosages, drip rates, unit conversions)
2. Build a module of healthcare utility functions you can reuse
3. Write a function that calculates age from date of birth

### Healthcare mini-project: Clinical Calculator Library
Build a module called `clinical_calc.py` containing functions for:
- IV drip rate calculation
- Pediatric dosing (weight-based)
- Creatinine clearance estimation
- BMI with category classification
- MAP (Mean Arterial Pressure) calculation

Write a separate program that imports and uses these functions.

---

## Week 4: File Handling & Error Management

### Learning objectives
- Read and write files
- Handle errors gracefully
- Work with JSON data

### Topics to study
- Opening files with `open()` and context managers (`with`)
- Reading: `read()`, `readline()`, `readlines()`
- Writing and appending to files
- CSV files with the csv module
- JSON files with the json module
- Try/except blocks
- Common exceptions and when they occur
- Raising exceptions

### Practice exercises
1. Read a CSV of patient data and calculate average age
2. Write patient records to a JSON file
3. Create a program that gracefully handles missing files or malformed data

### Healthcare mini-project: Patient Data Processor
Create a program that:
- Reads patient records from a CSV file
- Validates each record (checks for missing fields, invalid values)
- Logs any errors to an error file with details
- Writes valid records to a new JSON file
- Generates a summary report (total patients, error count, basic statistics)

Sample CSV structure:
```
patient_id,name,dob,gender,heart_rate,bp_systolic,bp_diastolic,temperature
```

---

## Week 5: Object-Oriented Programming Basics

### Learning objectives
- Understand classes and objects
- Create custom classes for healthcare entities
- Use inheritance for code reuse

### Topics to study
- Classes and objects
- The `__init__` method
- Instance attributes and methods
- Class attributes
- Basic inheritance
- The `__str__` and `__repr__` methods

### Practice exercises
1. Create a Patient class with attributes and methods
2. Build a Medication class that tracks dosing information
3. Implement a VitalSigns class that can evaluate readings

### Healthcare mini-project: Hospital Ward Management System
Build a command-line system with classes for:
- `Patient`: id, name, dob, diagnosis, vital signs history
- `Bed`: bed number, patient assignment, status
- `Ward`: collection of beds, admission/discharge methods
- `VitalSigns`: readings with timestamp, normal range checking

The system should:
- Add/remove patients
- Assign patients to beds
- Record vital signs with timestamps
- Generate ward census report
- Save/load state from JSON files

---

## Phase 1 Checkpoint

Before moving to Phase 2, you should be able to:
- [ ] Write Python scripts without constantly referencing syntax
- [ ] Use lists and dictionaries comfortably
- [ ] Create functions with appropriate parameters and return values
- [ ] Read/write CSV and JSON files
- [ ] Handle errors with try/except
- [ ] Create simple classes with methods
- [ ] Complete the Ward Management System project

---

# Phase 2: Environment & Tooling
**Duration**: 2 weeks (~16 hours)  
**Goal**: Professional Python development setup

## Week 6: Virtual Environments & Package Management

### Learning objectives
- Create isolated Python environments
- Manage dependencies properly
- Understand why this matters for deployment

### Topics to study
- Why virtual environments matter
- Creating environments with `venv`
- Activating/deactivating environments
- Installing packages with pip
- Requirements files
- Understanding pip freeze

### Setup commands

**Create a project with virtual environment**:
```bash
# Create project directory
mkdir healthcare-project
cd healthcare-project

# Create virtual environment
python3 -m venv venv

# Activate environment (macOS)
source venv/bin/activate

# Your prompt should now show (venv)

# Install packages
pip install pandas numpy

# Save dependencies
pip freeze > requirements.txt

# Deactivate when done
deactivate
```

### VS Code configuration
1. Open your project folder in VS Code
2. Command Palette → "Python: Select Interpreter"
3. Choose the interpreter from your venv folder
4. VS Code will now use this environment automatically

### Practice exercises
1. Create a new project with its own virtual environment
2. Install pandas, numpy, and requests
3. Generate a requirements.txt
4. Delete the venv, recreate it, and restore packages from requirements.txt

---

## Week 7: Git, GitHub & Development Workflow

### Learning objectives
- Use Git for version control
- Collaborate and backup code with GitHub
- Follow a professional development workflow

### Topics to study
- Git fundamentals: init, add, commit, status, log
- Branching and merging basics
- Remote repositories with GitHub
- .gitignore for Python projects
- Writing good commit messages
- Basic GitHub workflow

### Setup commands

**Install Git**:
```bash
brew install git
```

**Configure Git**:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Initialize a repository**:
```bash
cd your-project
git init

# Create .gitignore
echo "venv/
__pycache__/
*.pyc
.env
.DS_Store" > .gitignore

# Initial commit
git add .
git commit -m "Initial commit"
```

### GitHub setup
1. Create a GitHub account if you don't have one
2. Create a new repository
3. Follow GitHub's instructions to push your local repo

### Practice exercises
1. Initialize Git in your Ward Management System project
2. Create a proper .gitignore
3. Push to GitHub
4. Practice making changes, committing, and pushing

### Healthcare mini-project: Portfolio Repository Setup
Create a GitHub repository called `healthcare-python-portfolio` that will hold all your projects from this curriculum. Set up:
- Clear README with your learning goals
- Proper .gitignore
- Folder structure for each phase
- Push your Phase 1 projects

---

## Phase 2 Checkpoint

Before moving to Phase 3, you should be able to:
- [ ] Create virtual environments for each project
- [ ] Manage dependencies with pip and requirements.txt
- [ ] Initialize Git repositories
- [ ] Write meaningful commit messages
- [ ] Push code to GitHub
- [ ] Your portfolio repository is set up with Phase 1 projects

---

# Phase 3: Databases & SQL
**Duration**: 4 weeks (~32 hours)  
**Goal**: Store and query healthcare data effectively

## Week 8: SQL Fundamentals

### Learning objectives
- Understand relational database concepts
- Write basic SQL queries
- Set up PostgreSQL locally

### Environment setup

**Install PostgreSQL**:
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Add to PATH** (add to ~/.zshrc):
```bash
export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"
```

**Create a database**:
```bash
createdb healthcare_db
psql healthcare_db
```

**Install VS Code extension**:
- Install "PostgreSQL" extension by Chris Kolkman

### Topics to study
- Relational database concepts (tables, rows, columns)
- Primary keys and data types
- CREATE TABLE statements
- INSERT, SELECT, UPDATE, DELETE
- WHERE clauses and operators
- ORDER BY and LIMIT
- NULL handling

### Practice exercises
1. Create a patients table and insert sample records
2. Write queries to find patients by various criteria
3. Update patient records
4. Create a medications table

---

## Week 9: Intermediate SQL

### Learning objectives
- Join data across tables
- Aggregate and group data
- Design normalized schemas

### Topics to study
- Table relationships (one-to-many, many-to-many)
- Foreign keys
- INNER JOIN, LEFT JOIN, RIGHT JOIN
- GROUP BY and aggregate functions (COUNT, SUM, AVG, MIN, MAX)
- HAVING clause
- Subqueries
- Basic normalization concepts

### Practice exercises
1. Create related tables (patients, encounters, diagnoses)
2. Write queries joining multiple tables
3. Calculate statistics grouped by diagnosis, provider, or time period

### Healthcare mini-project: Hospital Database Schema
Design and implement a database schema for a small hospital including:
- Patients (demographics, contact info)
- Providers (doctors, nurses, staff)
- Encounters (visits, admissions)
- Diagnoses (linked to encounters)
- Medications (prescriptions linked to patients and encounters)
- Vital signs (linked to encounters)

Write queries to answer:
- How many patients were seen last month?
- What are the most common diagnoses?
- Which providers have the highest patient volume?
- Average length of stay by diagnosis

---

## Week 10: Python Database Connectivity

### Learning objectives
- Connect Python to PostgreSQL
- Execute queries from Python
- Handle database errors

### Topics to study
- psycopg2 library
- Connection management
- Executing queries with parameters (preventing SQL injection)
- Fetching results
- Transaction management
- Connection pooling basics

### Setup
```bash
pip install psycopg2-binary
```

### Practice exercises
1. Write Python functions to CRUD patients
2. Build a script that imports CSV data into your database
3. Create a reporting script that queries and formats results

---

## Week 11: SQLAlchemy ORM

### Learning objectives
- Map Python classes to database tables
- Perform CRUD operations with ORM
- Write complex queries with SQLAlchemy

### Topics to study
- ORM concepts
- Defining models with SQLAlchemy
- Creating tables from models
- Session management
- CRUD operations
- Querying with filter, order_by, join
- Relationships between models

### Setup
```bash
pip install sqlalchemy
```

### Healthcare mini-project: Patient Records System
Rebuild your hospital database interaction using SQLAlchemy:
- Define models for all your tables
- Create a module with functions for common operations
- Build a command-line interface for:
  - Adding new patients
  - Recording encounters
  - Adding diagnoses and medications
  - Generating reports
- All data persists to PostgreSQL

---

## Phase 3 Checkpoint

Before moving to Phase 4, you should be able to:
- [ ] Design normalized database schemas
- [ ] Write complex SQL queries with joins and aggregations
- [ ] Connect Python to PostgreSQL
- [ ] Use SQLAlchemy ORM for database operations
- [ ] Complete the Patient Records System with full CRUD operations

---

# Phase 4: Data Analytics with Pandas
**Duration**: 4 weeks (~32 hours)  
**Goal**: Analyze healthcare data like a professional

## Week 12: Pandas Fundamentals

### Learning objectives
- Create and manipulate DataFrames
- Load data from various sources
- Perform basic data exploration

### Setup
```bash
pip install pandas numpy openpyxl
```

### Topics to study
- Series and DataFrame objects
- Creating DataFrames from various sources
- Reading CSV, Excel, JSON
- Basic attributes: shape, dtypes, columns, index
- Viewing data: head(), tail(), sample()
- Basic statistics: describe(), value_counts()
- Selecting columns and rows

### Practice exercises
1. Load CMS hospital quality data and explore its structure
2. Calculate basic statistics on patient datasets
3. Select and filter data by various criteria

### Dataset to use
Download "Hospital General Information" from:
https://data.cms.gov/provider-data/dataset/xubh-q36u

---

## Week 13: Data Cleaning & Transformation

### Learning objectives
- Handle missing data
- Transform and clean messy data
- Prepare data for analysis

### Topics to study
- Handling missing values: isna(), fillna(), dropna()
- Data type conversion
- String operations with .str accessor
- Renaming columns
- Replacing values
- Removing duplicates
- Apply and map functions

### Practice exercises
1. Clean a messy patient dataset (inconsistent formatting, missing values)
2. Standardize date formats and categorical values
3. Create derived columns from existing data

### Healthcare mini-project: CMS Data Cleaning Pipeline
Download multiple CMS datasets and build a cleaning pipeline that:
- Loads raw data
- Identifies and reports data quality issues
- Standardizes column names and formats
- Handles missing values appropriately
- Validates data against expected ranges
- Outputs clean, analysis-ready datasets

---

## Week 14: Data Analysis & Aggregation

### Learning objectives
- Group and aggregate data
- Merge datasets together
- Perform time-series analysis

### Topics to study
- GroupBy operations
- Aggregation functions
- Pivot tables and cross-tabulation
- Merging and joining DataFrames
- Concatenating DataFrames
- Working with dates and times
- Resampling time series data

### Practice exercises
1. Analyze hospital quality metrics by state and hospital type
2. Merge hospital information with readmission rates
3. Track trends over time in health metrics

### Healthcare mini-project: Hospital Quality Analysis
Using CMS data, create an analysis that:
- Merges hospital general info with quality metrics
- Calculates summary statistics by state and ownership type
- Identifies top and bottom performing hospitals
- Analyzes correlation between different quality measures
- Exports findings to formatted Excel reports

---

## Week 15: Advanced Pandas & Real-World Analysis

### Learning objectives
- Optimize pandas performance
- Handle large datasets
- Build reproducible analysis pipelines

### Topics to study
- Memory optimization techniques
- Chunked reading for large files
- Categorical data type
- Method chaining for readable code
- Creating analysis functions
- Saving intermediate results

### Healthcare capstone mini-project: Readmission Risk Analysis
Using CMS Hospital Readmissions data:
1. Load and clean the dataset
2. Analyze readmission rates by:
   - Geographic region
   - Hospital characteristics
   - Diagnosis category
3. Identify factors associated with higher readmission rates
4. Create a comprehensive report with:
   - Executive summary
   - Methodology
   - Key findings
   - Recommendations
5. Export to formatted Excel with multiple sheets

---

## Phase 4 Checkpoint

Before moving to Phase 5, you should be able to:
- [ ] Load data from CSV, Excel, databases into pandas
- [ ] Clean and transform messy data
- [ ] Perform groupby aggregations
- [ ] Merge multiple datasets
- [ ] Build reproducible analysis pipelines
- [ ] Complete the Readmission Risk Analysis project

---

# Phase 5: Data Visualization & Dashboards
**Duration**: 3 weeks (~24 hours)  
**Goal**: Communicate insights through visual analytics

## Week 16: Static Visualization

### Learning objectives
- Create publication-quality charts
- Choose appropriate visualizations
- Customize plot appearance

### Setup
```bash
pip install matplotlib seaborn plotly
```

### Topics to study
- Matplotlib fundamentals
- Figure and axes objects
- Common plot types: line, bar, scatter, histogram
- Customizing colors, labels, titles
- Subplots and layouts
- Seaborn for statistical visualization
- Saving figures

### Practice exercises
1. Create visualizations of hospital quality metrics
2. Build comparison charts across states
3. Design a multi-panel figure for a report

---

## Week 17: Interactive Visualization

### Learning objectives
- Create interactive charts
- Build drill-down visualizations
- Export for web display

### Topics to study
- Plotly Express for quick interactive charts
- Plotly Graph Objects for customization
- Interactive features: hover, zoom, filter
- Subplots and multiple axes
- Exporting to HTML

### Practice exercises
1. Convert static charts to interactive Plotly versions
2. Create a geographic visualization of health metrics
3. Build linked visualizations

---

## Week 18: Building Dashboards with Streamlit

### Learning objectives
- Build interactive web dashboards
- Connect dashboards to data sources
- Deploy dashboards for sharing

### Setup
```bash
pip install streamlit
```

### Topics to study
- Streamlit basics: text, data, charts
- Layout: columns, sidebar, expanders
- Input widgets: selectbox, slider, text input
- Caching for performance
- Session state
- Connecting to databases

### Healthcare capstone mini-project: Hospital Quality Dashboard
Build a Streamlit dashboard that:
- Loads CMS hospital quality data
- Provides filters for state, hospital type, ownership
- Displays key metrics and comparisons
- Shows interactive charts and maps
- Allows drilling down to individual hospitals
- Includes data download capability

```bash
# Run your dashboard
streamlit run dashboard.py
```

---

## Phase 5 Checkpoint

Before moving to Phase 6, you should be able to:
- [ ] Create static visualizations with matplotlib and seaborn
- [ ] Build interactive charts with Plotly
- [ ] Develop Streamlit dashboards with multiple pages
- [ ] Connect dashboards to data sources
- [ ] Complete the Hospital Quality Dashboard

---

# Phase 6: API Development with FastAPI
**Duration**: 5 weeks (~40 hours)  
**Goal**: Build production-ready healthcare APIs

## Week 19: HTTP & REST Fundamentals

### Learning objectives
- Understand how web APIs work
- Consume existing APIs
- Design RESTful endpoints

### Topics to study
- HTTP methods: GET, POST, PUT, DELETE, PATCH
- Status codes and their meanings
- Headers and content types
- Request and response bodies
- REST principles
- API documentation standards
- Using the requests library

### Setup
```bash
pip install requests
```

### Practice exercises
1. Consume the NPPES NPI Registry API
2. Fetch data from public health APIs
3. Design a RESTful API spec for a patient management system

### Healthcare exercise: NPI Lookup Tool
Build a command-line tool that:
- Takes a provider name or NPI as input
- Queries the NPPES API
- Parses and displays provider information
- Handles errors gracefully

NPPES API documentation: https://npiregistry.cms.hhs.gov/api-page

---

## Week 20: FastAPI Basics

### Learning objectives
- Create API endpoints
- Handle path and query parameters
- Return JSON responses

### Setup
```bash
pip install fastapi uvicorn
```

### Topics to study
- Creating a FastAPI application
- Path operations (routes)
- Path parameters
- Query parameters
- Request body
- Running with uvicorn
- Automatic documentation (Swagger UI, ReDoc)

### Practice exercises
1. Create a simple API with multiple endpoints
2. Implement path and query parameters
3. Build CRUD endpoints for a resource

### Basic FastAPI structure
```python
from fastapi import FastAPI

app = FastAPI(title="Healthcare API")

@app.get("/")
def root():
    return {"message": "Healthcare API is running"}

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    return {"patient_id": patient_id}

# Run with: uvicorn main:app --reload
```

---

## Week 21: Data Validation with Pydantic

### Learning objectives
- Define data models
- Validate request data
- Serialize responses

### Topics to study
- Pydantic models
- Field types and validation
- Optional and required fields
- Nested models
- Custom validators
- Response models

### Practice exercises
1. Create Pydantic models for patient data
2. Implement request validation
3. Build response models with computed fields

### Healthcare mini-project: Validated Patient API
Create an API with full validation for:
- Patient demographics (name format, date validation, etc.)
- Vital signs (range validation)
- Medications (drug name lookup, dosage validation)

The API should return helpful error messages for invalid data.

---

## Week 22: Database Integration

### Learning objectives
- Connect FastAPI to PostgreSQL
- Implement repository pattern
- Handle database sessions properly

### Topics to study
- SQLAlchemy with FastAPI
- Dependency injection
- Database session management
- CRUD operations through API
- Async database operations (optional)

### Practice exercises
1. Connect your patient API to PostgreSQL
2. Implement full CRUD operations
3. Add filtering and pagination

### Healthcare mini-project: Patient Records API
Build a complete API that:
- Manages patients, encounters, diagnoses
- Supports filtering by various criteria
- Implements pagination for large result sets
- Includes search functionality
- Stores all data in PostgreSQL

---

## Week 23: Authentication & Advanced Features

### Learning objectives
- Secure API endpoints
- Implement error handling
- Add logging and monitoring

### Topics to study
- API key authentication
- OAuth2 basics (conceptual)
- Exception handling
- Custom error responses
- Logging
- CORS configuration
- Rate limiting basics

### Practice exercises
1. Add API key authentication to your API
2. Implement proper error handling
3. Add request logging

### Healthcare capstone mini-project: Secure Healthcare API
Enhance your Patient Records API with:
- API key authentication
- Role-based access (admin, provider, readonly)
- Audit logging (who accessed what, when)
- Proper error handling with meaningful messages
- Request validation and sanitization
- Comprehensive API documentation

---

## Phase 6 Checkpoint

Before moving to Phase 7, you should be able to:
- [ ] Design RESTful APIs
- [ ] Build FastAPI applications with proper structure
- [ ] Validate data with Pydantic
- [ ] Connect APIs to PostgreSQL
- [ ] Implement authentication
- [ ] Complete the Secure Healthcare API project

---

# Phase 7: Testing & Code Quality
**Duration**: 2 weeks (~16 hours)  
**Goal**: Write reliable, maintainable code

## Week 24: Testing with pytest

### Learning objectives
- Write unit and integration tests
- Test FastAPI endpoints
- Achieve good test coverage

### Setup
```bash
pip install pytest pytest-cov httpx
```

### Topics to study
- pytest basics
- Test organization
- Fixtures
- Parametrized tests
- Testing FastAPI with TestClient
- Mocking external dependencies
- Test coverage

### Practice exercises
1. Write tests for your clinical calculator functions
2. Test your API endpoints
3. Achieve 80%+ test coverage

---

## Week 25: Code Quality Tools

### Learning objectives
- Format code consistently
- Catch errors with static analysis
- Document code properly

### Setup
```bash
pip install black ruff mypy
```

### Topics to study
- Code formatting with Black
- Linting with Ruff
- Type hints
- Type checking with mypy
- Docstrings and documentation
- Pre-commit hooks

### VS Code configuration
Add to settings.json:
```json
{
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "python.analysis.typeCheckingMode": "basic"
}
```

### Practice exercises
1. Add type hints to your API project
2. Set up Black and Ruff
3. Fix all linting errors
4. Add docstrings to public functions

---

## Phase 7 Checkpoint

Before moving to Phase 8, you should be able to:
- [ ] Write comprehensive tests with pytest
- [ ] Test API endpoints effectively
- [ ] Use Black for consistent formatting
- [ ] Add type hints to your code
- [ ] Document functions with docstrings
- [ ] All projects have tests and pass linting

---

# Phase 8: Containerization & Deployment
**Duration**: 3 weeks (~24 hours)  
**Goal**: Deploy your applications to the cloud

## Week 26: Docker Fundamentals

### Learning objectives
- Containerize Python applications
- Create efficient Docker images
- Use Docker Compose for multi-container apps

### Setup

**Install Docker Desktop for Mac**:
Download from https://www.docker.com/products/docker-desktop/

### Topics to study
- Container concepts
- Dockerfile syntax
- Building images
- Running containers
- Environment variables
- Docker Compose
- Volumes for data persistence

### Basic Dockerfile for FastAPI
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Practice exercises
1. Containerize your FastAPI application
2. Create a docker-compose.yml with API and PostgreSQL
3. Run your entire stack with one command

---

## Week 27: AWS Fundamentals

### Learning objectives
- Understand AWS core services
- Set up AWS account properly
- Deploy containers to AWS

### AWS Free Tier Setup
1. Create AWS account: https://aws.amazon.com/free/
2. Enable MFA on root account
3. Create an IAM user for development
4. Install AWS CLI

**Install AWS CLI**:
```bash
brew install awscli
aws configure
```

### Topics to study
- AWS account structure and IAM
- EC2 basics (we'll use for context, not direct deployment)
- RDS for managed PostgreSQL
- ECR for container registry
- ECS/Fargate for container deployment
- Basic networking (VPC, security groups)

### Practice exercises
1. Set up AWS account with proper security
2. Create an RDS PostgreSQL instance (free tier)
3. Push a Docker image to ECR

---

## Week 28: Production Deployment

### Learning objectives
- Deploy a complete application stack
- Configure environment properly
- Monitor deployed applications

### Deployment path: AWS App Runner
AWS App Runner is the simplest path to deploy containers on AWS. It handles load balancing, scaling, and SSL automatically.

### Topics to study
- AWS App Runner service
- Environment configuration
- Secrets management with AWS Secrets Manager
- Basic monitoring with CloudWatch
- Custom domains (optional)

### Healthcare mini-project: Deploy Your API
Deploy your Secure Healthcare API to AWS:
1. Push Docker image to ECR
2. Create RDS PostgreSQL database
3. Configure App Runner service
4. Set up environment variables and secrets
5. Test your live API
6. Set up basic monitoring

### Cost management
- Use AWS Free Tier services where possible
- Set up billing alerts
- Shut down unused resources
- Expected cost: $0-15/month for learning

---

## Phase 8 Checkpoint

Before moving to Capstone, you should be able to:
- [ ] Create Docker images for your applications
- [ ] Use Docker Compose for local development
- [ ] Deploy containers to AWS
- [ ] Manage environment variables and secrets
- [ ] Monitor deployed applications
- [ ] Your API is running live on AWS

---

# Phase 9: Capstone Project
**Duration**: 4 weeks (~32 hours)  
**Goal**: Build a portfolio-worthy healthcare application

## Healthcare Analytics Platform

Build a complete system that demonstrates all your skills:

### Project requirements

**Backend API** (FastAPI):
- Patient management endpoints
- Encounter and diagnosis tracking
- Analytics endpoints (aggregations, trends)
- Secure authentication
- Full test coverage
- OpenAPI documentation

**Database** (PostgreSQL):
- Normalized schema
- Proper indexes
- Sample data seeding

**Analytics** (Pandas):
- Data quality reports
- Statistical analysis endpoints
- Trend calculations

**Dashboard** (Streamlit):
- Patient population overview
- Quality metrics visualization
- Drill-down capabilities
- Configurable filters

**Deployment** (AWS):
- Containerized with Docker
- API deployed to App Runner
- Database on RDS
- Dashboard deployed separately (Streamlit Cloud free tier)

### Week 29-30: Build core functionality
- Set up project structure
- Implement database schema
- Build API endpoints
- Create basic dashboard

### Week 31: Polish and testing
- Write comprehensive tests
- Add authentication
- Improve error handling
- Enhance documentation

### Week 32: Deploy and document
- Deploy to AWS
- Write README with setup instructions
- Record a demo video
- Add to portfolio

### Project structure
```
healthcare-analytics-platform/
├── api/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── tests/
├── dashboard/
│   └── app.py
├── database/
│   ├── migrations/
│   └── seed_data/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Phase 9 Checkpoint (Final)

Your capstone project should demonstrate:
- [ ] Clean, well-organized code
- [ ] Full CRUD API with authentication
- [ ] Data validation and error handling
- [ ] Database design and queries
- [ ] Data analysis capabilities
- [ ] Interactive visualization
- [ ] Comprehensive tests
- [ ] Docker containerization
- [ ] Cloud deployment
- [ ] Professional documentation

---

# Appendix A: VS Code Setup

## Recommended extensions
- Python (Microsoft)
- Pylance
- Black Formatter
- Ruff
- PostgreSQL
- Docker
- GitLens
- Thunder Client (API testing)

## settings.json
```json
{
    "editor.formatOnSave": true,
    "editor.rulers": [88],
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "python.analysis.typeCheckingMode": "basic",
    "python.testing.pytestEnabled": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true
    }
}
```

---

# Appendix B: Common Commands Reference

## Python & pip
```bash
# Create virtual environment
python3 -m venv venv

# Activate (macOS)
source venv/bin/activate

# Install from requirements
pip install -r requirements.txt

# Save dependencies
pip freeze > requirements.txt
```

## PostgreSQL
```bash
# Start PostgreSQL
brew services start postgresql@15

# Connect to database
psql healthcare_db

# Common psql commands
\dt          # List tables
\d tablename # Describe table
\q           # Quit
```

## Git
```bash
# Initialize repository
git init

# Stage and commit
git add .
git commit -m "message"

# Push to GitHub
git push origin main

# Create branch
git checkout -b feature-name
```

## Docker
```bash
# Build image
docker build -t myapp .

# Run container
docker run -p 8000:8000 myapp

# Docker Compose
docker-compose up -d
docker-compose down
```

## FastAPI
```bash
# Run development server
uvicorn main:app --reload

# Run with specific host/port
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Streamlit
```bash
# Run dashboard
streamlit run app.py
```

## Testing
```bash
# Run tests
pytest

# With coverage
pytest --cov=app --cov-report=html
```

---

# Appendix C: Healthcare Data Resources

## Public datasets
- CMS Provider Data: https://data.cms.gov/
- CDC Data: https://www.cdc.gov/datastatistics/
- HealthData.gov: https://healthdata.gov/
- Synthea (synthetic data): https://synthetichealth.github.io/synthea/

## APIs
- NPPES NPI Registry: https://npiregistry.cms.hhs.gov/api-page
- OpenFDA: https://open.fda.gov/apis/
- CDC APIs: https://data.cdc.gov/

## Standards
- HL7 FHIR: https://www.hl7.org/fhir/
- ICD-10: https://www.cms.gov/medicare/coding-billing/icd-10-codes
- SNOMED CT: https://www.snomed.org/

---

# Learning Progress Tracker

Use this to track your progress through the curriculum:

## Phase 1: Python Fundamentals
- [ ] Week 1: Core Syntax
- [ ] Week 2: Control Flow & Data Structures
- [ ] Week 3: Functions & Modules
- [ ] Week 4: File Handling
- [ ] Week 5: OOP Basics
- [ ] **Mini-project: Ward Management System**

## Phase 2: Environment & Tooling
- [ ] Week 6: Virtual Environments
- [ ] Week 7: Git & GitHub
- [ ] **Portfolio repository set up**

## Phase 3: Databases & SQL
- [ ] Week 8: SQL Fundamentals
- [ ] Week 9: Intermediate SQL
- [ ] Week 10: Python Database Connectivity
- [ ] Week 11: SQLAlchemy ORM
- [ ] **Mini-project: Patient Records System**

## Phase 4: Data Analytics
- [ ] Week 12: Pandas Fundamentals
- [ ] Week 13: Data Cleaning
- [ ] Week 14: Analysis & Aggregation
- [ ] Week 15: Advanced Pandas
- [ ] **Mini-project: Readmission Risk Analysis**

## Phase 5: Visualization
- [ ] Week 16: Static Visualization
- [ ] Week 17: Interactive Visualization
- [ ] Week 18: Streamlit Dashboards
- [ ] **Mini-project: Hospital Quality Dashboard**

## Phase 6: API Development
- [ ] Week 19: HTTP & REST
- [ ] Week 20: FastAPI Basics
- [ ] Week 21: Pydantic Validation
- [ ] Week 22: Database Integration
- [ ] Week 23: Authentication
- [ ] **Mini-project: Secure Healthcare API**

## Phase 7: Testing & Quality
- [ ] Week 24: pytest
- [ ] Week 25: Code Quality Tools
- [ ] **All projects have tests**

## Phase 8: Deployment
- [ ] Week 26: Docker
- [ ] Week 27: AWS Fundamentals
- [ ] Week 28: Production Deployment
- [ ] **API deployed to AWS**

## Phase 9: Capstone
- [ ] Week 29-30: Core Functionality
- [ ] Week 31: Polish & Testing
- [ ] Week 32: Deploy & Document
- [ ] **Capstone complete and deployed**

---

*Curriculum version 1.0 - Created for Jason's Python backend development journey*
