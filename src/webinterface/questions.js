export const employeeQuestions = {
  categories: [
    {
      category: "Password & Access Management",
      questions: [
        {
          question: "Do you use unique passwords for different accounts (work and personal)?",
          answers: [
            { option: "No", score: 0 },
            { option: "I reuse passwords across many accounts", score: 1 },
            { option: "I use different passwords but sometimes reuse old ones", score: 2 },
            { option: "I use different passwords and change them occasionally", score: 3 },
            { option: "I use different, strong passwords and a password manager", score: 4 }
          ]
        },
        {
          question: "Do you store your passwords securely?",
          answers: [
            { option: "No, I write them down or save them in unprotected files", score: 0 },
            { option: "I use a simple password-protected document", score: 1 },
            { option: "I memorize most but reuse some weak passwords", score: 2 },
            { option: "I use a password manager but sometimes write down passwords", score: 3 },
            { option: "I exclusively use a password manager or secure method", score: 4 }
          ]
        },
        {
          question: "Do you use multi-factor authentication (MFA) when available?",
          answers: [
            { option: "No", score: 0 },
            { option: "Only for highly sensitive accounts", score: 1 },
            { option: "I enable MFA for some work accounts", score: 2 },
            { option: "I enable MFA for most work accounts", score: 3 },
            { option: "I enable MFA for all possible accounts", score: 4 }
          ]
        },
        {
          question: "Do you lock your computer and devices when leaving them unattended?",
          answers: [
            { option: "No", score: 0 },
            { option: "Sometimes, but I often forget", score: 1 },
            { option: "I lock them when in public spaces", score: 2 },
            { option: "I lock them in most situations", score: 3 },
            { option: "I always lock them, even at home", score: 4 }
          ]
        }
      ]
    },
    {
      category: "Phishing Awareness & Email Security",
      questions: [
        {
          question: "Would you recognize a phishing email?",
          answers: [
            { option: "No, I am not familiar with phishing attacks", score: 0 },
            { option: "I have heard of phishing but wouldn’t always recognize it", score: 1 },
            { option: "I recognize some phishing attempts but have fallen for them before", score: 2 },
            { option: "I can recognize most phishing emails and verify links before clicking", score: 3 },
            { option: "I always verify sender details, URLs, and report phishing attempts", score: 4 }
          ]
        },
        {
          question: "Have you received cybersecurity training on phishing attacks?",
          answers: [
            { option: "No", score: 0 },
            { option: "Once, but I do not remember much", score: 1 },
            { option: "Occasionally, but not regularly", score: 2 },
            { option: "I receive training at least once a year", score: 3 },
            { option: "I regularly receive training and participate in phishing tests", score: 4 }
          ]
        },
        {
          question: "Do you verify sender addresses before clicking on links or opening attachments?",
          answers: [
            { option: "Never", score: 0 },
            { option: "Rarely", score: 1 },
            { option: "Sometimes, if an email looks suspicious", score: 2 },
            { option: "Often, but I have clicked on a suspicious link before", score: 3 },
            { option: "Always, I verify senders and links before clicking", score: 4 }
          ]
        },
        {
          question: "Do you report suspicious emails to IT/security?",
          answers: [
            { option: "No", score: 0 },
            { option: "I delete them but don’t report them", score: 1 },
            { option: "I report some emails but not consistently", score: 2 },
            { option: "I usually report them", score: 3 },
            { option: "I always report phishing attempts", score: 4 }
          ]
        }
      ]
    },
    {
      category: "Device & Data Security",
      questions: [
        {
          question: "Do you regularly update your work device (OS, apps, security patches)?",
          answers: [
            { option: "No, I ignore updates", score: 0 },
            { option: "Sometimes, but I delay updates", score: 1 },
            { option: "I update most things within a few weeks", score: 2 },
            { option: "I update devices promptly when notified", score: 3 },
            { option: "I always update immediately or have auto-updates enabled", score: 4 }
          ]
        },
        {
          question: "Do you use personal USB drives or unauthorized software on work devices?",
          answers: [
            { option: "Yes, regularly", score: 0 },
            { option: "Sometimes, if necessary", score: 1 },
            { option: "Rarely, only when required", score: 2 },
            { option: "Almost never, and only after IT approval", score: 3 },
            { option: "Never, I follow IT policies strictly", score: 4 }
          ]
        },
        {
          question: "Do you use encrypted communication channels for sensitive work discussions?",
          answers: [
            { option: "No", score: 0 },
            { option: "Sometimes, but not always", score: 1 },
            { option: "I use encrypted channels when instructed", score: 2 },
            { option: "I use them for most sensitive communications", score: 3 },
            { option: "I always use encrypted channels", score: 4 }
          ]
        }
      ]
    },
    {
      category: "Remote Work & Public Network Security",
      questions: [
        {
          question: "Do you use a VPN or secured connection when working remotely?",
          answers: [
            { option: "No", score: 0 },
            { option: "Only for highly sensitive work", score: 1 },
            { option: "Sometimes, but not consistently", score: 2 },
            { option: "Mostly, unless I forget", score: 3 },
            { option: "Always, I never work remotely without a VPN", score: 4 }
          ]
        },
        {
          question: "Do you avoid using public Wi-Fi for work tasks?",
          answers: [
            { option: "No, I use public Wi-Fi without precautions", score: 0 },
            { option: "Sometimes, but I don’t take security measures", score: 1 },
            { option: "I use public Wi-Fi but with some security precautions", score: 2 },
            { option: "I avoid public Wi-Fi when possible", score: 3 },
            { option: "I never use public Wi-Fi for work tasks", score: 4 }
          ]
        },
        {
          question: "Do you ensure that family members or friends do not use your work devices?",
          answers: [
            { option: "No, I share my work device", score: 0 },
            { option: "Sometimes, but only for non-work purposes", score: 1 },
            { option: "Rarely, but they have accessed it before", score: 2 },
            { option: "Almost never, except in emergencies", score: 3 },
            { option: "Never, I strictly keep work devices private", score: 4 }
          ]
        }
      ]
    },
    {
      category: "Incident Reporting & Cybersecurity Culture",
      questions: [
        {
          question: "Do you know how to report a cybersecurity incident?",
          answers: [
            { option: "No", score: 0 },
            { option: "I think I know, but I’m not sure", score: 1 },
            { option: "I know where to report but have never done it", score: 2 },
            { option: "I know how to report and have done it before", score: 3 },
            { option: "I actively report security incidents and encourage others to do so", score: 4 }
          ]
        },
        {
          question: "Do you feel your organization provides adequate cybersecurity training?",
          answers: [
            { option: "No, I have never received training", score: 0 },
            { option: "Some training, but not enough", score: 1 },
            { option: "Training is provided, but it could be better", score: 2 },
            { option: "Training is good, but I’d like more practical exercises", score: 3 },
            { option: "Training is excellent and prepares me well for threats", score: 4 }
          ]
        },
        {
          question: "Have you participated in simulated cybersecurity exercises (e.g., phishing tests)?",
          answers: [
            { option: "No", score: 0 },
            { option: "Once, but not recently", score: 1 },
            { option: "Occasionally, but not regularly", score: 2 },
            { option: "Frequently, at least once per year", score: 3 },
            { option: "Regularly, with multiple tests and feedback", score: 4 }
          ]
        },
        {
          question: "Do you think your organization prioritizes cybersecurity?",
          answers: [
            { option: "No, it is not a priority", score: 0 },
            { option: "There are some efforts, but they are weak", score: 1 },
            { option: "Cybersecurity is important but not enforced well", score: 2 },
            { option: "Cybersecurity is taken seriously", score: 3 },
            { option: "Cybersecurity is a top priority and well-integrated", score: 4 }
          ]
        },
        {
          question: "Would you feel comfortable reporting a mistake or security issue to IT/security?",
          answers: [
            { option: "No, I am afraid of consequences", score: 0 },
            { option: "I am unsure if I should report mistakes", score: 1 },
            { option: "I would report it, but I worry about judgment", score: 2 },
            { option: "I would report it without hesitation", score: 3 },
            { option: "I actively encourage others to report issues", score: 4 }
          ]
        }
      ]
    }
  ]
};

export const organizationQuestions = {
  categories: [
    {
      category: "Identity & Access Management",
      questions: [
        {
          question: "Do you enforce multi-factor authentication (MFA) for all critical systems?",
          answers: [
            { option: "No", score: 0 },
            { option: "Only for administrators", score: 1 },
            { option: "For some employees", score: 2 },
            { option: "For most employees", score: 3 },
            { option: "Mandatory for all employees", score: 4 }
          ]
        },
        {
          question: "How often are user access privileges reviewed?",
          answers: [
            { option: "Never", score: 0 },
            { option: "Annually", score: 1 },
            { option: "Semi-annually", score: 2 },
            { option: "Quarterly", score: 3 },
            { option: "Monthly or continuously monitored", score: 4 }
          ]
        },
        {
          question: "Are strong password policies enforced (length, complexity, expiration, reuse restrictions)?",
          answers: [
            { option: "No", score: 0 },
            { option: "Basic enforcement, but not monitored", score: 1 },
            { option: "Enforced for administrators only", score: 2 },
            { option: "Enforced for most employees", score: 3 },
            { option: "Strictly enforced for all employees", score: 4 }
          ]
        },
        {
          question: "Are inactive or terminated employee accounts deactivated immediately?",
          answers: [
            { option: "No formal process", score: 0 },
            { option: "Deactivated within a month", score: 1 },
            { option: "Deactivated within a week", score: 2 },
            { option: "Deactivated within 48 hours", score: 3 },
            { option: "Deactivated immediately upon termination", score: 4 }
          ]
        },
        {
          question: "Do employees have access only to the data and systems required for their job roles (least privilege principle)?",
          answers: [
            { option: "No restrictions", score: 0 },
            { option: "Limited restrictions", score: 1 },
            { option: "Some departments follow least privilege", score: 2 },
            { option: "Most departments follow least privilege", score: 3 },
            { option: "Strict least privilege policy enforced across the organization", score: 4 }
          ]
        },
        {
          question: "Does your organization provide and require the use of password managers?",
          answers: [
            { option: "No", score: 0 },
            { option: "Available but not required", score: 1 },
            { option: "Required for administrators", score: 2 },
            { option: "Required for most employees", score: 3 },
            { option: "Required for all employees", score: 4 }
          ]
        }
      ]
    },
    {
      category: "Software & Patch Management",
      questions: [
        {
          question: "Does your organization have a centralized system for managing software updates?",
          answers: [
            { option: "No", score: 0 },
            { option: "Updates are done manually by users", score: 1 },
            { option: "IT manages updates but not automatically", score: 2 },
            { option: "Centralized automatic updates for some systems", score: 3 },
            { option: "Fully automated patch management", score: 4 }
          ]
        },
        {
          question: "Do you perform regular vulnerability scans?",
          answers: [
            { option: "No", score: 0 },
            { option: "Annually", score: 1 },
            { option: "Semi-annually", score: 2 },
            { option: "Quarterly", score: 3 },
            { option: "Monthly or continuously monitored", score: 4 }
          ]
        },
        {
          question: "Are antivirus and endpoint protection solutions installed and updated?",
          answers: [
            { option: "No protection in place", score: 0 },
            { option: "Installed but not updated regularly", score: 1 },
            { option: "Installed and updated semi-regularly", score: 2 },
            { option: "Installed and updated regularly", score: 3 },
            { option: "Installed, updated, and centrally monitored", score: 4 }
          ]
        },
        {
          question: "How often are operating systems, software, and applications updated?",
          answers: [
            { option: "Never or rarely", score: 0 },
            { option: "Only critical updates applied manually", score: 1 },
            { option: "Updates applied within 3 months of release", score: 2 },
            { option: "Updates applied within 1 month of release", score: 3 },
            { option: "Automated patching system in place", score: 4 }
          ]
        }
      ]
    },
    {
      category: "Data Classification & Protection",
      questions: [
        {
          question: "Does your organization have a formal data classification policy?",
          answers: [
            { option: "No classification policy", score: 0 },
            { option: "Basic classification exists", score: 1 },
            { option: "Classified data has access restrictions", score: 2 },
            { option: "Classified data is encrypted", score: 3 },
            { option: "Data is encrypted and regularly audited", score: 4 }
          ]
        },
        {
          question: "Are sensitive files and communications encrypted at rest and in transit?",
          answers: [
            { option: "No encryption", score: 0 },
            { option: "Basic encryption but not enforced", score: 1 },
            { option: "Encryption applied to some systems", score: 2 },
            { option: "Encryption applied to most systems", score: 3 },
            { option: "Full encryption for all sensitive data", score: 4 }
          ]
        }
      ]
    },
    {
      category: "Backup & Recovery",
      questions: [
        {
          question: "Do you have a data backup and recovery process?",
          answers: [
            { option: "No backup system in place", score: 0 },
            { option: "Backups exist but are not performed regularly", score: 1 },
            { option: "Backups are performed regularly but not tested for recovery", score: 2 },
            { option: "Backups are performed regularly and tested occasionally", score: 3 },
            { option: "Backups are performed regularly, encrypted, stored securely, and tested frequently", score: 4 }
          ]
        },
        {
          question: "How frequently are data backups performed?",
          answers: [
            { option: "No backup system in place", score: 0 },
            { option: "Monthly", score: 1 },
            { option: "Weekly", score: 2 },
            { option: "Daily", score: 3 },
            { option: "Continuous real-time backups", score: 4 }
          ]
        }
      ]
    },
    {
      category: "Security Awareness & Training",
      questions: [
        {
          question: "How often do employees receive cybersecurity awareness training?",
          answers: [
            { option: "Never", score: 0 },
            { option: "Once during onboarding", score: 1 },
            { option: "Annually", score: 2 },
            { option: "Semi-annually", score: 3 },
            { option: "Regular ongoing training with simulations", score: 4 }
          ]
        },
        {
          question: "Are simulated phishing attacks conducted to test employee awareness?",
          answers: [
            { option: "No", score: 0 },
            { option: "Once per year", score: 1 },
            { option: "Semi-annually", score: 2 },
            { option: "Quarterly", score: 3 },
            { option: "Monthly with detailed reporting", score: 4 }
          ]
        },
        {
          question: "Do employees receive role-specific cybersecurity training?",
          answers: [
            { option: "No", score: 0 },
            { option: "Basic training for all", score: 1 },
            { option: "Role-specific training for some", score: 2 },
            { option: "Role-specific training for most", score: 3 },
            { option: "Continuous training tailored to roles", score: 4 }
          ]
        },
        {
          question: "Do employees know how to report security incidents and suspicious activity?",
          answers: [
            { option: "No awareness", score: 0 },
            { option: "Some employees know", score: 1 },
            { option: "A formal reporting system exists but is not well known", score: 2 },
            { option: "A formal system exists and most employees are aware", score: 3 },
            { option: "A well-established system exists with clear reporting procedures", score: 4 }
          ]
        }
      ]
    }
  ]
};