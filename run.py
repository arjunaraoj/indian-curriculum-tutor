from interface.gradio_ui import create_interface

if __name__ == "__main__":
    try:
        print("🚀 Starting Tutor Application...")
        create_interface().launch(server_port=7865)
    except Exception as e:
        print(f"❌ Launch failed: {e}")