from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = self.art()
        self.wfile.write(message.encode())
        return
    
    def art(self):
        
        thumbs_up = """
            ________$$$$
            _______$$__$
            _______$___$$
            _______$___$$
            _______$$___$$
            ________$____$$
            ________$$____$$$
            _________$$_____$$
            _________$$______$$
            __________$_______$$
            ____$$$$$$$________$$
            __$$$_______________$$$$$$
            _$$____$$$$____________$$$
            _$___$$$__$$$____________$$
            _$$________$$$____________$
            __$$____$$$$$$____________$
            __$$$$$$$____$$___________$
            __$$_______$$$$___________$
            ___$$$$$$$$$__$$_________$$
            ____$________$$$$_____$$$$
            ____$$____$$$$$$____$$$$$$
            _____$$$$$$____$$__$$
            _______$_____$$$_$$$
            ________$$$$$$$$$$
        """
        
        return thumbs_up