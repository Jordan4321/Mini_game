# Game in python window
import pygame
import random


class StartGame:
    def __init__(self):
        pygame.init()
        self.DISPLAY_W, self.DISPLAY_H = 500, 500
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.screen = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.playing = True
        self.background = pygame.image.load('image/arena.jpg')
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.player1_score, self.player2_score = 0, 0
        self.player1_choice, self.player2_choice = '', ''
        self.player_score, self.computer_score = 0, 0
        self.player_choice, self.computer_choice = '', ''
        self.BLACK = (0, 0, 0)

    def game_loop(self):
        while self.playing:
            self.menu()
            self.display.fill(self.BLACK)
            self.screen.blit(self.display, (0, 0))
            pygame.display.update()

    def menu(self):

        pygame.display.set_caption("Menu")
        basic_font = pygame.font.Font(None, 30)
        start_text = '1. New Game'
        quit_text = '2. Quit Game'

        input_rect = pygame.Rect(0, 60, 140, 32)
        color_active = pygame.Color('gray15')
        color_passive = pygame.Color('lightskyblue3')
        active = False

        input_rect2 = pygame.Rect(0, 110, 140, 32)
        color_active2 = pygame.Color('gray15')
        color_passive2 = pygame.Color('lightskyblue3')
        active2 = False

        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        self.pvx()
                    if input_rect2.collidepoint(event.pos):
                        active2 = True
                        pygame.quit()

            pygame.display.update()
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, self.background_rect)
            if active:
                color = color_active
            else:
                color = color_passive

            if active2:
                color2 = color_active2
            else:
                color2 = color_passive2

            font = pygame.font.SysFont('comicsans', 30)
            label = font.render('Paper, Scissor, Rock!', True, (255, 255, 255))
            self.screen.blit(label, (90, 0))

            pygame.draw.rect(self.screen, color, input_rect, 2)
            start = basic_font.render(start_text, True, (0, 255, 0))
            self.screen.blit(start, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = start.get_width() + 10

            pygame.draw.rect(self.screen, color2, input_rect2, 2)
            text2 = basic_font.render(quit_text, True, (255, 0, 0))
            self.screen.blit(text2, (input_rect2.x + 5, input_rect2.y + 5))
            input_rect2.w = text2.get_width() + 10

            pygame.display.flip()

    def player1choice(self):

        pygame.display.set_caption("Player1_choice")

        input_rect = pygame.Rect(20, 60, 140, 32)
        active1 = False
        input_rect2 = pygame.Rect(180, 60, 140, 32)
        active2 = False
        input_rect3 = pygame.Rect(330, 60, 140, 32)
        active3 = False
        input_rect4 = pygame.Rect(180, 300, 140, 32)
        color = pygame.Color('gray15')

        back_menu_text = '--> Back to menu <--'
        input_rect5 = pygame.Rect(145, 450, 140, 32)

        while True:
            self.screen.fill("black")
            basic_font = pygame.font.Font(None, 30)
            text_paper = 'PAPER'
            text_scissor = 'SCISSOR'
            text_rock = 'ROCK'
            choice = 'Please select your choice player 1 '
            cd = 'Continue'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active1 = True
                        active2 = False
                        active3 = False

                    elif input_rect2.collidepoint(event.pos):
                        active2 = True
                        active1 = False
                        active3 = False

                    elif input_rect3.collidepoint(event.pos):
                        active3 = True
                        active1 = False
                        active2 = False

                    elif input_rect4.collidepoint(event.pos) and active1 is True:
                        self.player1_choice += 'paper'
                        self.player2choice()

                    elif input_rect4.collidepoint(event.pos) and active2 is True:
                        self.player1_choice += 'scissor'
                        self.player2choice()

                    elif input_rect4.collidepoint(event.pos) and active3 is True:
                        self.player1_choice += 'rock'
                        self.player2choice()

                    elif input_rect5.collidepoint(event.pos):
                        self.player1_score = 0
                        self.player2_score = 0
                        self.player1_choice = ''
                        self.player2_choice = ''
                        self.menu()

                    else:
                        active1 = False
                        active2 = False
                        active3 = False

            self.screen.blit(self.background, self.background_rect)

            if active1:
                paper_image = pygame.image.load('image/paper1.jpg')
            else:
                paper_image = pygame.image.load('image/paper.jpg')

            if active2:
                scissor_image = pygame.image.load('image/scissor1.jpg')
            else:
                scissor_image = pygame.image.load('image/scissor.jpg')

            if active3:
                rock_image = pygame.image.load('image/rock1.jpg')
            else:
                rock_image = pygame.image.load('image/rock.jpg')

            pygame.draw.rect(self.screen, color, input_rect, 2)  # Paper - input
            self.screen.blit(paper_image, input_rect)
            input_rect.h = paper_image.get_height() + 0
            input_rect.w = paper_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect2, 2)  # Scissor - input
            self.screen.blit(scissor_image, (input_rect2.x, input_rect2.y))
            input_rect2.h = scissor_image.get_height() + 0
            input_rect2.w = scissor_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect3, 2)  # Rock - input
            self.screen.blit(rock_image, (input_rect3.x, input_rect3.y))
            input_rect3.h = rock_image.get_height() + 0
            input_rect3.w = rock_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect4, 2)  # Continue - input
            cont = basic_font.render(cd, True, (255, 0, 0))
            self.screen.blit(cont, (input_rect4.x + 5, input_rect4.y + 5))
            input_rect4.w = cont.get_width() + 10

            paper = basic_font.render(text_paper, True, (255, 255, 255))  # Paper - text
            self.screen.blit(paper, (40, 20))

            scissor = basic_font.render(text_scissor, True, (255, 255, 0))  # Scissor - text
            self.screen.blit(scissor, (190, 20))

            rock = basic_font.render(text_rock, True, (255, 0, 255))  # Rock - text
            self.screen.blit(rock, (360, 20))

            choice = basic_font.render(choice, True, (255, 0, 255))
            self.screen.blit(choice, (70, 260))

            pygame.draw.rect(self.screen, color, input_rect5, 2)  # Back to menu - button
            back_menu = basic_font.render(back_menu_text, True, (0, 255, 0))
            self.screen.blit(back_menu, (input_rect5.x, input_rect5.y + 5))
            input_rect5.w = back_menu.get_width() + 10

            pygame.display.flip()

    def player2choice(self):

        pygame.display.set_caption("Player2_choice")
        input_rect = pygame.Rect(20, 60, 140, 32)
        active1 = False

        input_rect2 = pygame.Rect(180, 60, 140, 32)
        active2 = False

        input_rect3 = pygame.Rect(330, 60, 140, 32)
        active3 = False

        input_rect4 = pygame.Rect(180, 300, 140, 32)
        color = pygame.Color('gray15')

        back_menu_text = '--> Back to menu <--'
        input_rect5 = pygame.Rect(145, 450, 140, 32)

        while True:
            self.screen.fill("black")
            basic_font = pygame.font.Font(None, 30)
            text_paper = 'PAPER'
            text_scissor = 'SCISSOR'
            text_rock = 'ROCK'
            choice = 'Please select your choice player 2 '
            cd = 'Continue'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active1 = True
                        active2 = False
                        active3 = False

                    elif input_rect2.collidepoint(event.pos):
                        active2 = True
                        active1 = False
                        active3 = False

                    elif input_rect3.collidepoint(event.pos):
                        active3 = True
                        active1 = False
                        active2 = False

                    elif input_rect4.collidepoint(event.pos) and active1 is True:
                        self.player2_choice += 'paper'
                        self.result()
                    elif input_rect4.collidepoint(event.pos) and active2 is True:
                        self.player2_choice += 'scissor'
                        self.result()
                    elif input_rect4.collidepoint(event.pos) and active3 is True:
                        self.player2_choice += 'rock'
                        self.result()

                    elif input_rect5.collidepoint(event.pos):
                        self.player1_score = 0
                        self.player2_score = 0
                        self.player1_choice = ''
                        self.player2_choice = ''
                        self.menu()

                    else:
                        active1 = False
                        active2 = False
                        active3 = False

            self.screen.blit(self.background, self.background_rect)

            if active1:
                paper_image = pygame.image.load('image/paper1.jpg')
            else:
                paper_image = pygame.image.load('image/paper.jpg')

            if active2:
                scissor_image = pygame.image.load('image/scissor1.jpg')
            else:
                scissor_image = pygame.image.load('image/scissor.jpg')

            if active3:
                rock_image = pygame.image.load('image/rock1.jpg')
            else:
                rock_image = pygame.image.load('image/rock.jpg')

            pygame.draw.rect(self.screen, color, input_rect, 2)  # Paper - input
            self.screen.blit(paper_image, input_rect)
            input_rect.h = paper_image.get_height() + 0
            input_rect.w = paper_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect2, 2)  # Scissor - input
            self.screen.blit(scissor_image, (input_rect2.x, input_rect2.y))
            input_rect2.h = scissor_image.get_height() + 0
            input_rect2.w = scissor_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect3, 2)  # Rock - input
            self.screen.blit(rock_image, (input_rect3.x, input_rect3.y))
            input_rect3.h = rock_image.get_height() + 0
            input_rect3.w = rock_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect4, 2)  # Continue - input
            cont = basic_font.render(cd, True, (255, 0, 0))
            self.screen.blit(cont, (input_rect4.x + 5, input_rect4.y + 5))
            input_rect4.w = cont.get_width() + 10

            paper = basic_font.render(text_paper, True, (255, 255, 255))  # Paper - text
            self.screen.blit(paper, (40, 20))

            scissor = basic_font.render(text_scissor, True, (255, 255, 0))  # Scissor - text
            self.screen.blit(scissor, (190, 20))

            rock = basic_font.render(text_rock, True, (255, 0, 255))  # Rock - text
            self.screen.blit(rock, (360, 20))

            choice = basic_font.render(choice, True, (255, 0, 255))
            self.screen.blit(choice, (70, 260))

            pygame.draw.rect(self.screen, color, input_rect5, 2)  # Back to menu - button
            back_menu = basic_font.render(back_menu_text, True, (0, 255, 0))
            self.screen.blit(back_menu, (input_rect5.x, input_rect5.y + 5))
            input_rect5.w = back_menu.get_width() + 10

            pygame.display.flip()

    def result(self):

        pygame.display.set_caption("Result")

        basic_font = pygame.font.Font(None, 30)
        back_text = 'Wanna play again?'
        input_rect1 = pygame.Rect(150, 130, 140, 32)
        color_active1 = pygame.Color('gray15')
        color_passive1 = pygame.Color('lightskyblue3')
        active1 = False

        back_menu_text = '--> Back to menu <--'
        input_rect2 = pygame.Rect(145, 450, 140, 32)
        color = pygame.Color('gray15')

        if self.player1_choice == 'paper' and self.player2_choice == 'scissor' \
                or self.player1_choice == 'scissor' and self.player2_choice == 'rock' \
                or self.player1_choice == 'rock' and self.player2_choice == 'paper':
            self.player2_score += 1

        elif self.player1_choice == 'paper' and self.player2_choice == 'rock' \
                or self.player1_choice == 'scissor' and self.player2_choice == 'paper' \
                or self.player1_choice == 'rock' and self.player2_choice == 'scissor':
            self.player1_score += 1

        score = f'Player1 : {self.player1_score} vs {self.player2_score} : Player2 '

        while True:
            self.screen.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect1.collidepoint(event.pos):
                        active1 = True
                        self.player1_choice = ''
                        self.player2_choice = ''
                        self.player1choice()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect2.collidepoint(event.pos):
                        self.player1_score = 0
                        self.player2_score = 0
                        self.player1_choice = ''
                        self.player2_choice = ''
                        self.menu()

            self.screen.blit(self.background, self.background_rect)

            if self.player1_choice == self.player2_choice:
                font = pygame.font.SysFont('comicsans', 30)
                label = font.render('DRAW', True, (255, 255, 255))
                self.screen.blit(label, (200, 0))

            elif self.player1_choice == 'paper' and self.player2_choice == 'scissor' \
                    or self.player1_choice == 'scissor' and self.player2_choice == 'rock' \
                    or self.player1_choice == 'rock' and self.player2_choice == 'paper':
                font = pygame.font.SysFont('comicsans', 30)
                label = font.render('PLAYER2 WINS', True, (255, 255, 255))
                self.screen.blit(label, (140, 0))

            elif self.player1_choice == 'paper' and self.player2_choice == 'rock' \
                    or self.player1_choice == 'scissor' and self.player2_choice == 'paper' \
                    or self.player1_choice == 'rock' and self.player2_choice == 'scissor':
                font = pygame.font.SysFont('comicsans', 30)
                label = font.render('PLAYER1 WINS', True, (255, 255, 255))
                self.screen.blit(label, (140, 0))

            if active1:
                color1 = color_active1
            else:
                color1 = color_passive1

            pygame.draw.rect(self.screen, color1, input_rect1, 2)
            back = basic_font.render(back_text, True, (0, 255, 0))
            self.screen.blit(back, (input_rect1.x + 5, input_rect1.y + 5))
            input_rect1.w = back.get_width() + 10

            points = basic_font.render(score, True, (255, 0, 0))  # Score - text
            self.screen.blit(points, (125, 255))

            pygame.draw.rect(self.screen, color, input_rect2, 2)
            back_menu = basic_font.render(back_menu_text, True, (0, 255, 0))
            self.screen.blit(back_menu, (input_rect2.x, input_rect2.y + 5))
            input_rect2.w = back_menu.get_width() + 10

            pygame.display.flip()

    def pvx(self):

        pygame.display.set_caption("PvE vs PvP")
        basic_font = pygame.font.Font(None, 30)
        start_text = '1. Single player'
        quit_text = '2. Player vs Plater'

        input_rect = pygame.Rect(0, 60, 140, 32)
        color_active = pygame.Color('gray15')
        color_passive = pygame.Color('lightskyblue3')
        active = False

        input_rect2 = pygame.Rect(0, 110, 140, 32)
        color_active2 = pygame.Color('gray15')
        color_passive2 = pygame.Color('lightskyblue3')
        active2 = False

        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                        self.pve()
                    if input_rect2.collidepoint(event.pos):
                        active2 = True
                        self.player1choice()

            pygame.display.update()
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, self.background_rect)
            if active:
                color = color_active
            else:
                color = color_passive

            if active2:
                color2 = color_active2
            else:
                color2 = color_passive2

            font = pygame.font.SysFont('comicsans', 30)
            label = font.render('Paper, Scissor, Rock!', True, (255, 255, 255))
            self.screen.blit(label, (90, 0))

            pygame.draw.rect(self.screen, color, input_rect, 2)
            start = basic_font.render(start_text, True, (0, 255, 0))
            self.screen.blit(start, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = start.get_width() + 10

            pygame.draw.rect(self.screen, color2, input_rect2, 2)
            text2 = basic_font.render(quit_text, True, (255, 0, 0))
            self.screen.blit(text2, (input_rect2.x + 5, input_rect2.y + 5))
            input_rect2.w = text2.get_width() + 10

            pygame.display.flip()

    def pve(self):

        pygame.display.set_caption("Player_choice")
        input_rect = pygame.Rect(20, 60, 140, 32)
        active1 = False

        input_rect2 = pygame.Rect(180, 60, 140, 32)
        active2 = False

        input_rect3 = pygame.Rect(330, 60, 140, 32)
        active3 = False

        input_rect4 = pygame.Rect(180, 300, 140, 32)
        color = pygame.Color('gray15')

        back_menu_text = '--> Back to menu <--'
        input_rect5 = pygame.Rect(145, 450, 140, 32)

        while True:
            self.screen.fill("black")
            basic_font = pygame.font.Font(None, 30)
            text_paper = 'PAPER'
            text_scissor = 'SCISSOR'
            text_rock = 'ROCK'
            choice = 'Please select your choice player'
            cd = 'Continue'
            items = random.choice(['rock', 'scissor', 'paper'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active1 = True
                        active2 = False
                        active3 = False

                    elif input_rect2.collidepoint(event.pos):
                        active2 = True
                        active1 = False
                        active3 = False

                    elif input_rect3.collidepoint(event.pos):
                        active3 = True
                        active1 = False
                        active2 = False

                    elif input_rect4.collidepoint(event.pos) and active1 is True:
                        self.player_choice += 'paper'
                        self.computer_choice += items
                        self.result_pve()
                    elif input_rect4.collidepoint(event.pos) and active2 is True:
                        self.player_choice += 'scissor'
                        self.computer_choice += items
                        self.result_pve()
                    elif input_rect4.collidepoint(event.pos) and active3 is True:
                        self.player_choice += 'rock'
                        self.computer_choice += items
                        self.result_pve()

                    elif input_rect5.collidepoint(event.pos):
                        self.player_score = 0
                        self.computer_score = 0
                        self.player_choice = ''
                        self.computer_choice = ''
                        self.menu()

                    else:
                        active1 = False
                        active2 = False
                        active3 = False

            self.screen.blit(self.background, self.background_rect)

            if active1:
                paper_image = pygame.image.load('image/paper1.jpg')
            else:
                paper_image = pygame.image.load('image/paper.jpg')

            if active2:
                scissor_image = pygame.image.load('image/scissor1.jpg')
            else:
                scissor_image = pygame.image.load('image/scissor.jpg')

            if active3:
                rock_image = pygame.image.load('image/rock1.jpg')
            else:
                rock_image = pygame.image.load('image/rock.jpg')

            pygame.draw.rect(self.screen, color, input_rect, 2)  # Paper - input
            self.screen.blit(paper_image, input_rect)
            input_rect.h = paper_image.get_height() + 0
            input_rect.w = paper_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect2, 2)  # Scissor - input
            self.screen.blit(scissor_image, (input_rect2.x, input_rect2.y))
            input_rect2.h = scissor_image.get_height() + 0
            input_rect2.w = scissor_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect3, 2)  # Rock - input
            self.screen.blit(rock_image, (input_rect3.x, input_rect3.y))
            input_rect3.h = rock_image.get_height() + 0
            input_rect3.w = rock_image.get_width() - 10

            pygame.draw.rect(self.screen, color, input_rect4, 2)  # Continue - input
            cont = basic_font.render(cd, True, (255, 0, 0))
            self.screen.blit(cont, (input_rect4.x + 5, input_rect4.y + 5))
            input_rect4.w = cont.get_width() + 10

            paper = basic_font.render(text_paper, True, (255, 255, 255))  # Paper - text
            self.screen.blit(paper, (40, 20))

            scissor = basic_font.render(text_scissor, True, (255, 255, 0))  # Scissor - text
            self.screen.blit(scissor, (190, 20))

            rock = basic_font.render(text_rock, True, (255, 0, 255))  # Rock - text
            self.screen.blit(rock, (360, 20))

            choice = basic_font.render(choice, True, (255, 0, 255))
            self.screen.blit(choice, (70, 260))

            pygame.draw.rect(self.screen, color, input_rect5, 2)  # Back to menu - button
            back_menu = basic_font.render(back_menu_text, True, (0, 255, 0))
            self.screen.blit(back_menu, (input_rect5.x, input_rect5.y + 5))
            input_rect5.w = back_menu.get_width() + 10

            pygame.display.flip()

    def result_pve(self):

        pygame.display.set_caption("Result PvE")

        basic_font = pygame.font.Font(None, 30)
        back_text = 'Wanna play again?'
        input_rect1 = pygame.Rect(150, 130, 140, 32)
        color_active1 = pygame.Color('gray15')
        color_passive1 = pygame.Color('lightskyblue3')
        active1 = False

        back_menu_text = '--> Back to menu <--'
        input_rect2 = pygame.Rect(145, 450, 140, 32)
        color = pygame.Color('gray15')

        if self.player_choice == 'paper' and self.computer_choice == 'scissor' \
                or self.player_choice == 'scissor' and self.computer_choice == 'rock' \
                or self.player_choice == 'rock' and self.computer_choice == 'paper':
            self.computer_score += 1

        elif self.player_choice == 'paper' and self.computer_choice == 'rock' \
                or self.player_choice == 'scissor' and self.computer_choice == 'paper' \
                or self.player_choice == 'rock' and self.computer_choice == 'scissor':
            self.player_score += 1

        score = f'Player : {self.player_score} vs {self.computer_score} : Computer '

        while True:
            self.screen.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect1.collidepoint(event.pos):
                        active1 = True
                        self.player_choice = ''
                        self.computer_choice = ''
                        self.pve()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect2.collidepoint(event.pos):
                        self.player_score = 0
                        self.computer_score = 0
                        self.player_choice = ''
                        self.computer_choice = ''
                        self.menu()

            self.screen.blit(self.background, self.background_rect)

            if self.player_choice == self.computer_choice:
                font = pygame.font.SysFont('comicsans', 30)
                label = font.render('DRAW', True, (255, 255, 255))
                self.screen.blit(label, (200, 0))

            elif self.player_choice == 'paper' and self.computer_choice == 'scissor' \
                    or self.player_choice == 'scissor' and self.computer_choice == 'rock' \
                    or self.player_choice == 'rock' and self.computer_choice == 'paper':
                font = pygame.font.SysFont('comicsans', 30)
                label = font.render('PLAYER2 WINS', True, (255, 255, 255))
                self.screen.blit(label, (140, 0))

            elif self.player_choice == 'paper' and self.computer_choice == 'rock' \
                    or self.player_choice == 'scissor' and self.computer_choice == 'paper' \
                    or self.player_choice == 'rock' and self.computer_choice == 'scissor':
                font = pygame.font.SysFont('comicsans', 30)
                label = font.render('PLAYER1 WINS', True, (255, 255, 255))
                self.screen.blit(label, (140, 0))

            if active1:
                color1 = color_active1
            else:
                color1 = color_passive1

            pygame.draw.rect(self.screen, color1, input_rect1, 2)
            back = basic_font.render(back_text, True, (0, 255, 0))
            self.screen.blit(back, (input_rect1.x + 5, input_rect1.y + 5))
            input_rect1.w = back.get_width() + 10

            points = basic_font.render(score, True, (255, 0, 0))  # Score - text
            self.screen.blit(points, (125, 255))

            pygame.draw.rect(self.screen, color, input_rect2, 2)
            back_menu = basic_font.render(back_menu_text, True, (0, 255, 0))
            self.screen.blit(back_menu, (input_rect2.x, input_rect2.y + 5))
            input_rect2.w = back_menu.get_width() + 10

            pygame.display.flip()


if __name__ == '__main__':
    g = StartGame()
    while g.playing:
        g.playing = True
        g.game_loop()
