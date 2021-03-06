# -*- coding: utf-8 -*-

import pygame
import classes.extras as ex


class Splash:
    lines = [[135, 128], [133, 132], [135, 137], [157, 157], [158, 161], [155, 165], [150, 166], [146, 163],
             [133, 140], [129, 138], [125, 139], [122, 142], [122, 144], [128, 157], [128, 159], [126, 161],
             [123, 161], [121, 160], [114, 147], [112, 145], [107, 145], [104, 148], [104, 154], [110, 179],
             [111, 186], [110, 192], [105, 194], [100, 193], [98, 188], [98, 180], [101, 154], [100, 148],
             [96, 146], [93, 147], [92, 149], [88, 163], [86, 165], [83, 165], [80, 164], [80, 161], [80, 158],
             [83, 147], [82, 143], [73, 139], [65, 143], [55, 167], [52, 174], [48, 179], [42, 178], [37, 174],
             [38, 169], [43, 163], [57, 151], [63, 144], [67, 137], [66, 129], [60, 126], [51, 138], [47, 141],
             [44, 142], [40, 140], [38, 136], [40, 134], [44, 131], [57, 124], [56, 117], [51, 114], [43, 120],
             [40, 122], [38, 124], [36, 124], [34, 122], [34, 119], [36, 117], [50, 111], [52, 108], [53, 102],
             [51, 98], [46, 96], [38, 97], [11, 103], [5, 103], [3, 99], [4, 94], [10, 92], [36, 94], [44, 94],
             [50, 91], [53, 87], [52, 83], [46, 81], [21, 79], [14, 78], [9, 76], [8, 73], [10, 71], [15, 71],
             [22, 72], [45, 77], [51, 77], [53, 74], [52, 69], [40, 60], [39, 57], [39, 55], [41, 53], [44, 53],
             [47, 54], [55, 59], [58, 59], [61, 58], [62, 55], [61, 52], [54, 43], [54, 41], [55, 38], [58, 37],
             [61, 39], [71, 51], [74, 52], [80, 50], [81, 46], [80, 40], [77, 32], [66, 18], [62, 12], [61, 6],
             [65, 3], [70, 2], [74, 6], [76, 13], [79, 30], [81, 37], [86, 42], [91, 43], [95, 41], [95, 39],
             [93, 28], [93, 25], [93, 23], [96, 22], [99, 22], [100, 24], [100, 28], [99, 39], [101, 41], [103, 42],
             [106, 42], [108, 40], [111, 29], [112, 26], [114, 25], [117, 24], [119, 26], [120, 29], [119, 33],
             [116, 45], [117, 48], [119, 50], [122, 50], [135, 33], [137, 31], [140, 31], [142, 34], [142, 37],
             [133, 53], [133, 56], [134, 59], [137, 59], [141, 56], [155, 40], [160, 36], [164, 35], [169, 38],
             [170, 42], [168, 46], [163, 50], [146, 59], [144, 62], [145, 66], [149, 67], [160, 64], [162, 63],
             [164, 64], [165, 66], [165, 69], [164, 71], [150, 77], [148, 79], [148, 84], [150, 88], [155, 89],
             [173, 81], [179, 79], [183, 79], [185, 83], [186, 90], [184, 93], [180, 95], [175, 94], [158, 95],
             [154, 99], [153, 103], [156, 106], [163, 108], [185, 113], [190, 115], [191, 118], [189, 122],
             [184, 121], [163, 111], [156, 109], [151, 110], [147, 115], [145, 120], [146, 124], [151, 128],
             [163, 135], [168, 139], [171, 142], [171, 146], [167, 146], [162, 144], [158, 140], [149, 132],
             [144, 128], [140, 127]]

    hue_choice = [[255, 255, 255], [2, 2, 2], [140, 140, 140], [255, 0, 0], [255, 138, 0], [255, 255, 0],
                  [181, 219, 3], [0, 160, 0], [41, 131, 82], [0, 130, 133], [0, 0, 255], [0, 0, 132],
                  [132, 0, 132], [255, 0, 255], [74, 0, 132], [255, 20, 138], [132, 0, 0], [140, 69, 16],
                  [0, 255, 255], [0, 255, 0]]

    def __init__(self, unit_size, scale, preset_color, custom_color=(-1, -1, -1, -1)):
        size = unit_size * scale
        self.scaled_lines = [[int(size * each[0] / 200.0), int(size * each[1] / 200.0)] for each in Splash.lines]

        self.canvas = pygame.Surface([size, size - 1], flags=pygame.SRCALPHA)
        self.canvas.fill((0, 0, 0, 0))
        if custom_color[0] > -1:
            col = ex.hsva_to_rgba(custom_color[0], custom_color[1], custom_color[2], custom_color[3])
        else:
            col = Splash.hue_choice[preset_color]
        self.draw_splash(self.canvas, col)

    def get_canvas(self):
        return self.canvas

    def draw_splash(self, canvas, color):
        pygame.draw.polygon(canvas, color, self.scaled_lines, 0)