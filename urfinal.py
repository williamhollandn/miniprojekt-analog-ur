import pygame
import math
import datetime
import sys

# sætter pygame op, for at kunne bruge pygame funktioner.
pygame.init()

# Sætter skærmstørrelsen og titel på vinduet til variblerne X og Y, som er 600x600 pixels.
X, Y = 600, 600
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Miniprojekt 1: Analog Ur")

# Definerer farverne, som der skal bruges i uret.
WHITE = (255, 255, 255)
CYAN = (50, 255, 255)
RED = (255, 50, 50)
ORANGE = (255, 150, 50)

# Definerer midten af uret og radiusen for uret, så de kan bruges senere i koden.
CENTER = (X // 2, Y // 2)
RADIUS = 260
# Sætter en clock til at styre opdateringshastigheden for uret.
clock = pygame.time.Clock()

# loop, der kører uret og opdaterer det hvert sekund.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Henter den aktuelle tid og konverterer den til 12-timers format der passer til uret.
    now = datetime.datetime.now()
    h = now.hour % 12  # Konverter til 12-timers format
    m = now.minute
    s = now.second

    # Sætter baggrundsfarven afhængigt af om det er formiddag eller eftermiddag.
    if now.hour < 12:
        bg_color = (255, 212, 59)  # gul til am (formiddag)
    else:
        bg_color = (0, 0, 0)  # sort til pm (eftermiddag)
    screen.fill(bg_color)

    # Tegner urets cirkel og markeringer for timerne.
    pygame.draw.circle(screen, WHITE, CENTER, RADIUS, 3)

    # Tegner markeringer for timerne på uret.
    for i in range(12):
        angle = i * (2 * math.pi / 12) - (math.pi / 2)
        x_outer = CENTER[0] + RADIUS * math.cos(angle)
        y_outer = CENTER[1] + RADIUS * math.sin(angle)
        x_inner = CENTER[0] + (RADIUS - 20) * math.cos(angle)
        y_inner = CENTER[1] + (RADIUS - 20) * math.sin(angle)
        pygame.draw.line(screen, WHITE, (x_inner, y_inner), (x_outer, y_outer), 4)

    # Tegner sekundviseren, minutviseren og timeviseren med forskellige farver og tykkelser.
    if s % 2 == 0:
        current_sec_color = RED
    else:
        current_sec_color = ORANGE

    # Tegner sekundviseren
    sec_angle = s * (2 * math.pi / 60) - (math.pi / 2)
    sec_x = CENTER[0] + (RADIUS - 30) * math.cos(sec_angle)
    sec_y = CENTER[1] + (RADIUS - 30) * math.sin(sec_angle)
    pygame.draw.line(screen, current_sec_color, CENTER, (sec_x, sec_y), 2)

    # Tegner minutviseren
    min_angle = (m + s / 60) * (2 * math.pi / 60) - (math.pi / 2)
    min_x = CENTER[0] + (RADIUS - 50) * math.cos(min_angle)
    min_y = CENTER[1] + (RADIUS - 50) * math.sin(min_angle)
    pygame.draw.line(screen, CYAN, CENTER, (min_x, min_y), 6)

    # Tegner timeviseren
    hour_angle = (h + m / 60) * (2 * math.pi / 12) - (math.pi / 2)
    hour_x = CENTER[0] + (RADIUS - 100) * math.cos(hour_angle)
    hour_y = CENTER[1] + (RADIUS - 100) * math.sin(hour_angle)
    pygame.draw.line(screen, WHITE, CENTER, (hour_x, hour_y), 10)

    # Tegner en cirkel i midten af uret, som ændrer farve afhængigt af om det er lige eller ulige sekund.
    pygame.draw.circle(screen, current_sec_color, CENTER, 8)

    # Opdaterer skærmen og sætter opdateringshastigheden til 60 FPS.
    pygame.display.flip()
    clock.tick(60)