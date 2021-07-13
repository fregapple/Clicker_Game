import pygame
from classes import *


# These functions do the Math on Upgrades / Quantites..

def GPUs():
    sc.score = sc.score + (gv.gpu * gv.gpus)
    sc.__call__()

def CLICKs():
    sc.score = sc.score + (clv.click * clv.clicks)
    sc.__call__()

