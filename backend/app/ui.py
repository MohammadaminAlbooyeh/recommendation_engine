from nicegui import ui
from .services import note_service
from .db.database import SessionLocal
from .schemas.note import NoteCreate

def init(fastapi_app):
    @ui.page('/')
    def main_page():
        db = SessionLocal()
        
        # State
        editing_id = None

        def refresh_notes():
            notes_container.clear()
            notes = note_service.get_notes(db)
            if not notes:
                with notes_container:
                    ui.label('No notes yet!').classes('text-gray-500 text-center w-full py-10')
                return
            
            for note in notes:
                with notes_container:
                    with ui.card().classes('w-full p-0 overflow-hidden bg-white hover:shadow-2xl transition-all duration-300 rounded-2xl border-l-8 border-indigo-500 shadow-sm group'):
                        with ui.row().classes('w-full p-6 items-start'):
                            with ui.column().classes('flex-1'):
                                ui.label(note.title).classes('text-xl font-bold text-slate-800 mb-1 group-hover:text-indigo-600 transition-colors')
                                ui.label(note.content).classes('text-slate-600 leading-relaxed whitespace-pre-wrap')
                                with ui.row().classes('items-center gap-2 mt-4 text-slate-400'):
                                    ui.icon('schedule', size='14px')
                                    ui.label(f'Created: {note.created_at.strftime("%b %d, %H:%M")}').classes('text-xs font-semibold uppercase tracking-wider')
                            
                            with ui.column().classes('items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity'):
                                ui.button(icon='edit', on_click=lambda n=note: start_edit(n)).props('flat round color=indigo').classes('hover:bg-indigo-50')
                                ui.button(icon='delete', on_click=lambda n=note: remove_note(n.id)).props('flat round color=pink').classes('hover:bg-pink-50')

        def start_edit(note):
            nonlocal editing_id
            editing_id = note.id
            title_input.value = note.title
            content_input.value = note.content
            submit_btn.text = 'Update Note'
            cancel_btn.set_visibility(True)
            ui.scroll_to(0)

        def reset_form():
            nonlocal editing_id
            editing_id = None
            title_input.value = ''
            content_input.value = ''
            submit_btn.text = 'Save Note'
            cancel_btn.set_visibility(False)

        async def save_note():
            if not title_input.value or not content_input.value:
                ui.notify('Please fill all fields', type='warning')
                return
            
            note_data = NoteCreate(title=title_input.value, content=content_input.value)
            
            if editing_id:
                note_service.update_note(db, editing_id, note_data)
                ui.notify('Note updated!')
            else:
                note_service.create_note(db, note_data)
                ui.notify('Idea captured!')
            
            reset_form()
            refresh_notes()

        async def remove_note(note_id):
            note_service.delete_note(db, note_id)
            ui.notify('Note deleted', type='negative')
            refresh_notes()

        # UI Layout
        ui.query('body').style('background: radial-gradient(circle at top left, #eef2ff 0%, #f8fafc 100%); min-height: 100vh;')
        
        with ui.header().classes('bg-indigo-700/90 backdrop-blur-md items-center justify-between py-4 px-8 shadow-lg fixed'):
            with ui.row().classes('items-center gap-3'):
                ui.icon('auto_awesome').classes('text-3xl text-yellow-300')
                ui.label('Smart Notes').classes('text-2xl font-black text-white tracking-widest uppercase')
            with ui.row().classes('items-center gap-4'):
                ui.button(icon='add', on_click=lambda: ui.scroll_to(0)).props('flat white').classes('text-white')

        with ui.row().classes('w-full max-w-7xl mx-auto pt-24 pb-12 px-6 gap-10 items-start'):
            # Sidebar / Form - Sticky
            with ui.column().classes('w-full md:w-[380px] sticky top-24'):
                with ui.card().classes('w-full p-8 bg-white/90 backdrop-blur-xl rounded-3xl shadow-2xl border border-indigo-50'):
                    with ui.row().classes('items-center gap-2 mb-6'):
                        ui.icon('edit_note', size='2rem').classes('text-indigo-600')
                        ui.label('Create New').classes('text-2xl font-bold text-slate-800')
                    
                    title_input = ui.input(label='Subject', placeholder='Title of your note...').classes('w-full mb-4').props('outlined rounded')
                    content_input = ui.textarea(label='Content', placeholder='Write something amazing...').classes('w-full mb-6').props('outlined rounded rows=6')
                    
                    with ui.column().classes('w-full gap-3'):
                        submit_btn = ui.button('Save Note', on_click=save_note).classes('w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-xl py-4 shadow-lg transform transition-all hover:scale-[1.02]')
                        cancel_btn = ui.button('Discard Changes', on_click=reset_form).classes('w-full').props('flat color=grey')
                        cancel_btn.set_visibility(False)

            # Main Feed
            with ui.column().classes('flex-1'):
                with ui.row().classes('w-full justify-between items-end mb-8 border-b border-indigo-100 pb-4'):
                    with ui.column():
                        ui.label('Your Collection').classes('text-3xl font-black text-slate-800 tracking-tight')
                        ui.label('Manage your thoughts and ideas').classes('text-slate-500 font-medium')
                    
                    # Search placeholder (could be functional later)
                    ui.input(placeholder='Search notes...').props('rounded outlined dense').classes('w-64 bg-white').on('update:model-value', lambda e: ui.notify(f'Searching for: {e.value}') if e.value else None)
                
                notes_container = ui.column().classes('w-full gap-6')
                refresh_notes()

    ui.run_with(fastapi_app, storage_secret='your_secret_key_here')
