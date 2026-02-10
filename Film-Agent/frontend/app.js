/**
 * AI Film Studio - Frontend Application
 * 
 * JavaScript for interacting with the AI Film Agent API.
 */

// API Configuration
const API_BASE = window.location.origin;
let currentJobId = null;
let statusPolling = null;

// DOM Elements
const elements = {
    generateForm: document.getElementById('generateForm'),
    generateBtn: document.getElementById('generateBtn'),
    progressSection: document.getElementById('progressSection'),
    resultSection: document.getElementById('resultSection'),
    jobsList: document.getElementById('jobsList'),
    agentsGrid: document.getElementById('agentsGrid'),
    prompt: document.getElementById('prompt'),
    genre: document.getElementById('genre'),
    length: document.getElementById('length'),
    format: document.getElementById('format'),
    jobId: document.getElementById('jobId'),
    status: document.getElementById('status'),
    progressFill: document.getElementById('progressFill'),
    currentStep: document.getElementById('currentStep'),
    downloadVideo: document.getElementById('downloadVideo'),
    createNew: document.getElementById('createNew')
};

// ============ API Functions ============

/**
 * Generate a new film
 */
async function generateFilm(data) {
    const response = await fetch(`${API_BASE}/api/generate`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
        throw new Error('Failed to generate film');
    }

    return response.json();
}

/**
 * Get job status
 */
async function getJobStatus(jobId) {
    const response = await fetch(`${API_BASE}/api/status/${jobId}`);
    
    if (!response.ok) {
        throw new Error('Failed to get job status');
    }

    return response.json();
}

/**
 * Get list of agents
 */
async function getAgents() {
    const response = await fetch(`${API_BASE}/api/agents`);
    
    if (!response.ok) {
        throw new Error('Failed to get agents');
    }

    return response.json();
}

/**
 * Get recent jobs
 */
async function getJobs() {
    const response = await fetch(`${API_BASE}/api/jobs`);
    
    if (!response.ok) {
        throw new Error('Failed to get jobs');
    }

    return response.json();
}

/**
 * Cancel a job
 */
async function cancelJob(jobId) {
    const response = await fetch(`${API_BASE}/api/jobs/${jobId}`, {
        method: 'DELETE'
    });

    if (!response.ok) {
        throw new Error('Failed to cancel job');
    }

    return response.json();
}

// ============ UI Functions ============

/**
 * Show progress section
 */
function showProgress(jobId) {
    elements.progressSection.style.display = 'block';
    elements.resultSection.style.display = 'none';
    elements.jobId.textContent = `Job ID: ${jobId}`;
    elements.status.textContent = 'Queued';
    elements.progressFill.style.width = '0%';
    elements.currentStep.textContent = 'Waiting to start...';
}

/**
 * Update progress display
 */
function updateProgress(status) {
    elements.status.textContent = status.status.charAt(0).toUpperCase() + status.status.slice(1);
    elements.progressFill.style.width = `${status.progress}%`;
    
    // Format step name
    const stepName = status.current_step
        .replace(/_/g, ' ')
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
    
    elements.currentStep.textContent = `Current: ${stepName}`;
}

/**
 * Show result section
 */
function showResult(jobId) {
    elements.progressSection.style.display = 'none';
    elements.resultSection.style.display = 'block';
    elements.downloadVideo.href = `${API_BASE}/api/download/${jobId}`;
}

/**
 * Render agents grid
 */
function renderAgents(agents) {
    const emojiMap = {
        'director': '🎭',
        'screenwriter': '✍️',
        'cinematographer': '🎥',
        'editor': '✂️',
        'sound_designer': '🎵',
        'vfx': '✨'
    };

    elements.agentsGrid.innerHTML = agents.map(agent => `
        <div class="agent-card">
            <h3>${emojiMap[agent.name] || '🤖'} ${agent.name.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</h3>
            <p>${agent.description}</p>
            <div class="agent-methods">
                ${agent.methods.map(method => `
                    <span class="method-tag">${method.replace(/_/g, ' ')}</span>
                `).join('')}
            </div>
        </div>
    `).join('');
}

/**
 * Render jobs list
 */
function renderJobs(jobs) {
    if (jobs.length === 0) {
        elements.jobsList.innerHTML = '<p class="empty-state">No jobs yet. Create your first film!</p>';
        return;
    }

    elements.jobsList.innerHTML = jobs.map(job => `
        <div class="job-item ${job.status}" onclick="checkJobStatus('${job.job_id}')">
            <div class="job-info">
                <h4>${job.request?.prompt?.substring(0, 50) || 'Untitled'}...</h4>
                <p>${new Date(job.started_at).toLocaleString()}</p>
            </div>
            <span class="job-status ${job.status}">${job.status}</span>
        </div>
    `).join('');
}

/**
 * Check job status and poll
 */
async function checkJobStatus(jobId) {
    try {
        const status = await getJobStatus(jobId);
        
        if (currentJobId === jobId) {
            updateProgress(status);
            
            if (status.status === 'completed') {
                clearInterval(statusPolling);
                showResult(jobId);
            } else if (status.status === 'failed' || status.status === 'cancelled') {
                clearInterval(statusPolling);
                alert(`Job ${status.status}: ${status.error || 'Unknown error'}`);
            }
        }
    } catch (error) {
        console.error('Error checking status:', error);
    }
}

// ============ Event Handlers ============

/**
 * Form submission handler
 */
async function handleGenerate(e) {
    e.preventDefault();

    const data = {
        prompt: elements.prompt.value.trim(),
        genre: elements.genre.value,
        length: elements.length.value,
        format: elements.format.value
    };

    if (!data.prompt) {
        alert('Please enter a film prompt');
        return;
    }

    // Disable button
    elements.generateBtn.disabled = true;
    const btnText = elements.generateBtn.querySelector('.btn-text');
    const btnLoading = elements.generateBtn.querySelector('.btn-loading');
    btnText.style.display = 'none';
    btnLoading.style.display = 'inline';

    try {
        const response = await generateFilm(data);
        currentJobId = response.job_id;
        
        showProgress(response.job_id);
        
        // Start polling for status
        statusPolling = setInterval(() => checkJobStatus(response.jobId), 2000);
        
        // Load jobs list
        loadJobs();
        
    } catch (error) {
        alert('Error generating film: ' + error.message);
        elements.generateBtn.disabled = false;
    }
}

/**
 * Create new film handler
 */
function handleCreateNew() {
    elements.resultSection.style.display = 'none';
    elements.progressSection.style.display = 'none';
    elements.prompt.value = '';
    currentJobId = null;
    elements.generateBtn.disabled = false;
}

// ============ Initialization ============

/**
 * Load initial data
 */
async function loadData() {
    try {
        // Load agents
        const agents = await getAgents();
        renderAgents(agents);
        
        // Load jobs
        loadJobs();
        
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

/**
 * Load jobs list
 */
async function loadJobs() {
    try {
        const jobs = await getJobs();
        renderJobs(jobs.reverse());
    } catch (error) {
        console.error('Error loading jobs:', error);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Attach event listeners
    elements.generateForm.addEventListener('submit', handleGenerate);
    elements.createNew.addEventListener('click', handleCreateNew);
    
    // Load initial data
    loadData();
});

// Make functions available globally
window.checkJobStatus = checkJobStatus;
