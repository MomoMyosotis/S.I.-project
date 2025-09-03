# first line

from services.server_logic import start_server, stop_server, server_state

def main():
    print("Loading [SERVER]...")
    try:
        start_server(server_state)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Shutting down [SERVER]...")
        stop_server(server_state)
    except Exception as e:
        print(f"[ERROR] Server crashed: {e}")
        stop_server(server_state)

if __name__ == "__main__":
    main()

# last line