#!/bin/sh

mkfifo foo

./game.py < foo | ./game_solver.py > foo

rm foo
