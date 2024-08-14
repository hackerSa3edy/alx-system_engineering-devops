# The Unexpected Turn: A Graduation Project Postmortem

![CoverImage](./grad_project_postmortem.jpg)

### **Issue Summary**

**Duration of the Outage:** 30 minutes (10:00 AM \- 10:30 AM GMT)

Before our project discussion, we discovered a critical issue: a new feature's URLs and routes were still set to localhost in all JS files. We had tested only in the localhost environment and failed to check the deployment. An hour before the presentation, we noticed the feature didn't work. We quickly replaced all localhost URLs with the domain name using the `sed` command, pushed the changes, and the CI/CD pipeline redeployed the project.

### **Timeline**

* **10:00 AM GMT:** Issue detected by a team member during a pre-presentation check.
* **10:07 AM GMT:** Team member noticed the new feature was not functioning as expected.
* **10:10 AM GMT:** Initial assumption was that there was a deployment issue; checked deployment logs.
* **10:17 AM GMT:** Realized the issue was due to URLs pointing to localhost in the JavaScript files.
* **10:21 AM GMT:** Ran the `sed` command to replace localhost URLs with the production domain in all files.
* **10:23 AM GMT:** Pushed changes to the repository.
* **10:25 AM GMT:** CI/CD pipeline deployed the changes.
* **10:29 AM GMT:** Verified that the new feature was functioning correctly on the production domain.

### **Root Cause and Resolution**

**Root Cause:**

* The root cause was the hard-coded localhost URLs in the JavaScript files. During the final day of development, a new feature was implemented and tested on a localhost environment. The routes and URLs remained unchanged when the code was pushed to the repository and subsequently deployed.

**Resolution:**

* The issue was resolved by using the `sed` command to replace all instances of "localhost" with the production domain in the JavaScript files. This change was then pushed to the repository, and the CI/CD pipeline automatically redeployed the updated code.

### **Corrective and Preventative Measures**

**Improvements/Fixes:**

* Implement a more robust testing procedure that includes testing all features on the deployment environment.
* Ensure that all environment-specific variables are configurable and not hard-coded.
* Introduce pre-deployment checks to catch similar issues before they reach production.

**Tasks:**

1. **Update Testing Procedures:** Revise the testing checklist to include verification of all features on the production environment.
2. **Environment Configuration:** Refactor the codebase to use environment variables for URLs and routes instead of hard-coded values.
3. **Pre-Deployment Checks:** Implement automated pre-deployment checks to ensure that all URLs and routes point to the correct environment.
4. **CI/CD Pipeline Enhancement:** Add a step in the CI/CD pipeline to validate environment-specific configurations before deployment.
5. **Documentation:** Update project documentation to highlight the importance of environment-specific testing and configuration management.

###### The original [post](https://docs.google.com/document/d/1By4yQN-_j6Wvjm8B7OHzlWDLec4eELt_q1ydaIp7QMM/edit?usp=sharing "The Unexpected Turn: A Graduation Project Postmortem").
