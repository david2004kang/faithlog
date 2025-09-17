# GitHub Setup Commands

## Milestones to Create

1. **v0.1: Ultra-thin MVP**
   - Description: Build minimal viable product to validate core Bible reading check-in loop
   - Due date: 2 days from start

2. **v0.2: Customizable Reading Plans**
   - Description: Allow users to choose and customize Bible reading plans
   - Due date: 5 days from start

3. **v0.3: Basic Social Features**
   - Description: Add friend system and basic sharing functionality
   - Due date: 9 days from start

4. **v0.4: Reflection Sharing & Visibility**
   - Description: Enhanced reflection sharing with visibility controls
   - Due date: 12 days from start

5. **v0.5: Ask Pastor Upgrade**
   - Description: Upgrade Ask Pastor to full private messaging system
   - Due date: 16 days from start

6. **v0.6: Mini-games & Achievements**
   - Description: Add mini-games and achievement system for rewards
   - Due date: 21 days from start

7. **v0.7: Management & Moderation**
   - Description: Complete management and content moderation features
   - Due date: 24 days from start

8. **v1.0: Production Ready**
   - Description: Production environment deployment with PostgreSQL and Docker
   - Due date: 28 days from start

## Labels to Create

### Priority Labels
- `priority: high` (color: #d73a49) - High priority tasks
- `priority: medium` (color: #fbca04) - Medium priority tasks  
- `priority: low` (color: #0e8a16) - Low priority tasks

### Type Labels
- `type: feature` (color: #a2eeef) - New feature development
- `type: bug` (color: #d73a49) - Bug fixes
- `type: enhancement` (color: #84b6eb) - Enhancement to existing features
- `type: documentation` (color: #0075ca) - Documentation updates
- `type: testing` (color: #f9d0c4) - Testing related tasks

### Component Labels
- `component: backend` (color: #b60205) - Backend/Django related
- `component: frontend` (color: #1d76db) - Frontend/Templates related
- `component: database` (color: #5319e7) - Database related
- `component: deployment` (color: #0e8a16) - Deployment related
- `component: auth` (color: #fbca04) - Authentication related

### Status Labels
- `status: ready` (color: #0e8a16) - Ready to work on
- `status: in-progress` (color: #fbca04) - Currently being worked on
- `status: blocked` (color: #d73a49) - Blocked by dependencies
- `status: review` (color: #5319e7) - Ready for review

## Issues to Create for v0.1 MVP

### Backend Setup Issues
1. **Set up Django project structure**
   - Labels: `type: feature`, `component: backend`, `priority: high`
   - Milestone: v0.1
   - Description: Create Django project with proper app structure and basic configuration

2. **Create data models for MVP**
   - Labels: `type: feature`, `component: backend`, `component: database`, `priority: high`
   - Milestone: v0.1
   - Description: Implement User, ReadingPlan, UserPlan, ReadingProgress, Reflection, and AskTicket models

3. **Set up basic authentication**
   - Labels: `type: feature`, `component: auth`, `priority: high`
   - Milestone: v0.1
   - Description: Configure Django authentication system with user registration and login

### Frontend Issues
4. **Create base template and styling**
   - Labels: `type: feature`, `component: frontend`, `priority: high`
   - Milestone: v0.1
   - Description: Set up base HTML template with Tailwind CSS integration

5. **Build daily reading check-in page**
   - Labels: `type: feature`, `component: frontend`, `priority: high`
   - Milestone: v0.1
   - Description: Create main page showing today's Bible passage with check-in functionality

6. **Create reflection input form**
   - Labels: `type: feature`, `component: frontend`, `priority: medium`
   - Milestone: v0.1
   - Description: Build form for users to input daily reflections

7. **Design completion reward page**
   - Labels: `type: feature`, `component: frontend`, `priority: medium`
   - Milestone: v0.1
   - Description: Create page showing completion badge/reward after check-in

### Backend Logic Issues
8. **Implement daily progress tracking**
   - Labels: `type: feature`, `component: backend`, `priority: high`
   - Milestone: v0.1
   - Description: Build logic to track and update daily reading progress

9. **Create Ask Pastor form handling**
   - Labels: `type: feature`, `component: backend`, `priority: medium`
   - Milestone: v0.1
   - Description: Implement form processing for Ask Pastor questions

10. **Set up admin interface**
    - Labels: `type: feature`, `component: backend`, `priority: medium`
    - Milestone: v0.1
    - Description: Configure Django admin for managing users, plans, and questions

### Deployment Issues
11. **Create deployment script**
    - Labels: `type: feature`, `component: deployment`, `priority: high`
    - Milestone: v0.1
    - Description: Write deployment script for SSH-based deployment

12. **Set up SQLite database**
    - Labels: `type: feature`, `component: database`, `component: deployment`, `priority: high`
    - Milestone: v0.1
    - Description: Configure SQLite database for MVP deployment

### Testing Issues
13. **Write basic tests for models**
    - Labels: `type: testing`, `component: backend`, `priority: medium`
    - Milestone: v0.1
    - Description: Create unit tests for data models

14. **Test deployment process**
    - Labels: `type: testing`, `component: deployment`, `priority: high`
    - Milestone: v0.1
    - Description: Verify deployment works on target server

### Documentation Issues
15. **Write deployment README**
    - Labels: `type: documentation`, `priority: medium`
    - Milestone: v0.1
    - Description: Document deployment process and server setup requirements
