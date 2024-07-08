# CourseAutomator

## Overview
CourseAutomator is a Python bot that automates the process of adding and dropping courses for Tamkang University students using Selenium to interact with the university's course selection system, including handling audio CAPTCHA verification.

## Features
- Automates login to Tamkang University's course selection system
- Handles audio CAPTCHA verification
- Adds and drops courses based on user input
- Provides logging for course addition and removal status

## Demo
<video width="320" height="240" controls>
  <source src="demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Installation
### Prerequisites
- Python 3.x
- Google Chrome browser
- ChromeDriver

### Installation Steps
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/CourseAutomator.git
   ```
2. Navigate to the project directory:
   ```
   cd CourseAutomator
   ```
3. Install dependencies:
   ```
   pip install selenium
   ```

## Usage
1. Update the script with your student number and password:
   ```
   bot = CourseBot('stdNo', 'pwd')
   ```
2. Define the courses to add and drop:
   ```
   drop_list = ['0991','3076']
   add_list = ['2336','2337']
   ```
3. Run the script:
   ```
   python main.py
   ```

## Contact Information
If you have any questions, please submit an issue.
