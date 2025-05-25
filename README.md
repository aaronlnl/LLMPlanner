# LLMPlanner (Work in progress)

LLMPlanner is a schedule planner web application that helps users manage their calendar and events with the assistance of an AI assistant.

## Features

### Core Features
- **Sign Up / Sign In:** User authentication for secure access.
- **View Calendar:** See your events in a calendar view.
- **Event Management:** Manually add, edit, and delete events.
- **AI Assistant Chat:**
  - Ask about your schedule (e.g., "When is my next appointment with Dr. Smith?")
  - Get today’s schedule summary.
  - Add, edit, or delete events via natural language.

  ## Getting Started

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt

3. **Configure your database settings**  
   Edit `LLMPlanner/settings.py` to set up your MySQL database credentials.

4. **Run database migrations**
   ```sh
   python manage.py migrate
   ```

5. **Start the development server**
   ```sh
   python manage.py runserver
   ```