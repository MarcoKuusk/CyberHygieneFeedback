const employeeQuestions = {
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
                        { option: "I have heard of phishing but wouldn't always recognize it", score: 1 },
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
                        { option: "I delete them but don't report them", score: 1 },
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
                        { option: "Sometimes, but I don't take security measures", score: 1 },
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
                        { option: "I think I know, but I'm not sure", score: 1 },
                        { option: "I know where to report but have never done it", score: 2 },
                        { option: "I know how to report and have done it before", score: 3 },
                        { option: "I actively report security incidents and encourage others to do so", score: 4 }
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

const organizationQuestions = {
    categories: [
        {
            category: "Identity & Access Management",
            questions: [
                {
                    question: "Do you enforce multi-factor authentication (MFA) for all critical systems (e.g., email, financial software, customer databases)?",
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
                },
                {
                    question: "Are backups stored securely in an offsite or cloud location?",
                    answers: [
                        { option: "No backups", score: 0 },
                        { option: "Backups stored on-premises only", score: 1 },
                        { option: "Offsite backups stored but not encrypted", score: 2 },
                        { option: "Offsite backups stored with encryption", score: 3 },
                        { option: "Encrypted offsite backups with multi-location redundancy", score: 4 }
                    ]
                },
                {
                    question: "Are backups regularly tested for successful restoration?",
                    answers: [
                        { option: "Never", score: 0 },
                        { option: "Annually", score: 1 },
                        { option: "Semi-annually", score: 2 },
                        { option: "Quarterly", score: 3 },
                        { option: "Monthly or more frequently", score: 4 }
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
                },
                {
                    question: "Do employees understand and actively participate in cybersecurity practices (e.g., reporting suspicious activity, following policies)?",
                    answers: [
                        { option: "No expectations or policies in place", score: 0 },
                        { option: "Basic policies exist, but no training provided", score: 1 },
                        { option: "Employees receive occasional awareness training", score: 2 },
                        { option: "Employees actively report threats and follow security procedures", score: 3 },
                        { option: "A strong cybersecurity culture is embedded across the organization", score: 4 }
                    ]
                }
            ]
        },
        {
            category: "Network & Endpoint Security",
            questions: [
                {
                    question: "Does your organization enforce secure Wi-Fi policies (e.g., WPA3, no default credentials, guest network separation)?",
                    answers: [
                        { option: "No", score: 0 },
                        { option: "Basic security, default passwords exist", score: 1 },
                        { option: "Secure settings, but not reviewed", score: 2 },
                        { option: "Regular security reviews", score: 3 },
                        { option: "Enforced policies with monitoring", score: 4 }
                    ]
                },
                {
                    question: "Are all devices protected with endpoint security solutions (e.g., EDR, antivirus, firewalls)?",
                    answers: [
                        { option: "No protection", score: 0 },
                        { option: "Basic antivirus only", score: 1 },
                        { option: "Antivirus & basic firewall", score: 2 },
                        { option: "Advanced endpoint detection and response (EDR)", score: 3 },
                        { option: "Fully managed EDR with advanced threat detection tools", score: 4 }
                    ]
                },
                {
                    question: "How is remote access to company systems secured?",
                    answers: [
                        { option: "No security measures", score: 0 },
                        { option: "Basic VPN access", score: 1 },
                        { option: "VPN with MFA", score: 2 },
                        { option: "Strict access controls partially implemented", score: 3 },
                        { option: "Full Zero Trust Model with strict controls", score: 4 }
                    ]
                }
            ]
        },
        {
            category: "Incident Response & Business Continuity",
            questions: [
                {
                    question: "Does your organization have a documented incident response plan?",
                    answers: [
                        { option: "No", score: 0 },
                        { option: "Exists but never tested", score: 1 },
                        { option: "Tested once a year", score: 2 },
                        { option: "Tested semi-annually", score: 3 },
                        { option: "Regularly tested with live drills", score: 4 }
                    ]
                },
                {
                    question: "Do you have a cybersecurity expert or service provider to help during emergencies (e.g., ransomware, data breaches)?",
                    answers: [
                        { option: "No", score: 0 },
                        { option: "Evaluating options", score: 1 },
                        { option: "External partner but no SLA", score: 2 },
                        { option: "Partner on retainer", score: 3 },
                        { option: "24/7 emergency support", score: 4 }
                    ]
                },
                {
                    question: "Are security incidents logged and analyzed for patterns?",
                    answers: [
                        { option: "No logging system", score: 0 },
                        { option: "Some manual logging", score: 1 },
                        { option: "Automated logging but no analysis", score: 2 },
                        { option: "Automated logging with periodic analysis", score: 3 },
                        { option: "Advanced logging with continuous monitoring and AI-driven analysis", score: 4 }
                    ]
                },
                {
                    question: "Is there a cyber insurance policy to mitigate financial losses from cyber incidents?",
                    answers: [
                        { option: "No", score: 0 },
                        { option: "Evaluating options", score: 1 },
                        { option: "Basic coverage", score: 2 },
                        { option: "Moderate coverage with defined incident response support", score: 3 },
                        { option: "Comprehensive cyber insurance with crisis management", score: 4 }
                    ]
                },
                {
                    question: "How quickly are cybersecurity incidents required to be reported internally?",
                    answers: [
                        { option: "No formal reporting process", score: 0 },
                        { option: "Within a week", score: 1 },
                        { option: "Within 72 hours", score: 2 },
                        { option: "Within 24 hours", score: 3 },
                        { option: "Immediately", score: 4 }
                    ]
                }
            ]
        },
        {
            category: "Compliance & Regulatory Alignment",
            questions: [
                {
                    question: "Does your organization follow industry-specific cybersecurity regulations or standards (e.g., ISO 27001, E-ITS, NIS2)?",
                    answers: [
                        { option: "No compliance efforts", score: 0 },
                        { option: "Aware of requirements but not implemented", score: 1 },
                        { option: "Partially compliant", score: 2 },
                        { option: "Mostly compliant", score: 3 },
                        { option: "Fully compliant with audits", score: 4 }
                    ]
                },
                {
                    question: "Are third-party vendors required to meet cybersecurity standards?",
                    answers: [
                        { option: "No security requirements for vendors", score: 0 },
                        { option: "Basic security requirements but not enforced", score: 1 },
                        { option: "Some vendors required to meet security standards", score: 2 },
                        { option: "Most vendors required to meet security standards", score: 3 },
                        { option: "All vendors required to meet strict security standards with audits", score: 4 }
                    ]
                }
            ]
        },
        {
            category: "Physical Security",
            questions: [
                {
                    question: "Are devices (laptops, servers, etc.) physically secured against unauthorized access?",
                    answers: [
                        { option: "No physical security measures", score: 0 },
                        { option: "Basic measures (e.g., office locks)", score: 1 },
                        { option: "Sensitive devices secured", score: 2 },
                        { option: "Most devices secured", score: 3 },
                        { option: "All devices secured and monitored", score: 4 }
                    ]
                }
            ]
        },
        {
            category: "Third-Party Risk",
            questions: [
                {
                    question: "Do you assess vendors/partners for cybersecurity practices before sharing data or system access?",
                    answers: [
                        { option: "No vendor assessments", score: 0 },
                        { option: "Informal verbal assurances", score: 1 },
                        { option: "Basic checklist for critical vendors", score: 2 },
                        { option: "Formal assessments for all vendors", score: 3 },
                        { option: "Continuous monitoring of vendor security", score: 4 }
                    ]
                }
            ]
        },
        {
            category: "Remote Work Security",
            questions: [
                {
                    question: "Are employees required to use VPNs or secure networks when accessing company data remotely?",
                    answers: [
                        { option: "No requirements", score: 0 },
                        { option: "Recommended but not enforced", score: 1 },
                        { option: "Enforced for administrators", score: 2 },
                        { option: "Enforced for most employees", score: 3 },
                        { option: "Mandatory for all remote access", score: 4 }
                    ]
                }
            ]
        }
    ]
};
// Flatten questions into single arrays
const flattenedEmployeeQuestions = employeeQuestions.categories.flatMap(category => category.questions);
const flattenedOrgQuestions = organizationQuestions.categories.flatMap(category => category.questions);

// Navigation between sections
document.addEventListener('DOMContentLoaded', function() {
    // Show home by default
    document.getElementById('home').classList.remove('hidden');

    // Button event listeners
    document.getElementById('startEmployee').addEventListener('click', () => {
        startAssessment('employee');
    });

    document.getElementById('startOrganization').addEventListener('click', () => {
        startAssessment('organization');
    });

    document.getElementById('generateReport').addEventListener('click', () => {
        showSection('unifiedFeedback');
    });

    // Navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = this.getAttribute('href').substring(1);
            if (target === 'employee') {
                startAssessment('employee');
            } else if (target === 'organization') {
                startAssessment('organization');
            } else {
                showSection(target === 'unified' ? 'unifiedFeedback' : target || 'home');
            }
        });
    });

    // Variables to track assessments
    const state = {
        employee: { currentQuestion: 0, answers: [] },
        organization: { currentQuestion: 0, answers: [] }
    };

    const questionData = {
        employee: {
            questions: flattenedEmployeeQuestions,
            containerId: 'employeeQuestionContainer',
            backBtnId: 'employeeBack',
            nextBtnId: 'employeeNext',
            progressBarId: 'employeeProgressBar',
            progressTextId: 'employeeProgressText',
            feedbackSection: 'employeeFeedback',
        },
        organization: {
            questions: flattenedOrgQuestions,
            containerId: 'orgQuestionContainer',
            backBtnId: 'orgBack',
            nextBtnId: 'orgNext',
            progressBarId: 'orgProgressBar',
            progressTextId: 'orgProgressText',
            feedbackSection: 'organizationFeedback',
        }
    };

    function startAssessment(type) {
        resetAssessment(type);
        showSection(`${type}Assessment`);
    }

    function resetAssessment(type) {
        const data = state[type];
        const config = questionData[type];

        data.currentQuestion = 0;
        data.answers.length = 0;

        renderQuestion(type, 0);
        updateProgress(type);

        document.getElementById(config.backBtnId).disabled = true;
        document.getElementById(config.nextBtnId).textContent = 'Next';
    }

    function renderQuestion(type, index) {
        const config = questionData[type];
        const container = document.getElementById(config.containerId);
        const question = config.questions[index];

        let html = `
            <div class="question" data-index="${index}">
                <p class="text-xl mb-6">${question.question}</p>
                <div class="space-y-4">
        `;

        question.answers.forEach((answer, i) => {
            html += `
                <div class="flex items-center">
                    <input type="radio" id="${type}Option${index}_${i}" name="${type}Answer${index}" 
                        value="${answer.score}" class="h-4 w-4 text-accent focus:ring-accent border-gray-300">
                    <label for="${type}Option${index}_${i}" class="ml-3 block text-textlight">${answer.option}</label>
                </div>
            `;
        });

        html += `
                </div>
                <div class="error-message">Please select an answer to continue</div>
            </div>
        `;

        container.innerHTML = html;

        const savedAnswer = state[type].answers[index];
        if (savedAnswer !== undefined) {
            document.querySelector(`input[name="${type}Answer${index}"][value="${savedAnswer}"]`).checked = true;
        }
    }

    function validateQuestion(type, index) {
        const selected = document.querySelector(`input[name="${type}Answer${index}"]:checked`);
        const error = document.querySelector(`#${questionData[type].containerId} .error-message`);

        if (!selected) {
            if (error) error.style.display = 'block';
            return false;
        }

        if (error) error.style.display = 'none';
        state[type].answers[index] = parseInt(selected.value);
        return true;
    }

    function updateProgress(type) {
        const data = state[type];
        const config = questionData[type];
        const progress = ((data.currentQuestion + 1) / config.questions.length) * 100;

        document.getElementById(config.progressBarId).style.width = `${progress}%`;
        document.getElementById(config.progressTextId).textContent = 
            `Question ${data.currentQuestion + 1} of ${config.questions.length}`;
    }

    function handleNext(type) {
        const data = state[type];
        const config = questionData[type];

        if (!validateQuestion(type, data.currentQuestion)) return;

        if (data.currentQuestion < config.questions.length - 1) {
            data.currentQuestion++;
            renderQuestion(type, data.currentQuestion);
            updateProgress(type);
            document.getElementById(config.backBtnId).disabled = false;

            if (data.currentQuestion === config.questions.length - 1) {
                document.getElementById(config.nextBtnId).textContent = 'Submit';
            }
        } else {
            showSection(config.feedbackSection);
        }
    }

    function handleBack(type) {
        const data = state[type];
        const config = questionData[type];

        if (data.currentQuestion > 0) {
            data.currentQuestion--;
            renderQuestion(type, data.currentQuestion);
            updateProgress(type);

            if (data.currentQuestion === 0) {
                document.getElementById(config.backBtnId).disabled = true;
            }

            document.getElementById(config.nextBtnId).textContent = 
                data.currentQuestion === config.questions.length - 1 ? 'Submit' : 'Next';
        }
    }

    // Attach assessment button handlers
    ['employee', 'organization'].forEach(type => {
        document.getElementById(questionData[type].nextBtnId).addEventListener('click', () => handleNext(type));
        document.getElementById(questionData[type].backBtnId).addEventListener('click', () => handleBack(type));
    });

    function showSection(sectionId) {
        document.querySelectorAll('main > section').forEach(section => {
            section.classList.add('hidden');
        });

        document.getElementById(sectionId).classList.remove('hidden');

        navLinks.forEach(link => {
            link.classList.remove('active');
        });

        const sectionMap = {
            home: 0,
            employeeAssessment: 1,
            employeeFeedback: 1,
            organizationAssessment: 2,
            organizationFeedback: 2,
            unifiedFeedback: 3,
            about: 4
        };

        if (sectionMap.hasOwnProperty(sectionId)) {
            document.querySelectorAll('.nav-link')[sectionMap[sectionId]].classList.add('active');
        }

        window.scrollTo(0, 0);
    }
});