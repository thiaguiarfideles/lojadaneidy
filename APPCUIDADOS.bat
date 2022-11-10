@echo off
start "Chrome" chrome --new-window http://127.0.0.1:8090/
location.reload()
@echo on
call C:\Users\thiago.fideles\Documents\lojadaneidy\myenv\Scripts\activate
call python C:\Users\thiago.fideles\Documents\lojadaneidy\manage.py runserver 8090
