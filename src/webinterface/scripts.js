document.addEventListener('DOMContentLoaded', function () {
    // State variables
    let currentEmpQuestion = 1;
    let currentOrgQuestion = 1;
    let totalEmpQuestions = 0;
    let totalOrgQuestions = 0;

    // Show home by default
    document.getElementById('home').classList.remove('hidden');

    // Button event listeners
    document.getElementById('startEmployee').addEventListener('click', function () {
        showSection('employeeAssessment');
        resetAssessment('employee');
    });

    document.getElementById('startOrganization').addEventListener('click', function () {
        showSection('organizationAssessment');
        resetAssessment('organization');
    });

    document.getElementById('generateReport').addEventListener('click', function () {
        showSection('unifiedFeedback');
    });

    // Navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const target = this.getAttribute('href').substring(1);
            if (target === 'employee') {
                showSection('employeeAssessment');
            } else if (target === 'organization') {
                showSection('organizationAssessment');
            } else if (target === 'unified') {
                showSection('unifiedFeedback');
            } else if (target === 'about') {
                showSection('about');
            } else {
                showSection('home');
            }
        });
    });

    // Employee assessment controls
    document.getElementById('employeeNext').addEventListener('click', function () {
        if (!validateQuestion('employee', currentEmpQuestion)) return;

        if (currentEmpQuestion < totalEmpQuestions) {
            showQuestion('employee', ++currentEmpQuestion);
            updateEmployeeProgress();
        } else {
            showSection('employeeFeedback');
        }
    });

    document.getElementById('employeeBack').addEventListener('click', function () {
        if (currentEmpQuestion > 1) {
            showQuestion('employee', --currentEmpQuestion);
            updateEmployeeProgress();
        }
    });

    // Organization assessment controls
    document.getElementById('orgNext').addEventListener('click', function () {
        if (!validateQuestion('organization', currentOrgQuestion)) return;

        if (currentOrgQuestion < totalOrgQuestions) {
            showQuestion('organization', ++currentOrgQuestion);
            updateOrgProgress();
        } else {
            showSection('organizationFeedback');
        }
    });

    document.getElementById('orgBack').addEventListener('click', function () {
        if (currentOrgQuestion > 1) {
            showQuestion('organization', --currentOrgQuestion);
            updateOrgProgress();
        }
    });

    // Utility Functions
    function showSection(sectionId) {
        document.querySelectorAll('main > section').forEach(section => {
            section.classList.add('hidden');
        });
        document.getElementById(sectionId).classList.remove('hidden');
    }

    function validateQuestion(assessmentType, questionNumber) {
        const containerId = `${assessmentType}Assessment`;
        const question = document.querySelector(`#${containerId} .question[data-question="${questionNumber}"]`);

        if (!question) return false;

        const inputs = question.querySelectorAll('input[type="radio"]');
        const error = question.querySelector('.error-message');

        const answered = Array.from(inputs).some(input => input.checked);

        if (!answered) {
            error.classList.remove('hidden');
            question.classList.add('shake');
            setTimeout(() => question.classList.remove('shake'), 500);
            return false;
        }

        error.classList.add('hidden');
        return true;
    }

    function resetAssessment(type) {
        if (type === 'employee') {
            currentEmpQuestion = 1;
            showQuestion('employee', currentEmpQuestion);
            updateEmployeeProgress();
            document.getElementById('employeeBack').disabled = true;
        } else {
            currentOrgQuestion = 1;
            showQuestion('organization', currentOrgQuestion);
            updateOrgProgress();
            document.getElementById('orgBack').disabled = true;
        }
    }

    function showQuestion(type, questionNumber) {
        const containerId = `${type}Assessment`;
        document.querySelectorAll(`#${containerId} .question`).forEach(q => {
            q.classList.add('hidden');
        });
        const target = document.querySelector(`#${containerId} .question[data-question="${questionNumber}"]`);
        if (target) target.classList.remove('hidden');

        // Enable/Disable Back button
        if (type === 'employee') {
            document.getElementById('employeeBack').disabled = questionNumber === 1;
        } else {
            document.getElementById('orgBack').disabled = questionNumber === 1;
        }
    }

    function updateEmployeeProgress() {
        const progress = (currentEmpQuestion / totalEmpQuestions) * 100;
        document.getElementById('employeeProgressBar').style.width = `${progress}%`;
        document.getElementById('employeeProgressText').textContent = `Question ${currentEmpQuestion} of ${totalEmpQuestions}`;
    }

    function updateOrgProgress() {
        const progress = (currentOrgQuestion / totalOrgQuestions) * 100;
        document.getElementById('orgProgressBar').style.width = `${progress}%`;
        document.getElementById('orgProgressText').textContent = `Question ${currentOrgQuestion} of ${totalOrgQuestions}`;
    }

    async function loadQuestions(type) {
        const filePath = type === 'employee'
            ? 'src/data/employee_questionnaire.json'
            : 'src/data/organization_questionnaire.json';

        try {
            const response = await fetch(filePath);
            const data = await response.json();

            const containerId = type === 'employee' ? 'employeeAssessment' : 'organizationAssessment';
            const container = document.querySelector(`#${containerId} .questions-container`);
            container.innerHTML = ''; // Clear existing questions

            let questionList = [];

            if (type === 'employee') {
                data.questions.forEach(category => {
                    category.questions.forEach(q => {
                        questionList.push({ ...q, category: category.category });
                    });
                });
            } else {
                questionList = data.questions;
            }

            questionList.forEach((question, index) => {
                container.innerHTML += renderQuestion(question, index + 1, type);
            });

            // Set total number dynamically
            if (type === 'employee') {
                totalEmpQuestions = questionList.length;
            } else {
                totalOrgQuestions = questionList.length;
            }
        } catch (error) {
            console.error(`Failed to load ${type} questions:`, error);
        }
    }

    function renderQuestion(question, questionNumber, type) {
        const answersHtml = question.answers.map(answer => `
            <label class="block mb-2">
                <input type="radio" name="${type}-question-${questionNumber}" value="${answer.value}" class="mr-2">
                ${answer.text || answer.option}
            </label>
        `).join('');

        return `
            <div class="question hidden" data-question="${questionNumber}">
                <h3 class="text-lg font-bold mb-4">
                    ${question.category ? `<span class="text-accent">${question.category}:</span> ` : ''}
                    ${question.question}
                </h3>
                ${answersHtml}
                <p class="error-message text-red-500 hidden">Please select an answer.</p>
            </div>
        `;
    }

    // Load questions after page ready
    loadQuestions('employee');
    loadQuestions('organization');
});
