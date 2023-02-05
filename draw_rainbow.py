import turtle
#renkler belirlendi
colors= ['red','orange','yellow','green','blue','dark blue','purple']
#Pen()= metodu ile çizim gerçekleştirildi
t= turtle.Pen()
#arkaplan belirlendi
turtle.bgcolor('black')
#Çizim hızı belirlendi
t.speed(50)
#Döngü ile çizim sürekli hale getirildi
for x in range(200):
#7 renk olduğu için mod 7 uygulandı
        t.pencolor(colors[x%7])
#Çizim kalınlığı belirlendi
        t.width(x/100+1)
#Çizim başlama noktası
        t.forward(x)
#dönüş açısı belirlendi
        t.left(52)
#turtle.hideturtle()
#Çizim bittiğinde ekranın kapanmamasını sağlar
turtle.mainloop()
