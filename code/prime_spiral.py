import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

n = 2026

def isPrime(n):
   if n == 1 or n % 2 == 0:
       return False 
   for i in range(2, int(np.sqrt(n))):
      if n % i == 0:
        return False 
   return True

def get_primes(num):
   primes = [2] 
   i, count = 1, 1
   while(count != num):
      if isPrime(i):
        primes.append(i)
        count = count + 1
      i = i + 1
   return primes

# get polar co-ordinates for (r, θ)
# both r and θ are taken as prime (p, p)
# hence, polar co-ordinates are:
# p.cos(p), p.sin(p) [θ in rad]

def get_polars(n):
   return n * np.cos(n), n * np.sin(n)

# plot the prime spiral
def plot_primes(num):
   # numpy broadcasting
   primes = np.array(get_primes(num))
   x, y = get_polars(primes)
   plt.figure(figsize = (7, 7))
   rest = plt.scatter(x, y, s = 1, label='')
   
   plast = plt.scatter(x[n-1], y[n-1], color='yellow', s=5, label=f'Prime {n}: {primes[n-1]}')
#    plt.legend(handles=[plast], loc='lower right', fontsize=11)
   plt.axis("off")
   plt.tight_layout()
#    plt.title(f"{n} prime numbers in a spiral!", size=20)
   plt.savefig("../assets/imgs/prime_spiral.png")
   plt.show()
   

plot_primes(n)
