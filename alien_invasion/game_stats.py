from settings import Settings


class GameStats():
    def __init__(self, ai_settings: Settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during game"""
        self.ships_left = self.ai_settings.ship_limit
