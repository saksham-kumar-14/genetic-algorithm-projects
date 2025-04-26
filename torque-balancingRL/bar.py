import pygame
import math 

class Bar:
    def __init__(self, x, y, init_acc, g):
        self.__base_width = 150
        self.__base_height = 30
        self.__bar_height = 300
        self.__bar_width = self.__base_height
        self.__radius = 7
        self.__angle = 0
        
        self.g = g
        self.x, self.y = x, y 

        self.__bar_weight = 30 
        self.__base_weight = 50
        # assuming pin's weight is negligible

        self.__center_MOI = self.__bar_weight * (self.__bar_height ** 2) / 12

        # bar corner points
        self.__corners = [
            (self.x - self.__bar_width / 2, self.y),
            (self.x + self.__bar_width / 2, self.y),
            (self.x - self.__bar_width / 2, self.y - self.__bar_height),
            (self.x + self.__bar_width / 2, self.y - self.__bar_height)
        ]

        # dynamics parameters
        self.angular_vel = 0
        self.vel = 0
        self.angular_acc = 0
        self.acc = init_acc # this acceleration is for x axis only

    def rotate(self, pts):
        rotated = []

        for pt in pts:
            px, py = pt[0], pt[1]
            px -= self.x 
            py -= self.y 

            x_new = px * math.cos(self.__angle) - py * math.sin(self.__angle)
            y_new = px * math.sin(self.__angle) + py * math.cos(self.__angle)

            px = x_new + self.x 
            py = y_new + self.y 

            rotated.append((px, py))

        rotated[0], rotated[1] = rotated[1], rotated[0]
        return rotated

    def cal_MOI(self, d):
        return self.__center_MOI + (self.__bar_weight * d * d)


    def change_dynamic_params(self):
        d = self.__bar_height 

        # for now total torque is the total exerted by gravity and pseudo force
        trq = (self.__bar_weight * d / 2) * ((self.g * math.sin(self.__angle)) - (self.acc * math.cos(self.__angle)) )
        I = self.cal_MOI(d)
        self.angular_acc = trq / I 

        # changes in dynamics after around 1 sec
        self.angular_vel += self.angular_acc
        self.change_angle(self.angular_vel + (0.5 * self.angular_acc))

    def change_angle(self, dt):
        self.__angle += dt
        if self.__angle > math.pi / 2:
            self.__angle = math.pi / 2 
        elif self.__angle < -math.pi / 2:
            self.__angle =  -math.pi / 2


    def draw(self, screen, base_color, bar_color, pin_color):
        # base
        corner_x, corner_y = self.x - self.__base_width / 2, self.y - self.__base_height / 2
        pygame.draw.rect(screen, base_color, (corner_x, corner_y, self.__base_width, self.__base_height)) 

        # bar 
        rotated_corners = self.rotate(self.__corners)
        pygame.draw.polygon(screen, bar_color, rotated_corners)

        # pin 
        pygame.draw.circle(screen, pin_color, (self.x, self.y), self.__radius)





