#!/usr/bin/env python3
import prompt


def welcome_user():
    user_name = prompt.string("Welcome to the Brain Games! \n"
                              "May I have your name? ")
    print(f"Hello, {user_name}!")
