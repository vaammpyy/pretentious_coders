from solver import *
from plotter import *

def projectile_motion(v,theta,h,dt,t_end):
    projectile(v,theta,h,dt,t_end)
    plot_projectile()
    make_movie()

def single_pendulum_motion(m,l,th,dth,r,dt,t_end):
    simple_pendulum(m,l,th,dth,r,dt,t_end)
    plot_simple_pendulum()
    make_movie()

def spring_block_motion(m,ks,x0,x,vx,mu,dt,t_end):
    spring_block(m,ks,x0,x,vx,mu,dt,t_end)
    plot_spring_block()
    make_movie()

spring_block_motion(1,10,0,2,0,0,0.1,5)
