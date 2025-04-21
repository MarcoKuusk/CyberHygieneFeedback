# Cyber Hygiene Feedback Project
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
## Overview
The Cyber Hygiene Feedback project is designed to help organizations and employees assess their cybersecurity practices through structured questionnaires. The project generates tailored feedback based on the responses provided, enabling users to identify areas for improvement in their cyber hygiene.

## Project Structure
```
cyber-hygiene-feedback
├── src
│   ├── main.py                # Entry point for the application
│   ├── feedback_generator.py   # Contains the FeedbackGenerator class
│   ├── data
│   │   ├── employee_questionnaire.json  # Employee questionnaire data
│   │   └── organization_questionnaire.json  # Organization questionnaire data
│   └── utils
│       └── scoring.py         # Scoring functions for feedback generation
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd cyber-hygiene-feedback
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

This will initiate the feedback generation process, loading the questionnaires and producing feedback based on user responses.

## Feedback Generation Process
1. The application loads the employee and organization questionnaires from the JSON files.
2. It collects responses from users.
3. The `FeedbackGenerator` class processes the responses and calculates scores using the scoring functions.
4. Tailored feedback is generated and presented to the users, highlighting strengths and areas for improvement in their cyber hygiene practices.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.