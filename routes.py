from fastapi import APIRouter, UploadFile, File
import shutil
from agents.orchestrator import AudioAIOrchestrator

router = APIRouter()
orchestrator = AudioAIOrchestrator()

@router.post("/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = orchestrator.run_pipeline(file_path)
    return result