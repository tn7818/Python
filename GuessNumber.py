#!/usr/bin/python
#coding=utf-8


number = 7
guess = -1

print ('Guess The Number !');
while guess != number:
	guess = int(input("Is It ......"))
	
	if guess == number:
		print('Hooray! You guessed it right !');
	elif guess < number:
		print("It's bigger...");
	elif guess > number:
	    print("It's not so big !");
