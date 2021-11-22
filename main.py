#Placeholder
inp_menu = True
size = 0
rear = 0
front = 0
capacity = 0
queue = []
tampilan = []
indeks = 0
noel = 0

def create():
  global queue
  global size
  global tampilan
  size = int(input("Ukuran Queue: "))
  queue = []
  tampilan = Q = ["_" for i in range(size)] 
  print("Queue telah dibuat") 
  print(tampilan)
  

def insert(q):
  global front
  global rear
  global size
  global indeks
  global noel
  if len(queue) == size:
    print("OVERFLOW")
  else:
    queue.append([q, indeks+1])
    tampilan[indeks] = q
    indeks += 1
    print(tampilan)
    # [a,1] = a,1 = 3
    # [1:4] 1 sampe 4
    # a,1
    # print(f"FRONT(Q) = {((queue[0]))[1:4]}")
    rear = len(queue)-1 #Dikurang 1 supaya hasilnya sesuai dengan queuenya (list)
    print(f"FRONT(Q) = {queue[0][0]},{queue[0][1]}")#Front (A) tetap 0, terus front(elemen) indeksnya dimulai dari 1
    print(f"REAR(Q) = {queue[rear][0]},{queue[rear][1]}")#Rear (A) berkurang 1, terus rear(elemen) indeksnya  1
    print(f"NOEL(Q) = {len(queue)}")#Ngitung panjang queue
    print("\n")

    if (indeks == size):
        indeks = 0
  

def remove():
  global front  
  global rear
  global size
  global indeks
  global noel
  global tampilan
  if len(queue) == 0:
    print("UNDERFLOW")
  else:
    queue.pop(0)
    rear -= 1
    tampilan[front] = "_"
    front += 1 
    if front == size:
        front = 0
    print(tampilan) 
    #Kondisi array sirkular (remove)
    if len(queue) == 0:
        print(f"FRONT(Q) = NULL")
        print(f"REAR(Q) = NULL")
        print(f"NOEL(Q) = {len(queue)}")
    else:
        print(f"FRONT(Q) = {queue[0][0]},{queue[0][1]}")#Front (A) tetap 0, terus front(elemen) indeksnya dimulai dari 1
        print(f"REAR(Q) = {queue[rear][0]},{queue[rear][1]}")#Rear (A) berkurang 1, terus rear(elemen) indeksnya  1
        print(f"NOEL(Q) = {len(queue)}")#Ngitung panjang queue
  

def isempty(q):
  global queue
  print(tampilan)
  if len(queue) == 0:
    print("Queue ini kosong/Hampa")
  else:
    print("Queue ini tidak kosong/hampa")

print('==========================')
print('========  QUEUE  =========')
print('==========================')

while inp_menu == True:
  print("\n1. CREATE")
  print("2. INSERT")
  print("3. REMOVE")
  print("4. ISEMPTY")
  print("5. Keluar")
  opsi = int(input("Masukkan operasi yang diinginkan: "))

  if (opsi == 1) :
    create()
  elif (opsi == 2) :
    inp = input("Masukkan elemen: ")
    insert(inp)
  elif (opsi == 3) :
    remove()
  elif (opsi == 4) :
    isempty(queue)  
  else :
    inp_menu = False  
