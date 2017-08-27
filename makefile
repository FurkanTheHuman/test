CC = cc
CFLAGS = -sdt=c99 -Wall
LFLAGS = -ledit -lm 

all: compile run

compile:
	 gcc  test.c -o lispy -ledit -lm  mpc.c -Wall -std=c99

run:
	./lispy



