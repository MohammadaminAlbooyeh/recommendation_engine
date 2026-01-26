const noteForm = document.getElementById('note-form');
const notesDiv = document.getElementById('notes');
const noteIdInput = document.getElementById('note-id');
const titleInput = document.getElementById('title');
const contentInput = document.getElementById('content');
const formTitle = document.getElementById('form-title');
const submitBtn = document.getElementById('submit-btn');
const cancelBtn = document.getElementById('cancel-btn');
const noteCount = document.getElementById('note-count');
const toastContainer = document.getElementById('toast-container');

document.addEventListener('DOMContentLoaded', loadNotes);
noteForm.addEventListener('submit', handleFormSubmit);
cancelBtn.addEventListener('click', resetForm);

async function loadNotes() {
    try {
        const response = await fetch('/api/notes/');
        const data = await response.json();
        renderNotes(data);
        noteCount.innerText = `${data.length} note${data.length !== 1 ? 's' : ''}`;
    } catch (error) {
        showToast('Failed to load notes', 'error');
    }
}

function renderNotes(notes) {
    notesDiv.innerHTML = '';
    
    if (notes.length === 0) {
        notesDiv.innerHTML = `
            <div style="grid-column: 1/-1; text-align: center; padding: 4rem 2rem; background: white; border-radius: 1.25rem; border: 2px dashed #e2e8f0;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📝</div>
                <h3 style="margin: 0; color: var(--text-dark);">Your desk is clean</h3>
                <p style="color: var(--text-gray); margin: 0.5rem 0 0 0;">Start capturing your brilliant ideas on the left.</p>
            </div>
        `;
        return;
    }

    notes.forEach(note => {
        const card = document.createElement('div');
        card.className = 'note-card';
        card.innerHTML = `
            <h3>${escapeHtml(note.title)}</h3>
            <p>${escapeHtml(note.content)}</p>
            <div class="note-footer">
                <span class="note-date">${new Date(note.created_at).toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' })}</span>
                <div class="actions">
                    <button class="action-btn" onclick="editNote(${note.id})" title="Edit">
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
                    </button>
                    <button class="action-btn delete" onclick="deleteNote(${note.id})" title="Delete">
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                    </button>
                </div>
            </div>
        `;
        notesDiv.appendChild(card);
    });
}

async function handleFormSubmit(e) {
    e.preventDefault();
    submitBtn.disabled = true;
    submitBtn.innerText = 'Processing...';

    const id = noteIdInput.value;
    const note = { title: titleInput.value, content: contentInput.value };
    
    try {
        const method = id ? 'PUT' : 'POST';
        const url = id ? `/api/notes/${id}` : '/api/notes/';
        
        const response = await fetch(url, {
            method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(note)
        });

        if (response.ok) {
            showToast(id ? 'Note updated successfully' : 'Idea captured!');
            resetForm();
            loadNotes();
        } else {
            throw new Error();
        }
    } catch (error) {
        showToast('Something went wrong', 'error');
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerText = id ? 'Update Note' : 'Save Note';
    }
}

async function deleteNote(id) {
    if (!confirm('Shall we erase this memory?')) return;
    try {
        const response = await fetch(\`/api/notes/\${id}\`, { method: 'DELETE' });
        if (response.ok) {
            showToast('Note deleted');
            loadNotes();
        }
    } catch (error) {
        showToast('Failed to delete', 'error');
    }
}

async function editNote(id) {
    try {
        const response = await fetch(\`/api/notes/\${id}\`);
        const note = await response.json();
        
        noteIdInput.value = note.id;
        titleInput.value = note.title;
        contentInput.value = note.content;
        
        formTitle.innerText = 'Refine Note';
        submitBtn.innerText = 'Update Note';
        cancelBtn.style.display = 'block';
        
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (error) {
        showToast('Error fetching details', 'error');
    }
}

function resetForm() {
    noteForm.reset();
    noteIdInput.value = '';
    formTitle.innerText = 'New Jotting';
    submitBtn.innerText = 'Save Note';
    cancelBtn.style.display = 'none';
}

function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.style.borderLeft = `4px solid \${type === 'success' ? '#10b981' : '#ef4444'}\`;
    toast.innerText = message;
    toastContainer.appendChild(toast);
    
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}