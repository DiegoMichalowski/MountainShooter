from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY, WIN_HEIGHT


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.move_control = True

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.name == "Enemy3":
            if self.move_control:
                self.rect.centery += (ENTITY_SPEED[self.name] * 2)
                if self.rect.bottom > WIN_HEIGHT:
                    self.move_control = False

            if not self.move_control:
                self.rect.centery -= ENTITY_SPEED[self.name]
                if self.rect.top < 0:
                    self.move_control = True

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot',position=(self.rect.centerx,self.rect.centery))


