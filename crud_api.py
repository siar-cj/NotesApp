import CRUD as c
from fastapi import FastAPI
import logger as l
app = FastAPI()
@app.post("/create_note")
def create_note_api(data: dict):
    filename, subject, other_info, content = (
        data['filename'],
        data['subject'],
        data['other_info'],
        data['content'],
    )
    c.create_note()

    return {"message": "Note created successfully"}

@app.get("/read_notes")
def read_notes_api():
    notes = c.read_notes()
    return {"notes": notes}

@app.put("/update_note")
def update_note_api(data: dict):
    filename, content = data['filename'], data['content']
    c.update_note(filename,content)

    return {"message": "Note updated successfully"}


@app.delete("/delete_note")
def delete_note_api(data: dict):
    filename = data['filename']
    c.delete_note(filename)

    return {"message": "Note deleted successfully"}
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
