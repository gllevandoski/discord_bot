from mcstatus import JavaServer

server = JavaServer.lookup("cs16redirect.servegame.com:25566")
server_status = server.status()
print(server_status)
