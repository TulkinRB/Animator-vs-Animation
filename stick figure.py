import math
import config
import pygame
pygame.init()

class stick_figure():
        angles = {
                "body": 90,
                "head": 180,
                "l_leg": -143.13,
                "r_leg": -36.87,
                "l_knee": -148.67,
                "r_knee": 148.67,
                "l_arm": -63.43,
                "r_arm": 63.43,
                "l_elbow": -143.13,
                "r_elbow": 143.13,
        }
        lengths = {
                "body": 45,
                "head": 11.25,
                "l_leg": 18.75,
                "r_leg": 18.75,
                "l_knee": 20.25,
                "r_knee": 20.25,
                "l_arm": 16.8,
                "r_arm": 16.8,
                "l_elbow": 16.8,
                "r_elbow": 16.8,
        }
        points = {
                "A": (200, 200), #body and legs
                "B": (0, 0), #body, arms and head
                "C": (0, 0), #head middle
                "D": (0, 0), #left knee
                "E": (0, 0), #right knee
                "F": (0, 0), #left leg end
                "G": (0, 0), #right leg end
                "H": (0, 0), #left elbow
                "I": (0, 0), #right elbow
                "J": (0, 0), #left arm end
                "K": (0, 0)  #right arm end
        }
        def __init__(self):
                pass

        def render(self, point="A"):
                point = point.upper()
                if point != "A":
                        return NotImplemented
                self.points["B"] = (int(self.points["A"][0] + math.cos(math.radians(self.angles["body"])) * self.lengths["body"]), int(self.points["A"][1] - math.sin(math.radians(self.angles["body"])) * self.lengths["body"]))
                self.points["C"] = (int(self.points["B"][0] + math.cos(math.radians(self.angles["head"] + self.angles["body"] - 180)) * self.lengths["head"]), int(self.points["B"][1] - math.sin(math.radians(self.angles["head"] + self.angles["body"] - 180)) * self.lengths["head"]))
                self.points["D"] = (int(self.points["A"][0] + math.cos(math.radians(self.angles["l_leg"])) * self.lengths["l_leg"]), int(self.points["A"][1] - math.sin(math.radians(self.angles["l_leg"])) * self.lengths["l_leg"]))
                self.points["E"] = (int(self.points["A"][0] + math.cos(math.radians(self.angles["r_leg"])) * self.lengths["r_leg"]), int(self.points["A"][1] - math.sin(math.radians(self.angles["r_leg"])) * self.lengths["r_leg"]))		
                self.points["F"] = (int(self.points["D"][0] + math.cos(math.radians(self.angles["l_knee"] + self.angles["l_leg"] - 180)) * self.lengths["l_knee"]), int(self.points["D"][1] - math.sin(math.radians(self.angles["l_knee"] + self.angles["l_leg"] - 180)) * self.lengths["l_knee"]))
                self.points["G"] = (int(self.points["E"][0] + math.cos(math.radians(self.angles["r_knee"] + self.angles["r_leg"] - 180)) * self.lengths["r_knee"]), int(self.points["E"][1] - math.sin(math.radians(self.angles["r_knee"] + self.angles["r_leg"] - 180)) * self.lengths["r_knee"]))
                self.points["H"] = (int(self.points["B"][0] + math.cos(math.radians(self.angles["l_arm"] + self.angles["body"] - 180)) * self.lengths["l_arm"]), int(self.points["B"][1] - math.sin(math.radians(self.angles["l_arm"] + self.angles["body"] - 180)) * self.lengths["l_arm"]))
                self.points["I"] = (int(self.points["B"][0] + math.cos(math.radians(self.angles["r_arm"] + self.angles["body"] - 180)) * self.lengths["r_arm"]), int(self.points["B"][1] - math.sin(math.radians(self.angles["r_arm"] + self.angles["body"] - 180)) * self.lengths["r_arm"]))
                self.points["J"] = (int(self.points["H"][0] + math.cos(math.radians(self.angles["l_elbow"] + self.angles["l_arm"] + self.angles["body"] - 360)) * self.lengths["l_elbow"]), int(self.points["H"][1] - math.sin(math.radians(self.angles["l_elbow"] + self.angles["l_arm"] + self.angles["body"] - 360)) * self.lengths["l_elbow"]))
                self.points["K"] = (int(self.points["I"][0] + math.cos(math.radians(self.angles["r_elbow"] + self.angles["r_arm"] + self.angles["body"] - 360)) * self.lengths["r_elbow"]), int(self.points["I"][1] - math.sin(math.radians(self.angles["r_elbow"] + self.angles["r_arm"] + self.angles["body"] - 360)) * self.lengths["r_elbow"]))

        def draw(self, render_point="A"):
                BLACK = (0, 0, 0)
                if not render_point == None:
                        self.render(render_point)

                pygame.draw.line(config.display, BLACK, self.points["A"], self.points["B"], 3)
                pygame.draw.line(config.display, BLACK, self.points["A"], self.points["D"], 3)
                pygame.draw.line(config.display, BLACK, self.points["A"], self.points["E"], 3)
                pygame.draw.line(config.display, BLACK, self.points["D"], self.points["F"], 3)
                pygame.draw.line(config.display, BLACK, self.points["E"], self.points["G"], 3)
                pygame.draw.line(config.display, BLACK, self.points["B"], self.points["H"], 3)
                pygame.draw.line(config.display, BLACK, self.points["B"], self.points["I"], 3)
                pygame.draw.line(config.display, BLACK, self.points["H"], self.points["J"], 3)
                pygame.draw.line(config.display, BLACK, self.points["I"], self.points["K"], 3)
                pygame.draw.circle(config.display, BLACK, self.points["C"], int(self.lengths["head"]), 3)
