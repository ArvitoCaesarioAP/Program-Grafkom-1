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
    
    # bintang
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(120, 95) 
    glVertex2f(124, 95) 
    glVertex2f(124, 100) 
    glVertex2f(120, 100) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(125, 123) 
    glVertex2f(126, 123) 
    glVertex2f(126, 125)
    glVertex2f(125, 125) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(125, 250) 
    glVertex2f(126, 250) 
    glVertex2f(126, 253) 
    glVertex2f(125, 253) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(125, 450) 
    glVertex2f(126, 450) 
    glVertex2f(126, 453) 
    glVertex2f(125, 453) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(95, 450) 
    glVertex2f(96, 450) 
    glVertex2f(96, 453) 
    glVertex2f(95, 453) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(10, 60) 
    glVertex2f(11, 60)  
    glVertex2f(11, 63) 
    glVertex2f(10, 63)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(10, 200)
    glVertex2f(11, 200)
    glVertex2f(11, 203)
    glVertex2f(10, 203)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(20, 250)
    glVertex2f(21, 250)
    glVertex2f(21, 253)
    glVertex2f(20, 253)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(499, 250)
    glVertex2f(500, 250)
    glVertex2f(500, 253)
    glVertex2f(499, 253)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(399, 250)
    glVertex2f(400, 250)
    glVertex2f(400, 253)
    glVertex2f(399, 253)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(10, 300)
    glVertex2f(11, 300)
    glVertex2f(11, 303)
    glVertex2f(10, 303)
    glEnd()
    
    glColor3ub(255, 255, 255)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(200, 100)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(7.0)
    glBegin(GL_POINTS)
    glVertex2f(300, 200)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(400, 250)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(450, 300)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(7.0)
    glBegin(GL_POINTS)
    glVertex2f(425, 355)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(80, 320)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(160, 300)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(180, 420)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(7.0)
    glBegin(GL_POINTS)
    glVertex2f(230, 400)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(7.0)
    glBegin(GL_POINTS)
    glVertex2f(20, 450)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(250, 300)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(330, 410)
    glEnd()

    glColor3ub(255, 255, 255)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(55, 130)
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
    glColor3ub(148, 15, 15)
    glBegin(GL_QUADS) 
    glVertex2f(30, 350)
    glVertex2f(155, 350)
    glVertex2f(155, 360)
    glVertex2f(30, 360)
    glEnd()

    # atas atap menara 2
    glColor3ub(148, 15, 15)
    glBegin(GL_QUADS) 
    glVertex2f(30, 360)
    glVertex2f(80, 360)
    glVertex2f(80, 370)
    glVertex2f(30, 370)
    glEnd()

    # atas atap menara 3 
    glColor3ub(148, 15, 15)
    glBegin(GL_LINE_LOOP) 
    glVertex2f(40, 359)
    glVertex2f(40, 400)
    glVertex2f(70, 400)
    glVertex2f(100, 390)
    glVertex2f(140, 380)
    glVertex2f(140, 359)
    glEnd()

    # atas atap menara 4
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(55, 400)
    glVertex2f(55, 370)
    glEnd()

    # atas atap menara 5
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(70, 400)
    glVertex2f(70, 370)
    glEnd()

    # atas atap menara 6
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(85, 395)
    glVertex2f(85, 360)
    glEnd()

    # atas atap menara 7
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(100, 390)
    glVertex2f(100, 360)
    glEnd()

    # atas atap menara 8
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(115, 385)
    glVertex2f(115, 360)
    glEnd()

    # atas atap menara 9
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(130, 382)
    glVertex2f(130, 360)
    glEnd()

    # besi atas
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(40, 400)
    glVertex2f(55, 370)
    glEnd()

    # besi atas 2
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(55, 370)
    glVertex2f(70, 400)
    glEnd()

    # besi atas 3
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(70, 400)
    glVertex2f(85, 360)
    glEnd()

    # besi atas 4
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(85, 360)
    glVertex2f(100, 390)
    glEnd()

    # besi atas 5
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(100, 390)
    glVertex2f(115, 360)
    glEnd()

    # besi atas 6
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(115, 360)
    glVertex2f(130, 383)
    glEnd()

    # besi atas 6
    glColor3ub(148, 15, 15)
    glBegin(GL_LINES) 
    glVertex2f(130, 383)
    glVertex2f(140, 360)
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
    
    #ROKET
    # sayap kiri
    glBegin(GL_POLYGON)
    glColor3ub(237, 16, 0)
    glVertex2f(161, 130)
    glVertex2f(161, 110)
    glVertex2f(161, 103)
    glVertex2f(161, 71)
    glVertex2f(153, 71)
    glVertex2f(153, 103)
    glEnd()

    #kuncupnya
    glBegin(GL_POLYGON)
    glColor3ub(237, 16, 0)
    glVertex2f(181, 400 ) 
    glVertex2f(168, 360) 
    glVertex2f(195, 360)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(248, 255, 56)
    glVertex2f(180, 409)
    glVertex2f(182, 409)
    glVertex2f(182, 397)
    glVertex2f(180, 397)
    glEnd()

    #badan roket
    glBegin(GL_POLYGON)
    glColor3ub(167, 184, 252)
    glVertex2f(195, 361)
    glVertex2f(195, 230)
    glVertex2f(195, 210)
    glVertex2f(195, 95)
    glVertex2f(168, 95)
    glVertex2f(168, 361)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(9, 11, 23)
    glVertex2f(167, 100)
    glVertex2f(168, 100)
    glVertex2f(168, 95)
    glVertex2f(167, 95)
    glEnd()

    #sabuk bawah
    glColor3ub(1, 1, 66)
    glBegin(GL_QUADS)
    glVertex2f(168, 95) 
    glVertex2f(195, 95) 
    glVertex2f(195, 100) 
    glVertex2f(168, 100) 
    glEnd()

    #Bintang-kecil
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(120, 95) 
    glVertex2f(124, 95) 
    glVertex2f(124, 100) 
    glVertex2f(120, 100) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(125, 123) 
    glVertex2f(126, 123) 
    glVertex2f(126, 125)
    glVertex2f(125, 125) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(125, 250) 
    glVertex2f(126, 250) 
    glVertex2f(126, 253) 
    glVertex2f(125, 253) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(125, 450) 
    glVertex2f(126, 450) 
    glVertex2f(126, 453) 
    glVertex2f(125, 453) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(95, 450) 
    glVertex2f(96, 450) 
    glVertex2f(96, 453) 
    glVertex2f(95, 453) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(10, 60) 
    glVertex2f(11, 60)  
    glVertex2f(11, 63) 
    glVertex2f(10, 63)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(10, 200)
    glVertex2f(11, 200)
    glVertex2f(11, 203)
    glVertex2f(10, 203)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(20, 250)
    glVertex2f(21, 250)
    glVertex2f(21, 253)
    glVertex2f(20, 253)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(499, 250)
    glVertex2f(500, 250)
    glVertex2f(500, 253)
    glVertex2f(499, 253)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(399, 250)
    glVertex2f(400, 250)
    glVertex2f(400, 253)
    glVertex2f(399, 253)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(10, 300)
    glVertex2f(11, 300)
    glVertex2f(11, 303)
    glVertex2f(10, 303)
    glEnd()

    #Hiasannya
    glBegin(GL_QUADS)
    glColor3ub(97, 97, 97)
    glVertex2f(190, 292)
    glVertex2f(192, 292)
    glVertex2f(192, 290)
    glVertex2f(190, 290)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(97, 97, 97)
    glVertex2f(180, 297)
    glVertex2f(182, 297)
    glVertex2f(182, 295)
    glVertex2f(180, 295)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(97, 97, 97)
    glVertex2f(185, 302)
    glVertex2f(187, 302)
    glVertex2f(187, 300)
    glVertex2f(185, 300)
    glEnd()

    #jendela roket persegi
    glBegin(GL_LINES)
    glColor3ub(94, 93, 92)
    glVertex2f(170, 177)
    glVertex2f(193, 177)
    glVertex2f(193, 200)
    glVertex2f(170, 200)
    glEnd()
    
    #Pintu biru
    glBegin(GL_QUADS)
    glColor3ub(1, 1, 66)
    glVertex2f(169, 315 ) 
    glVertex2f(180, 315) 
    glVertex2f(180, 276) 
    glVertex2f(169, 276)
    glEnd()

    #Seleret pintunya
    glBegin(GL_QUADS)
    glColor3ub(199, 129, 0)
    glVertex2f(180, 280)
    glVertex2f(195, 280)
    glVertex2f(195, 276)
    glVertex2f(180, 276)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(199, 129, 0)
    glVertex2f(180, 315)
    glVertex2f(195, 315)
    glVertex2f(195, 311)
    glVertex2f(180, 311)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(199, 129, 0)
    glVertex2f(168, 244)
    glVertex2f(195, 244)
    glVertex2f(195, 240)
    glVertex2f(168, 240)
    glEnd()

    #gagang pintu
    glColor3ub(211, 243, 245)
    glBegin(GL_QUADS)
    glVertex2f(170, 300) 
    glVertex2f(173, 300) 
    glVertex2f(173, 293) 
    glVertex2f(170, 293)
    glEnd()

    #Bendera merah Putih
    glColor3ub(250, 2, 7)
    glBegin(GL_QUADS)
    glVertex2f(193, 352) 
    glVertex2f(181, 352) 
    glVertex2f(181, 345)
    glVertex2f(193, 345) 
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(193, 345) 
    glVertex2f(181, 345) 
    glVertex2f(181, 338) 
    glVertex2f(193, 338) 
    glEnd()
    
    #Hiasan Segitiga bawah atas
    glBegin(GL_LINE_BIT)
    glColor3ub(94, 93, 92)
    glVertex2f(170, 140)
    glVertex2f(193, 140)
    glVertex2f(193, 170)
    glVertex2f(170, 170)
    glEnd()

    #Hiasan segitiga bawah
    glBegin(GL_TRIANGLES)
    glColor3ub(94, 93, 92)
    glVertex2f(170, 125) 
    glVertex2f(170, 100)
    glVertex2f(193, 125)
    glEnd()

    glBegin(GL_LINE_STRIP);
    glVertex2f (170, 340);
    glVertex2f (170, 360);
    glEnd()
    
    #sabuk atas
    glColor3ub(1, 1, 66)
    glBegin(GL_QUADS)
    glVertex2f(168, 357) 
    glVertex2f(195, 357)  
    glVertex2f(195, 361) 
    glVertex2f(168, 361)
    glEnd()

    #Tulisan INA
    # I
    glBegin(GL_QUADS)
    glColor3ub(1, 1, 66)
    glVertex2f(170, 206)
    glVertex2f(172, 206)
    glVertex2f(172, 230)
    glVertex2f(170, 230)
    glEnd()
    #N
    glBegin(GL_QUADS)
    glColor3ub(1, 1, 66)
    glVertex2f(174, 206)
    glVertex2f(176, 206)
    glVertex2f(176, 230)
    glVertex2f(174, 230)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(1, 1, 66)
    glVertex2f(176, 230)
    glVertex2f(181, 216)
    glVertex2f(181, 206)
    glVertex2f(176, 220)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(1, 1, 66)
    glVertex2f(181, 206)
    glVertex2f(183, 206)
    glVertex2f(183, 230)
    glVertex2f(181, 230)
    glEnd()

    #A
    glBegin(GL_QUADS)
    glColor3ub(1, 1, 66)
    glVertex2f(184, 206)
    glVertex2f(186, 206)
    glVertex2f(188, 230)
    glVertex2f(186, 230)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(1, 1, 66)
    glVertex2f(190, 206)
    glVertex2f(192, 206)
    glVertex2f(190, 230)
    glVertex2f(188, 230)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(1, 1, 66)
    glVertex2f(186, 210)
    glVertex2f(190, 210)
    glVertex2f(190, 212)
    glVertex2f(186, 212)
    glEnd()

    #titik bawah
    glColor3ub(1, 1, 66)
    glBegin(GL_QUADS)
    glVertex2f(172, 164) 
    glVertex2f(174, 164) 
    glVertex2f(174, 167) 
    glVertex2f(172, 167) 
    glEnd()

    glColor3ub(1, 1, 66)
    glBegin(GL_QUADS)
    glVertex2f(172, 159) 
    glVertex2f(174, 159) 
    glVertex2f(174, 162) 
    glVertex2f(172, 162) 
    glEnd()

    glColor3ub(1, 1, 66)
    glBegin(GL_QUADS)
    glVertex2f(172, 155)
    glVertex2f(174, 155) 
    glVertex2f(174, 158) 
    glVertex2f(172, 158)
    glEnd()

    #sabuk
    glColor3ub(1, 1, 66)
    glBegin(GL_QUADS)
    glVertex2f(168, 130)
    glVertex2f(195, 130) 
    glVertex2f(195, 135) 
    glVertex2f(168, 135) 
    glEnd()

    #bawah roket
    glBegin(GL_QUADS)
    glColor3ub(219, 202, 193)
    glVertex2f(170, 80)
    glVertex2f(193, 80)
    glVertex2f(190, 95)
    glVertex2f(173, 95)
    glEnd()

    #gagang sayap kiri
    glColor3ub(237, 16, 0)
    glBegin(GL_QUADS)
    glVertex2f(160, 110 ) 
    glVertex2f(168, 130) 
    glVertex2f(168, 100) 
    glVertex2f(160, 90) 
    glEnd()
    
    #gagang sayap kanan
    glColor3ub(237, 16, 0)
    glBegin(GL_QUADS)
    glVertex2f(203, 110) 
    glVertex2f(195, 130) 
    glVertex2f(195, 100) 
    glVertex2f(203, 90) 
    glEnd()

    #sayap depan roket
    glColor3ub(237, 16, 0)
    glBegin(GL_POLYGON)
    glVertex2f(179, 130)
    glVertex2f(179, 120)
    glVertex2f(179, 100)
    glVertex2f(179, 71)
    glVertex2f(185, 71)
    glVertex2f(185, 110)
    glEnd()

    #sayap kanan roket
    glColor3ub(237, 16, 0)
    glBegin(GL_POLYGON)
    glVertex2f(202, 130)
    glVertex2f(202, 110)
    glVertex2f(202, 100)
    glVertex2f(202, 71)
    glVertex2f(210, 71)
    glVertex2f(210, 100)
    glEnd()

    # bayangan Roket
    glBegin(GL_QUADS)
    glColor3ub(8, 46, 4) 
    glVertex2f(190, 10)
    glVertex2f(220, 10)
    glVertex2f(230, 5)
    glVertex2f(220, 5)
    glEnd()

def jembatan():
    # jembatan atas
    # alas jembatan roket
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(115, 270)
    glVertex2f(165, 270)
    glVertex2f(165, 275)
    glVertex2f(115, 275)
    glEnd()

    # atap jembatan roket
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(115, 310)
    glVertex2f(165, 310)
    glVertex2f(165, 315)
    glVertex2f(115, 315)
    glEnd()

    # penutup kaca jembatan
    glColor3ub(224, 220, 220)
    glBegin(GL_QUADS) 
    glVertex2f(115, 275)
    glVertex2f(165, 275)
    glVertex2f(165, 310)
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
    
    # besi atas 4
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(145, 310)
    glVertex2f(155, 275)
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
    
    # besi bawah 4
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(155, 310)
    glVertex2f(145, 275)
    glEnd()

    # pintu jembatan
    glColor3ub(196, 196, 196)
    glBegin(GL_QUADS) 
    glVertex2f(150, 275)
    glVertex2f(165, 275)
    glVertex2f(165, 310)
    glVertex2f(150, 310)
    glEnd()

    # jembatan bawah
    # alas jembatan roket 
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(115, 170)
    glVertex2f(165, 170)
    glVertex2f(165, 175)
    glVertex2f(115, 175)
    glEnd()

    # atap jembatan roket bawah
    glColor3ub(85, 75, 75)
    glBegin(GL_QUADS) 
    glVertex2f(115, 200)
    glVertex2f(165, 200)
    glVertex2f(165, 205)
    glVertex2f(115, 205)
    glEnd()

    # penutup kaca jembatan
    glColor3ub(224, 220, 220)
    glBegin(GL_QUADS) 
    glVertex2f(115, 175)
    glVertex2f(165, 175)
    glVertex2f(165, 200)
    glVertex2f(115, 200)
    glEnd()

    # besi atas
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(115, 200)
    glVertex2f(125, 175)
    glEnd()

    # besi atas 2
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(125, 200)
    glVertex2f(135, 175)
    glEnd()

    # besi atas 3
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(135, 200)
    glVertex2f(145, 175)
    glEnd()
    
    # besi atas 4
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(145, 200)
    glVertex2f(145, 175)
    glEnd()

    # besi bawah
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(125, 200)
    glVertex2f(115, 175)
    glEnd()

    # besi bawah 2
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(135, 200)
    glVertex2f(125, 175)
    glEnd()

    # besi bawah 3
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(145, 200)
    glVertex2f(135, 175)
    glEnd()
    
    # besi bawah 4
    glColor3ub(196, 196, 196)
    glBegin(GL_LINES) 
    glVertex2f(155, 200)
    glVertex2f(145, 175)
    glEnd()

    # pintu jembatan
    glColor3ub(196, 196, 196)
    glBegin(GL_QUADS) 
    glVertex2f(150, 175)
    glVertex2f(155, 175)
    glVertex2f(155, 200)
    glVertex2f(150, 200)
    glEnd()

def tiang_tengah():
    # kiri
    glBegin(GL_QUADS)
    glColor3ub(148, 15, 15)
    glVertex2f(60, 80)
    glVertex2f(65, 80)
    glVertex2f(65, 345)
    glVertex2f(60, 345)
    glEnd()

    # kanan
    glBegin(GL_QUADS)
    glColor3ub(148, 15, 15)
    glVertex2f(85, 80)
    glVertex2f(90, 80)
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

def alien():
    #kaki
    glBegin(GL_POLYGON)
    glColor3ub(0, 128, 0)
    glVertex2f(367,140)
    glVertex2f(370,130)
    glVertex2f(371,120)
    glVertex2f(370,100)
    glVertex2f(369,80)
    glVertex2f(370,75)
    glVertex2f(370,70)
    glVertex2f(371,65)
    glVertex2f(375,30)
    glVertex2f(380,20)
    glVertex2f(366,20)
    glVertex2f(320,20)
    glVertex2f(320,25)
    glEnd()
    
    #kepala
    glBegin(GL_POLYGON)
    glColor3ub(112, 224, 0)
    glVertex2f(322,30)
    glVertex2f(323,40)
    glVertex2f(323,60)
    glVertex2f(325,80)
    glVertex2f(320,100)
    glVertex2f(319,120)
    glVertex2f(320,130)
    glVertex2f(325,150)
    glVertex2f(332,157)
    glVertex2f(335,160)
    glVertex2f(340,163)
    glVertex2f(350,163)
    glVertex2f(355,160)
    glVertex2f(358,157)
    glVertex2f(365,150)
    glVertex2f(368,130)
    glVertex2f(368,110)
    glVertex2f(366,85)
    glVertex2f(363,70)
    glVertex2f(360,50)
    glVertex2f(355,40)
    glVertex2f(350,35)
    glVertex2f(330,33)
    glVertex2f(320,30)
    glEnd()

    #tanduk
    glBegin(GL_TRIANGLES)
    glVertex2f(325,150)
    glVertex2f(323,190)
    glVertex2f(338,150)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(352,150)
    glVertex2f(363,190)
    glVertex2f(365,150)
    glEnd()

    #tangan
    glBegin(GL_QUADS)
    glVertex2f(325,80)
    glVertex2f(305,90)
    glVertex2f(306,80)
    glVertex2f(325,55)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 0)
    glVertex2f(370,80)
    glVertex2f(390,60)
    glVertex2f(391,55)
    glVertex2f(370,55)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(255, 234, 0)
    glVertex2f(300,150)
    glVertex2f(308,60)
    glVertex2f(310,61)
    glVertex2f(302,151)
    glEnd()
    #sinar_tongkat
    glColor3ub(255,255,255)
    glBegin(GL_LINES)
    glVertex2f(298,171)
    glVertex2f(298,143)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(291,157)
    glVertex2f(306,157)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(294,166)
    glVertex2f(302,149)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(302,166)
    glVertex2f(294,149)
    glEnd()

    #mulut
    glBegin(GL_POLYGON)
    glColor3ub(176, 48, 54)
    glVertex2f(335,95)
    glVertex2f(333,93)
    glVertex2f(331,90)
    glVertex2f(330,85)
    glVertex2f(331,80)
    glVertex2f(333,75)
    glVertex2f(335,70)
    glVertex2f(340,65)
    glVertex2f(350,65)
    glVertex2f(355,70)
    glVertex2f(357,75)
    glVertex2f(359,80)
    glVertex2f(360,85)
    glVertex2f(359,90)
    glVertex2f(357,93)
    glVertex2f(355,95)
    glEnd()

    #gigi
    glBegin(GL_TRIANGLES)
    glColor3ub(254, 223, 212)
    glVertex2f(335,95)
    glVertex2f(339,95)
    glVertex2f(337,85)
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3ub(254, 223, 212)
    glVertex2f(339,95)
    glVertex2f(343,95)
    glVertex2f(341,85)
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3ub(254, 223, 212)
    glVertex2f(343,95)
    glVertex2f(347,95)
    glVertex2f(345,85)
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3ub(254, 223, 212)
    glVertex2f(347,95)
    glVertex2f(351,95)
    glVertex2f(349,85)
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3ub(254, 223, 212)
    glVertex2f(351,95)
    glVertex2f(355,95)
    glVertex2f(353,85)
    glEnd()
    #lidah
    glBegin(GL_POLYGON)
    glColor3ub(227, 74, 74)
    glVertex2f(333,75)
    glVertex2f(335,70)
    glVertex2f(340,65)
    glVertex2f(350,65)
    glVertex2f(355,70)
    glVertex2f(357,75)
    glEnd()

    #mata utama
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(341,155)
    glVertex2f(335,150)
    glVertex2f(333,145)
    glVertex2f(331,140)
    glVertex2f(330,135)
    glVertex2f(330,130)
    glVertex2f(331,125)
    glVertex2f(333,120)
    glVertex2f(335,115)
    glVertex2f(341,110)
    glVertex2f(347,110)
    glVertex2f(353,115)
    glVertex2f(355,120)
    glVertex2f(357,125)
    glVertex2f(358,130)
    glVertex2f(358,135)
    glVertex2f(357,140)
    glVertex2f(355,145)
    glVertex2f(353,150)
    glVertex2f(347,155)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(0, 100, 0)
    glVertex2f(340,150)
    glVertex2f(335,145)
    glVertex2f(334,140)
    glVertex2f(333,135)
    glVertex2f(334,130)
    glVertex2f(335,125)
    glVertex2f(340,120)
    glVertex2f(347,120)
    glVertex2f(352,125)
    glVertex2f(353,130)
    glVertex2f(354,135)
    glVertex2f(353,140)
    glVertex2f(352,145)
    glVertex2f(347,150)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(0,0,0)
    glVertex2f(342,145)
    glVertex2f(340,142)
    glVertex2f(339,140)
    glVertex2f(338,136)
    glVertex2f(338,134)
    glVertex2f(339,131)
    glVertex2f(340,128)
    glVertex2f(342,127)
    glVertex2f(345,127)
    glVertex2f(347,128)
    glVertex2f(348,131)
    glVertex2f(349,134)
    glVertex2f(349,136)
    glVertex2f(348,140)
    glVertex2f(347,142)
    glVertex2f(345,145)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(342,140)
    glVertex2f(340,138)
    glVertex2f(341,137)
    glVertex2f(341,136)
    glVertex2f(342,134)
    glVertex2f(343,134)
    glVertex2f(344,136)
    glVertex2f(345,137)
    glVertex2f(345,138)
    glVertex2f(343,140)
    glEnd()
    
    #mata kiri
    glBegin(GL_POLYGON)
    glColor3ub(112, 224, 0)
    glVertex2f(317,203)
    glVertex2f(316,201)
    glVertex2f(315,198)
    glVertex2f(314,196)
    glVertex2f(314,192)
    glVertex2f(315,183)
    glVertex2f(316,182)
    glVertex2f(317,181)
    glVertex2f(318,180)
    glVertex2f(320,179)
    glVertex2f(326,179)
    glVertex2f(328,180)
    glVertex2f(329,181)
    glVertex2f(330,182)
    glVertex2f(331,183)
    glVertex2f(332,192)
    glVertex2f(332,196)
    glVertex2f(331,198)
    glVertex2f(329,201)
    glVertex2f(328,203)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(321,201)
    glVertex2f(319,198)
    glVertex2f(318,196)
    glVertex2f(317,192)
    glVertex2f(317,190)
    glVertex2f(318,187)
    glVertex2f(319,184)
    glVertex2f(321,183)
    glVertex2f(324,183)
    glVertex2f(326,184)
    glVertex2f(327,187)
    glVertex2f(328,190)
    glVertex2f(328,192)
    glVertex2f(327,196)
    glVertex2f(326,198)
    glVertex2f(324,201)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2f(323,200)
    glVertex2f(320,193)
    glVertex2f(323,186)
    glVertex2f(326,193)
    glEnd()
    #mata kanan
    glBegin(GL_POLYGON)
    glColor3ub(112, 224, 0)
    glVertex2f(357,203)
    glVertex2f(356,201)
    glVertex2f(355,198)
    glVertex2f(354,196)
    glVertex2f(354,192)
    glVertex2f(355,183)
    glVertex2f(356,182)
    glVertex2f(357,181)
    glVertex2f(358,180)
    glVertex2f(360,179)
    glVertex2f(366,179)
    glVertex2f(368,180)
    glVertex2f(369,181)
    glVertex2f(370,182)
    glVertex2f(371,183)
    glVertex2f(372,192)
    glVertex2f(372,196)
    glVertex2f(371,198)
    glVertex2f(369,201)
    glVertex2f(368,203)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(361,201)
    glVertex2f(359,198)
    glVertex2f(358,196)
    glVertex2f(357,192)
    glVertex2f(357,190)
    glVertex2f(358,187)
    glVertex2f(359,184)
    glVertex2f(361,183)
    glVertex2f(364,183)
    glVertex2f(366,184)
    glVertex2f(367,187)
    glVertex2f(368,190)
    glVertex2f(368,192)
    glVertex2f(367,196)
    glVertex2f(366,198)
    glVertex2f(364,201)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2f(363,200)
    glVertex2f(360,193)
    glVertex2f(363,186)
    glVertex2f(366,193)
    glEnd()
    
    #bayangan alien
    glBegin(GL_QUADS)
    glColor3ub(8, 46, 4)
    glVertex2f(320, 20)
    glVertex2f(380,20)
    glVertex2f(405,0)
    glVertex2f(345,0)
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
    alien()
    glutSwapBuffers() 

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1364, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("PESAWAT LUAR ANGKASA")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
