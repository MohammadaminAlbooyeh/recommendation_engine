#!/usr/bin/env python
"""
Smart Notes - Notebook Application Runner
Starts the FastAPI server with NiceGUI interface
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Main entry point for running the application"""
    
    # Change to backend directory
    backend_dir = Path(__file__).parent / 'backend'
    os.chdir(backend_dir)
    
    print("=" * 60)
    print("🚀 Starting Smart Notes Application")
    print("=" * 60)
    print()
    print("📌 Application will be available at:")
    print("   - NiceGUI Interface: http://localhost:8000/")
    print("   - API Documentation: http://localhost:8000/docs")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    print()
    
    try:
        # Run uvicorn server
        subprocess.run([
            sys.executable, "-m", "uvicorn",
            "app.main:app",
            "--reload",
            "--host", "0.0.0.0",
            "--port", "8000"
        ])
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped gracefully")
        print("Thank you for using Smart Notes!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
