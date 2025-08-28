# first line

#####################
# starts the server #
#####################

from services.server_logic import start_server, server_state

def main():
    try:
        print("loading [SERVER]...")
        start_server(server_state)
    except KeyboardInterrupt:
        print("shutting down [SERVER]...")
        from services.server_logic import stop_server
        stop_server(server_state)

# initialize only if this file is directly started
if __name__ == "__main__":
    main()

# last line