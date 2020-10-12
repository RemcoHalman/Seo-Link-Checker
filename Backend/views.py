import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect

load_dotenv()

def home():
    return "Hello World"