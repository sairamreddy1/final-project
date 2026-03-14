import pygame
import random
import sys
import matplotlib.pyplot as plt

pygame.init()
pygame.mixer.init()




# BACKGROUND MUSIC
pygame.mixer.music.load("yakastreams-retro-gaming-271301.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


WIDTH = 1000
HEIGHT = 650
CELL = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wandering in the Woods")

font = pygame.font.SysFont("Arial", 22)
bigfont = pygame.font.SysFont("Arial", 42)

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(30,120,40)
RED=(200,0,0)
BLUE=(0,0,200)
YELLOW=(255,230,50)

paused = False


clock = pygame.time.Clock()

# --------------------------------------------------
# PLAYER
# --------------------------------------------------

class Player:

    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        self.size=1

    def move(self,w,h):

        d=random.choice(["up","down","left","right"])

        if d=="up" and self.y>0:
            self.y-=1
        elif d=="down" and self.y<h-1:
            self.y+=1
        elif d=="left" and self.x>0:
            self.x-=1
        elif d=="right" and self.x<w-1:
            self.x+=1

    def draw(self):

        pygame.draw.circle(
            screen,
            self.color,
            (self.x*CELL+CELL//2,self.y*CELL+CELL//2),
            10+self.size*3
        )

# --------------------------------------------------
# GRID
# --------------------------------------------------

def draw_grid(w,h):

    for x in range(w):
        pygame.draw.line(screen,(60,160,60),(x*CELL,0),(x*CELL,h*CELL))

    for y in range(h):
        pygame.draw.line(screen,(60,160,60),(0,y*CELL),(w*CELL,y*CELL))

# --------------------------------------------------
# BUTTON
# --------------------------------------------------

def button(x,y,w,h,text):

    pygame.draw.rect(screen,(200,200,200),(x,y,w,h))
    label=font.render(text,True,BLACK)
    screen.blit(label,(x+10,y+10))

    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    if x<mouse[0]<x+w and y<mouse[1]<y+h:
        if click[0]==1:
            pygame.time.delay(200)
            return True

    return False

# --------------------------------------------------
# INPUT BOX
# --------------------------------------------------

class InputBox:

    def __init__(self,x,y,w,h):
        self.rect=pygame.Rect(x,y,w,h)
        self.text=""
        self.active=False

    def handle_event(self,event):

        if event.type==pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                self.active=True
            else:
                self.active=False

        if event.type==pygame.KEYDOWN and self.active:

            if event.key==pygame.K_BACKSPACE:
                self.text=self.text[:-1]
            else:
                self.text+=event.unicode

    def draw(self):

        pygame.draw.rect(screen,WHITE,self.rect)
        txt=font.render(self.text,True,BLACK)
        screen.blit(txt,(self.rect.x+5,self.rect.y+5))
        pygame.draw.rect(screen,BLACK,self.rect,2)

# --------------------------------------------------
# MERGE PLAYERS
# --------------------------------------------------

def merge_players(players):

    pos_map={}

    for p in players:

        pos=(p.x,p.y)

        if pos not in pos_map:
            pos_map[pos]=[p]
        else:
            pos_map[pos].append(p)

    new_players=[]

    for pos,group in pos_map.items():

        if len(group)==1:
            new_players.append(group[0])
        else:
            merged=Player(pos[0],pos[1],BLUE)
            merged.size=sum(g.size for g in group)
            new_players.append(merged)

    return new_players

# --------------------------------------------------
# SIMULATION
# --------------------------------------------------

def run_simulation(grid_w,grid_h,players):

    global paused

    moves = 0

    while True:

        screen.fill(GREEN)
        draw_grid(grid_w,grid_h)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # BACK BUTTON
        if button(20,580,120,40,"Back"):
            return "back"

        # PAUSE BUTTON
        if button(160,580,120,40,"Pause"):
            paused = True
            result = pause_menu()

            if result == "home":
                return "home"

        if not paused:

            for p in players:
                p.move(grid_w,grid_h)

            players = merge_players(players)

            moves += 1

        for p in players:
            p.draw()

        screen.blit(font.render(f"Moves: {moves}",True,WHITE),(20,520))

        pygame.display.update()
        clock.tick(6)

        if len(players) == 1:
            return moves

def pause_menu():

    global paused

    while paused:

        screen.fill((20,100,40))

        screen.blit(bigfont.render("Paused",True,WHITE),(420,200))

        if button(420,300,160,50,"Resume"):
            paused = False
            return

        if button(420,380,160,50,"Home"):
            paused = False
            return "home"

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# --------------------------------------------------
# GAME OVER + GRAPH
# --------------------------------------------------

def show_results(results):

    shortest=min(results)
    longest=max(results)
    avg=sum(results)/len(results)

    # save score
    with open("scores.txt","a") as f:
        f.write(f"Shortest:{shortest} Longest:{longest} Average:{avg}\n")

    # graph
    plt.figure()
    plt.plot(results,marker="o")
    plt.title("Meeting Time per Simulation")
    plt.xlabel("Simulation Number")
    plt.ylabel("Moves Until Meeting")
    plt.grid(True)
    plt.show()

    while True:

        screen.fill((20,100,40))

        screen.blit(bigfont.render("Game Over",True,WHITE),(380,150))

        screen.blit(font.render(f"Shortest Run: {shortest}",True,WHITE),(420,260))
        screen.blit(font.render(f"Longest Run: {longest}",True,WHITE),(420,300))
        screen.blit(font.render(f"Average Run: {round(avg,2)}",True,WHITE),(420,340))

        if button(420,420,160,50,"Home"):
            return "home"

        pygame.display.update()

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

# --------------------------------------------------
# K-2 MODE
# --------------------------------------------------

def game_k2():

    grid = 10

    players = [
        Player(0,0,RED),
        Player(grid-1,grid-1,BLUE)
    ]

    result = run_simulation(grid,grid,players)

    if result == "back":
        return

    if result == "home":
        return

    return show_results([result])

# --------------------------------------------------
# GRADES 3-5 SETUP
# --------------------------------------------------

def game_35_setup():

    w_box=InputBox(420,220,120,32)
    h_box=InputBox(420,260,120,32)
    p_box=InputBox(420,300,120,32)

    while True:

        screen.fill((30,110,40))

        screen.blit(font.render("Grid Width",True,WHITE),(250,220))
        screen.blit(font.render("Grid Height",True,WHITE),(250,260))
        screen.blit(font.render("Players (2-4)",True,WHITE),(250,300))

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            w_box.handle_event(event)
            h_box.handle_event(event)
            p_box.handle_event(event)

        w_box.draw()
        h_box.draw()
        p_box.draw()

        if button(420,360,140,40,"Start"):

            grid_w=int(w_box.text)
            grid_h=int(h_box.text)
            players=int(p_box.text)

            p_list=[]

            for i in range(players):

                x=random.randint(0,grid_w-1)
                y=random.randint(0,grid_h-1)

                p_list.append(Player(x,y,RED))

            moves=run_simulation(grid_w,grid_h,p_list)

            return show_results([moves])

        if button(20,580,120,40,"Back"):
            return
        pygame.display.update()

# --------------------------------------------------
# GRADES 6-8 MODE
# --------------------------------------------------

def game_68():

    grid_box = InputBox(420,220,120,32)
    p_box = InputBox(420,260,120,32)
    s_box = InputBox(420,300,120,32)

    while True:

        screen.fill((30,120,40))

        screen.blit(font.render("Grid (example 10x10)",True,WHITE),(220,220))
        screen.blit(font.render("Players (2-4)",True,WHITE),(220,260))
        screen.blit(font.render("Simulations",True,WHITE),(220,300))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            grid_box.handle_event(event)
            p_box.handle_event(event)
            s_box.handle_event(event)

        grid_box.draw()
        p_box.draw()
        s_box.draw()

        if button(420,360,140,40,"Next"):

            grid = grid_box.text
            players = int(p_box.text)
            sims = int(s_box.text)

            grid_w = int(grid.split("x")[0])
            grid_h = int(grid.split("x")[1])

            return player_positions_68(grid_w,grid_h,players,sims)

        if button(20,580,120,40,"Back"):
            return

        pygame.display.update()


def player_positions_68(grid_w,grid_h,players,sims):

    placed_players=[]
    message="Click grid cells to place players"

    while True:

        screen.fill((30,120,40))
        draw_grid(grid_w,grid_h)

        screen.blit(font.render(message,True,WHITE),(320,20))
        screen.blit(font.render(f"Players placed: {len(placed_players)}/{players}",True,WHITE),(20,20))

        for p in placed_players:
            p.draw()

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:

                mx,my=pygame.mouse.get_pos()

                grid_x=mx//CELL
                grid_y=my//CELL

                if grid_x<grid_w and grid_y<grid_h:

                    if len(placed_players)<players:

                        placed_players.append(Player(grid_x,grid_y,RED))

        if len(placed_players)==players:

            if button(420,580,140,40,"Start"):

                start_positions=[(p.x,p.y) for p in placed_players]

                results=[]

                for i in range(sims):

                    p_list=[]

                    for pos in start_positions:
                        p_list.append(Player(pos[0],pos[1],RED))

                    moves=run_simulation(grid_w,grid_h,p_list)

                    if moves=="back":
                        return

                    if moves=="home":
                        return

                    results.append(moves)

                return show_results(results)

        if button(20,580,120,40,"Back"):
            return

        pygame.display.update()

# --------------------------------------------------
# LAUNCHER (HOME PAGE)
# --------------------------------------------------

def launcher():

    while True:

        screen.fill((20,100,40))

        screen.blit(bigfont.render("Wandering in the Woods",True,WHITE),(270,120))

        if button(400,250,200,60,"K-2"):
            game_k2()

        if button(400,340,200,60,"Grades 3-5"):
            game_35_setup()

        if button(400,430,200,60,"Grades 6-8"):
            game_68()

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

launcher()