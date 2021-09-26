from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500

def Bg():
    glBegin(GL_QUADS)
    glColor3ub(9, 11, 23)
    glVertex2f(0, 0)
    glVertex2f(0, 500)
    glVertex2f(500, 500)
    glVertex2f(500, 0)
    glEnd()

def Land():
    glBegin(GL_QUADS)
    glColor3ub(72, 171, 48)
    glVertex2f(0, 0)
    glVertex2f(0, 45)
    glVertex2f(500, 45)
    glVertex2f(500, 0)
    glEnd()

def Building():
    glBegin(GL_QUADS)
    glColor3ub(42, 156, 121)

    # Bangunan Utama
    glVertex2f(350, 45)
    glVertex2f(350, 200)
    glVertex2f(500, 200)
    glVertex2f(500, 45)
    
    # Atap Depan
    glVertex2f(325, 135)
    glVertex2f(325, 150)
    glVertex2f(350, 150)
    glVertex2f(350, 135)

    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(28, 26, 26)

    # Pelindung kaca lantai bawah
    glVertex2f(360, 70)
    glVertex2f(360, 115)
    glVertex2f(500, 115)
    glVertex2f(500, 70)

    # Pelindung kaca lantai atas
    glVertex2f(360, 140)
    glVertex2f(360, 185)
    glVertex2f(500, 185)
    glVertex2f(500, 140)

    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(209, 224, 240)

    # Kaca lantai bawah
    glVertex2f(365, 75)
    glVertex2f(365, 110)
    glVertex2f(500, 110)
    glVertex2f(500, 75)

    # Kaca lantai atas
    glVertex2f(365, 145)
    glVertex2f(365, 180)
    glVertex2f(500, 180)
    glVertex2f(500, 145)

    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(28, 26, 26)

    # Pemisah kaca lantai bawah
    glVertex2f(400, 73)
    glVertex2f(400, 112)
    glVertex2f(405, 112)
    glVertex2f(405, 73)

    glVertex2f(440, 73)
    glVertex2f(440, 112)
    glVertex2f(445, 112)
    glVertex2f(445, 73)

    glVertex2f(480, 73)
    glVertex2f(480, 112)
    glVertex2f(485, 112)
    glVertex2f(485, 73)

    # Pemisah kaca lantai atas
    glVertex2f(400, 143)
    glVertex2f(400, 182)
    glVertex2f(405, 182)
    glVertex2f(405, 143)

    glVertex2f(440, 143)
    glVertex2f(440, 182)
    glVertex2f(445, 182)
    glVertex2f(445, 143)

    glVertex2f(480, 143)
    glVertex2f(480, 182)
    glVertex2f(485, 182)
    glVertex2f(485, 143)

    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(8, 46, 4)

    # Bayangan Gedung
    glVertex2f(390, 20)
    glVertex2f(350, 45)
    glVertex2f(500, 45)
    glVertex2f(500, 20)
    glVertex2f(365, 25)
    glVertex2f(355, 30)
    glVertex2f(400, 30)
    glVertex2f(400, 25)
    
    glEnd()

def platform_roket():
    # Alas menara dan roket
    glColor3ub(85, 75, 75)
    glBegin(GL_POLYGON) 
    glVertex2f(20, 50)
    glVertex2f(220, 50)
    glVertex2f(220, 70)
    glVertex2f(150, 70)
    glVertex2f(150, 80)
    glVertex2f(20, 80)
    glEnd()

    # kaki kiri
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(80, 40)
    glVertex2f(80, 50)
    glVertex2f(50, 50)
    glVertex2f(50, 40)
    glEnd()

    # kaki kiri 2
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    # titik A
    glVertex2f(40, 30)
    # titik B
    glVertex2f(90, 30)
    # titik C
    glVertex2f(80, 40)
    # titik F
    glVertex2f(50, 40)
    glEnd()

    # kaki kanan
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(170, 40)
    glVertex2f(170, 50)
    glVertex2f(140, 50)
    glVertex2f(140, 40)
    glEnd()

    # kaki kanan 2
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(130, 30)
    glVertex2f(180, 30)
    glVertex2f(170, 40)
    glVertex2f(140, 40)
    glEnd()

def menara():
    # tiang kiri bawah
    glColor3ub(148, 15, 15)
    glBegin(GL_QUADS) 
    glVertex2f(30, 80)
    glVertex2f(40, 80)
    glVertex2f(50, 140)
    glVertex2f(40, 140)
    glEnd()

    # tiang kiri atas
    glColor3ub(148, 15, 15)
    glBegin(GL_QUADS) 
    glVertex2f(40, 140)
    glVertex2f(50, 140)
    glVertex2f(50, 350)
    glVertex2f(40, 350)
    glEnd()

    # tiang kanan bawah
    glColor3ub(148, 15, 15)
    glBegin(GL_QUADS) 
    glVertex2f(110, 80)
    glVertex2f(125, 80)
    glVertex2f(115, 140)
    glVertex2f(100, 140)
    glEnd()

    # tiang kanan atas
    glColor3ub(148, 15, 15)
    glBegin(GL_QUADS) 
    glVertex2f(100, 140)
    glVertex2f(115, 140)
    glVertex2f(115, 350)
    glVertex2f(100, 350)
    glEnd()

    # atap menara
    glColor3ub(117, 19, 19)
    glBegin(GL_QUADS) 
    glVertex2f(50, 350)
    glVertex2f(100, 350)
    glVertex2f(100, 345)
    glVertex2f(50, 345)
    glEnd()

    # atas atap menara
    glColor3ub(214, 214, 0)
    glBegin(GL_QUADS) 
    glVertex2f(55, 350)
    glVertex2f(95, 350)
    glVertex2f(95, 360)
    glVertex2f(55, 360)
    glEnd()

    # bayangan menara
    glBegin(GL_QUADS)
    glColor3ub(8, 46, 4)
    # kaki kiri 2
    glVertex2f(40, 30)
    glVertex2f(90, 30)
    glVertex2f(80, 20)
    glVertex2f(50, 20)
    glEnd()

    # kaki kiri
    glBegin(GL_QUADS)
    glColor3ub(8, 46, 4)
    glVertex2f(90, 10)
    glVertex2f(80, 20)
    glVertex2f(50, 20)
    glVertex2f(60, 10)
    glEnd()

    # kaki kanan 2
    glColor3ub(8, 46, 4)
    glBegin(GL_QUADS) 
    glVertex2f(130, 30)
    glVertex2f(180, 30)
    glVertex2f(170, 20)
    glVertex2f(140, 20)
    glEnd()

    # kaki kanan
    glColor3ub(8, 46, 4)
    glBegin(GL_QUADS)
    glVertex2f(180, 10)
    glVertex2f(170, 20)
    glVertex2f(140, 20)
    glVertex2f(150, 10)
    glEnd()

    # alas menara dan roket
    glColor3ub(8, 46, 4)
    glBegin(GL_QUADS) 
    glVertex2f(80, 20)
    glVertex2f(220, 20)
    glVertex2f(230, 10)
    glVertex2f(90, 10)
    glEnd()

    # tiang kiri
    glColor3ub(8, 46, 4)
    glBegin(GL_QUADS) 
    # 80 85 140 145
    glVertex2f(70, 10)
    glVertex2f(80, 10)
    glVertex2f(90, 5)
    glVertex2f(80, 5)
    glEnd()

    # tiang kanan
    glColor3ub(8, 46, 4)
    glBegin(GL_QUADS) 
    glVertex2f(130, 10)
    glVertex2f(140, 10)
    glVertex2f(150, 5)
    glVertex2f(140, 5)
    glEnd()

    # besi kiri
    glColor3ub(8, 46, 4)
    glBegin(GL_LINES) 
    glVertex2f(70, 10)
    glVertex2f(140, 5)
    glEnd()

    # besi kanan
    glColor3ub(8, 46, 4)
    glBegin(GL_LINES) 
    glVertex2f(140, 10)
    glVertex2f(90, 5)
    glEnd()

def jembatan():
    # alas jembatan roket
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(115, 270)
    glVertex2f(155, 270)
    glVertex2f(155, 275)
    glVertex2f(115, 275)
    glEnd()

    # atap jembatan roket
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(115, 310)
    glVertex2f(155, 310)
    glVertex2f(155, 315)
    glVertex2f(115, 315)
    glEnd()

    # penutup kaca jembatan
    glColor3ub(224, 220, 220)
    glBegin(GL_QUADS) 
    glVertex2f(115, 275)
    glVertex2f(155, 275)
    glVertex2f(155, 310)
    glVertex2f(115, 310)
    glEnd()

    # besi atas
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(115, 310)
    glVertex2f(125, 275)
    glEnd()

    # besi atas 2
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(125, 310)
    glVertex2f(135, 275)
    glEnd()

    # besi atas 3
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(135, 310)
    glVertex2f(145, 275)
    glEnd()

    # besi bawah
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(125, 310)
    glVertex2f(115, 275)
    glEnd()

    # besi bawah 2
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(135, 310)
    glVertex2f(125, 275)
    glEnd()

    # besi bawah 3
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(145, 310)
    glVertex2f(135, 275)
    glEnd()

    # pintu jembatan
    glColor3ub(196, 196, 196)
    glBegin(GL_QUADS) 
    glVertex2f(150, 275)
    glVertex2f(155, 275)
    glVertex2f(155, 310)
    glVertex2f(150, 310)
    glEnd()

def tiang_tengah():
    # kiri
    glBegin(GL_QUADS)
    glColor3ub(85, 75, 75)
    glVertex2f(60, 50)
    glVertex2f(65, 50)
    glVertex2f(65, 345)
    glVertex2f(60, 345)
    glEnd()

    # kanan
    glBegin(GL_QUADS)
    glColor3ub(85, 75, 75)
    glVertex2f(85, 50)
    glVertex2f(90, 50)
    glVertex2f(90, 345)
    glVertex2f(85, 345)
    glEnd()

def rangkaian_besi():
    # besi_kiri
    glBegin(GL_LINES) 
    glVertex2f(50, 345)
    glVertex2f(100, 330)
    glEnd()

    # besi kiri 2
    glBegin(GL_LINES)
    glVertex2f(50, 330)
    glVertex2f(100, 315)
    glEnd()

    # besi kiri 3
    glBegin(GL_LINES) 
    glVertex2f(50, 310)
    glVertex2f(100, 295)
    glEnd()

    # besi kiri 4
    glBegin(GL_LINES) 
    glVertex2f(50, 290)
    glVertex2f(100, 275)
    glEnd()

    # besi kiri 5
    glBegin(GL_LINES) 
    glVertex2f(50, 270)
    glVertex2f(100, 255)
    glEnd()

    # besi kiri 6
    glBegin(GL_LINES) 
    glVertex2f(50, 250)
    glVertex2f(100, 235)
    glEnd()

    # besi kiri 7
    glBegin(GL_LINES) 
    glVertex2f(50, 230)
    glVertex2f(100, 215)
    glEnd()

    # besi kiri 8
    glBegin(GL_LINES) 
    glVertex2f(50, 210)
    glVertex2f(100, 195)
    glEnd()

    # besi kiri 9
    glBegin(GL_LINES) 
    glVertex2f(50, 190)
    glVertex2f(100, 175)
    glEnd()

    # besi kiri 10
    glBegin(GL_LINES) 
    glVertex2f(50, 170)
    glVertex2f(100, 155)
    glEnd()

    # besi kiri 11
    glBegin(GL_LINES) 
    glVertex2f(50, 150)
    glVertex2f(101, 135)
    glEnd()

    # besi kiri 12
    glBegin(GL_LINES) 
    glVertex2f(48, 130)
    glVertex2f(104, 115)
    glEnd()

    # besi kiri 13
    glBegin(GL_LINES)
    glVertex2f(45, 110)
    glVertex2f(107, 95)
    glEnd()

def rangkaian_besi2():
    # besi_kanan
    glBegin(GL_LINES) 
    glVertex2f(100, 345)
    glVertex2f(50, 330)
    glEnd()

    # besi kanan 2
    glBegin(GL_LINES) 
    glVertex2f(100, 330)
    glVertex2f(50, 315)
    glEnd()

    # besi kanan 3
    glBegin(GL_LINES) 
    glVertex2f(100, 310)
    glVertex2f(50, 295)
    glEnd()

    # besi kanan 4
    glBegin(GL_LINES) 
    glVertex2f(100, 290)
    glVertex2f(50, 275)
    glEnd()

    # besi kanan 5
    glBegin(GL_LINES) 
    glVertex2f(100, 270)
    glVertex2f(50, 255)
    glEnd()

    # besi kanan 6
    glBegin(GL_LINES) 
    glVertex2f(100, 250)
    glVertex2f(50, 235)
    glEnd()

    # besi kanan 7
    glBegin(GL_LINES) 
    glVertex2f(100, 230)
    glVertex2f(50, 215)
    glEnd()

    # besi kanan 8
    glBegin(GL_LINES) 
    glVertex2f(100, 210)
    glVertex2f(50, 195)
    glEnd()

    # besi kanan 9
    glBegin(GL_LINES) 
    glVertex2f(100, 190)
    glVertex2f(50, 175)
    glEnd()

    # besi kanan 10
    glBegin(GL_LINES) 
    glVertex2f(100, 170)
    glVertex2f(50, 155)
    glEnd()

    # besi kanan 11
    glBegin(GL_LINES) 
    glVertex2f(100, 150)
    glVertex2f(49, 135)
    glEnd()

    # besi kanan 12
    glBegin(GL_LINES) 
    glVertex2f(102, 130)
    glVertex2f(46, 115)
    glEnd()

    # besi kanan 13
    glBegin(GL_LINES) 
    glVertex2f(105, 110)
    glVertex2f(42, 95)
    glEnd()

def iterate():
    glViewport(0, 0, 1364, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    Bg()
    Land()
    Building()
    platform_roket()
    menara()
    tiang_tengah()
    jembatan()
    glColor3ub(117, 19, 19)
    rangkaian_besi()
    rangkaian_besi2()
    glutSwapBuffers() 

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1364, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("PESAWAT LUAR ANGKASA")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()