from math import sqrt
import matplotlib.pyplot as plt
from numpy import arange


while True :
    print("f est une fontion trinôme du second degré tel que f(x)=ax² + bx + c")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    
    
    if a == 0 and b != 0 :
        x_list = arange( -50 , 50 , 0.001 )
        racine_0 = ( (-1)*c )/b
        print("\n\n")
        print("f(x)="+str(b)+"x+"+str(c)+"\n ")
        print("f(x)=0 <=> x="+str(racine_0)+"\n ")
        print("\n\n")

    elif a == 0 and b == 0 :
        x_list = arange( -50 , 50 , 0.001 )
        print("\n\n")
        print("f(x)="+str(c))
        print("\n\n")

        
    else :
        alpha = ( (-1)*b ) / 2*a
        beta = a*(alpha**2) + b*alpha + c
        delta = b**2 -(4*a*c)
        x_list = arange( alpha-200.0 , alpha+200.0 , 0.001 )
    
        if delta > 0 :
            racine_1 = ( (-1)*b - sqrt(delta) ) / 2*a
            racine_2 = ( (-1)*b + sqrt(delta) ) / 2*a
            print("\n\n")
            print("alpha="+str(alpha)+"    beta="+str(beta)+"    delta="+str(delta)+"    x1="+str(racine_1)+"    x2="+str(racine_2)+"\n ")
            print("f(x)="+str(a)+"x²+("+str(b)+")x+("+str(c)+")\n ")
            print("f(x)="+str(a)+"(x-("+str(alpha)+"))²+("+str(beta)+")\n ")
            print("f(x)="+str(a)+"(x-("+str(racine_1)+"))(x-("+str(racine_2)+"))\n ")
            print("f(x)=0 <=> x="+str(racine_1)+" ou x="+str(racine_2))
            print("\n\n")
    
            
        elif delta == 0 :
            racine_0 = ( (-1)*b ) / 2*a
            print("\n\n")
            print("alpha="+str(alpha)+"    beta="+str(beta)+"    delta="+str(delta)+"    x0="+str(racine_0)+"\n ")
            print("f(x)="+str(a)+"x²+("+str(b)+")x+("+str(c)+")\n ")
            print("f(x)="+str(a)+"(x-("+str(alpha)+"))²+("+str(beta)+")\n ")
            print("f(x)="+str(a)+"(x-("+str(racine_0)+"))\n ")
            print("f(x)=0 <=> x="+str(racine_0))
            print("\n\n")
    
            
        elif delta < 0 :
            print("\n\n")
            print("alpha="+str(alpha)+"    beta="+str(beta)+"    delta="+str(delta)+"    il n'existe pas de racine réelle\n ")
            print("f(x)="+str(a)+"x²+"+str(b)+"x+"+str(c)+"\n ")
            print("f(x)="+str(a)+"(x-("+str(alpha)+"))²+("+str(beta)+")\n ")
            print("f(x)≠0")
            print("\n\n")
        
        
    y = [  a*x**(2)+b*x+c for x in x_list  ]
        
    plt.plot(x_list,y,color="purple")
    plt.grid()
    plt.xlabel("X",color="blue")
    plt.ylabel("Y",color="blue")
    plt.title("fonction polynôme du second degré",color="red")
    plt.show()