from pygame import mixer


class SFX():
    def __init__(self):
        mixer.init()
        self.start_sound = mixer.Sound("sfx/start.wav")
        self.bullet_sound = mixer.Sound("sfx/bullet.wav")
        self.dead_sound = mixer.Sound("sfx/dead.wav")
        self.score_sound = mixer.Sound("sfx/score.wav")
        self.alien_sound = mixer.Sound("sfx/alien.wav")
