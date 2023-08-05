import random


def run_guess( n,nums):
    if 0<n<11:
        if n==nums:
            print("you are correct")
            return True
    else:
        print("you are wrong")
        return False
    
#print(nums)
if __name__=="__main__":
    nums=random.randint(1,10)

    while True:
        try:
            n=int(input("Enter the number :"))
            if (run_guess(n,nums)):
                break
            
        except ValueError:
            print("Please Enter the number")
            continue
        