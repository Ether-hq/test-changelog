class AuthService:
    def __init__(self):
        self.providers = ['google', 'github']
    
    def login(self, username, password, provider='google'):
        """Authenticate user with OAuth2"""
        if provider not in self.providers:
            raise ValueError(f"Unsupported provider: {provider}")
        
        # OAuth2 authentication logic
        token = self._generate_token(username, provider)
        return {"success": True, "token": token}
    
    def _generate_token(self, username, provider):
        """Generate OAuth2 token"""
        return f"token_{provider}_{username}"
