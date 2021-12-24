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
    queue = []
    tampilan =  ["_" for i in range(size)]  
    print("Q =",'[ %s ]' % ' , '.join(map(str, tampilan)))
    print("FRONT(Q) = NULL")#Karena masih hampa, front = null
    print("REAR(Q)  = NULL") #karena masih hampa, rear = null
    print(f"NOEL(Q)  = {len(queue)}\n")#Ngitung panjang queue
  
  
def insert(q):
  global rear
  global size
  global indeks
  global noel
  if len(queue) == size:
    print("OVERFLOW\n")
  else:
    queue.append([q, indeks+1])
    tampilan[indeks] = q
    indeks += 1
    print("Q =",'[ %s ]' % ' , '.join(map(str, tampilan)))
    # [a,1] = a,1 = 3
    # [1:4] 1 sampe 4
    # a,1
    # print(f"FRONT(Q) = {((queue[0]))[1:4]}")
    rear = len(queue)-1 #Dikurang 1 supaya hasilnya sesuai dengan queuenya (list)
    print(f"FRONT(Q) = {queue[0][0]},{queue[0][1]}")#Front (A) tetap 0, terus front(elemen) indeksnya dimulai dari 1
    print(f"REAR(Q)  = {queue[rear][0]},{queue[rear][1]}")#Rear (A) berkurang 1, terus rear(elemen) indeksnya  1
    print(f"NOEL(Q)  = {len(queue)}\n")#Ngitung panjang queue

    if (indeks == size):
        indeks = 0
  

def remove():
  global front  
  global rear
  global size
  global indeks
  global tampilan
  if len(queue) == 0:
    print("UNDERFLOW\n")
  else:
    queue.pop(0)
    rear -= 1
    tampilan[front] = "_"
    front += 1 
    if front == size:
        front = 0
    print("Q =",'[ %s ]' % ' , '.join(map(str, tampilan)))
    if len(queue) == 0:
        print(f"FRONT(Q) = NULL")
        print(f"REAR(Q)  = NULL")
        print(f"NOEL(Q)  = {len(queue)}\n")
    else:
        print(f"FRONT(Q) = {queue[0][0]},{queue[0][1]}")#Front (A) tetap 0, terus front(elemen) indeksnya dimulai dari 1
        print(f"REAR(Q)  = {queue[rear][0]},{queue[rear][1]}")#Rear (A) berkurang 1, terus rear(elemen) indeksnya  1
        print(f"NOEL(Q)  = {len(queue)}\n")#Ngitung panjang queue
  

def isempty(q):
  global queue
  global rear
  if len(queue) == 0:
    print("(TRUE) Queue ini kosong/Hampa : ")
    print("Q =",'[ %s ]' % ' , '.join(map(str, tampilan)))
    print("FRONT(Q) = NULL")
    print("REAR(Q)  = NULL")
    print(f"NOEL(Q) = {len(queue)}\n")   
  else:
    print("(FALSE) Queue ini tidak kosong/hampa : ")
    print("Q =",'[ %s ]' % ' , '.join(map(str, tampilan)))
    print(f"FRONT(Q) = {queue[0][0]},{queue[0][1]}")
    print(f"REAR(Q)  = {queue[rear][0]},{queue[rear][1]}")
    print(f"NOEL(Q)  = {len(queue)}\n")

print('==========================')
print('========  QUEUE  =========')
print('==========================\n')

print("1. Membuat Queue Kosong")#queue kosong
print("2. Membuat Queue Terisi")#queue terisi penuh otomatis
print("3. Mmebuat Queue Bebas/Acak")#menginput manual elemen queue
input1=int(input("Pilihan : "))
if input1 == 1 :
  size = int(input("\nMasukkan Ukuran Queue: "))
  if size == 0:
      print("Queue tidak boleh memiliki ukuran 0!\n")
  else:
      queue = []
      tampilan =  ["_" for i in range(size)]
      print("\nQ =",'[ %s ]' % ' , '.join(map(str, tampilan)))
      print("FRONT(Q) = NULL")
      print("REAR(Q)  = NULL")
      print(f"NOEL(Q) = {len(queue)}\n")
elif input1 == 2 :
  asci1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  size = int(input("\nMasukkan Ukuran Queue: "))
  if size == 0:
      print("Queue tidak boleh memiliki ukuran 0!\n")
  else:
      queue = []
      tampilan = ["_" for i in range(size)]
      for i in range(size):
          queue.append([asci1[i], i + 1])
          tampilan[i] = asci1[i]

      print("Queue telah dibuat")
      print("Q =", '[ %s ]' % ' , '.join(map(str, tampilan)))
      print(
          f"FRONT(Q) = {queue[0][0]},{queue[0][1]}")  # Front (A) tetap 0, terus front(elemen) indeksnya dimulai dari 1
      print(
          f"REAR(Q)  = {queue[-1][0]},{queue[-1][1]}")  # Rear (A) berkurang 1, terus rear(elemen) indeksnya  1
      print(f"NOEL(Q)  = {len(queue)}\n")  # Ngitung panjang queue
else:
    size = int(input("\nMasukkan Ukuran Queue: "))
    if size == 0:
        print("Queue tidak boleh memiliki ukuran 0!\n")
    else:
        queue = []
        tampilan =  ["_" for i in range(size)] 
        while (len(queue) < size):
            print("Masukkan elemen ke-",len(queue)+1," : ")
            inp = input()
            if (inp == "_"):
                break
            else:
                queue.append([inp, indeks+1])
                tampilan[indeks] = inp
                indeks += 1
                rear = len(queue)-1
        if len(queue) == 0:
            print("\nQ =",'[ %s ]' % ' , '.join(map(str, tampilan)))
            print("FRONT(Q) = NULL")
            print("REAR(Q)  = NULL")
            print(f"NOEL(Q) = {len(queue)}\n")   
        else:
            print("\nQ =",'[ %s ]' % ' , '.join(map(str, tampilan)))
            print(f"FRONT(Q) = {queue[0][0]},{queue[0][1]}")
            print(f"REAR(Q)  = {queue[rear][0]},{queue[rear][1]}")
            print(f"NOEL(Q)  = {len(queue)}\n")
while inp_menu == True:
  print("======MENU======\n|  1. CREATE   |")
  print("|  2. ISEMPTY  |")
  print("|  3. INSERT   |")
  print("|  4. REMOVE   |")
  print("|  5. KELUAR   |\n================")
  opsi = int(input("Masukkan operasi yang diinginkan: "))

  if (opsi == 1) :
    create()
  elif (opsi == 2) :
    isempty(queue)
  elif (opsi == 3) :
    inp = input("Masukkan elemen: ")
    insert(inp)
  elif (opsi == 4) :
    remove()
  else :
    inp_menu = False 
    print("Anda keluar dari program...") 



