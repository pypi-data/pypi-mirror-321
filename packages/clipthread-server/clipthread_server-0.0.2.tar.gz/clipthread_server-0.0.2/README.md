# ClipThread Server

ClipThread is a multi-platform clipboard synchronization tool that enables real-time sharing of clipboard content across different devices. It uses a client-server architecture to maintain clipboard history and ensure secure synchronization between multiple devices.

## Purpose
The ClipThread server acts as the central hub for all clipboard operations. It:
- Manages clipboard content synchronization between connected clients 
- Maintains a clipboard history journal
- Handles secure data transmission between devices
- Provides REST API endpoints for clipboard operations

## Running the Server

### Using Docker Compose
```bash
# Clone the repository
git clone https://github.com/clipthread/clipthread-server.git

# Navigate to docker directory
cd clipthread-server/docker

# Start the server
docker-compose up -d
```

### Using Systemd
1. Install the package:
```bash
pip install clipthread-server
```

2. Copy the systemd service file:
```bash
sudo cp systemd/clipthread-server.service /etc/systemd/system/
```

3. Start the service:
```bash
sudo systemctl enable clipthread-server
sudo systemctl start clipthread-server
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Todo
- [ ] Add authentication system
- [ ] Implement encryption for clipboard content
- [ ] Create API documentation
- [ ] Add rate limiting
- [ ] Implement clipboard content filtering

## Client Applications
- Desktop UI (Tkinter): [ui-tkinter](https://github.com/clipthread/ui-tkinter)
- Core Library: [clipthread-core](https://github.com/clipthread/core)
- Android App: [clipthread-android](https://github.com/clipthread/android)