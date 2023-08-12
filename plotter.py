import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

def make_movie():
    cmd='ffmpeg -framerate 5 -start_number 0 -i ./%05d.jpg -vcodec mpeg4 -vb 20M '+'movie.mp4'
    os.system(cmd)
    os.system("rm -r ./*.jpg")

def plot_projectile():
    data = pd.read_csv('data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    x=data[2]
    y=data[3]
    vx=data[4]
    vy=data[5]

    for frame in frames:
        fig=plt.figure(figsize=(25,20),facecolor='white')

        fig.suptitle(f"Time={t[int(frame)]:.3f}", fontsize=30)

        gs = fig.add_gridspec(2,4)
        ax1 = fig.add_subplot(gs[1, 0])
        ax2 = fig.add_subplot(gs[1, 1])
        ax3 = fig.add_subplot(gs[1, 2])
        ax4 = fig.add_subplot(gs[1, 3])
        ax5 = fig.add_subplot(gs[0, :])

        ax5.scatter(x[int(frame)],y[int(frame)],color='red',edgecolors='black',s=200)
        ax5.plot(x,y,'--k')
        ax5.set_xlabel("X-axis",fontsize=24)
        ax5.set_ylabel("Y-axis",fontsize=24)

        ax1.plot(t,x,'--k')
        ax1.scatter(t[int(frame)],x[int(frame)],color='red',edgecolors='black',s=200)
        ax1.set_xlabel("Time",fontsize=24)
        ax1.set_ylabel("X",fontsize=24)

        ax2.plot(t,y,'--k')
        ax2.scatter(t[int(frame)],y[int(frame)],color='red',edgecolors='black',s=200)
        ax2.set_xlabel("Time",fontsize=24)
        ax2.set_ylabel("Y",fontsize=24)

        ax3.plot(t,vx,'--k')
        ax3.scatter(t[int(frame)],vx[int(frame)],color='red',edgecolors='black',s=200)
        ax3.set_xlabel("Time",fontsize=24)
        ax3.set_ylabel("VX",fontsize=24)

        ax4.plot(t,vy,'--k')
        ax4.scatter(t[int(frame)],vy[int(frame)],color='red',edgecolors='black',s=200)
        ax4.set_xlabel("Time",fontsize=24)
        ax4.set_ylabel("VY",fontsize=24)

        plt.tight_layout()

        plt.savefig("{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()


def plot_simple_pendulum():
    data = pd.read_csv('data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    th=data[3]
    dth=data[4]
    x=data[5]
    y=data[6]
    k=data[7]
    p=data[8]

    for frame in frames:
        fig=plt.figure(figsize=(25,20),facecolor='white')

        fig.suptitle(f"Time={t[int(frame)]:.3f}", fontsize=30)

        gs = fig.add_gridspec(3,2)
        ax1 = fig.add_subplot(gs[0,0])
        ax2 = fig.add_subplot(gs[0,1])
        ax3 = fig.add_subplot(gs[1,0])
        ax4 = fig.add_subplot(gs[1,1])
        ax5 = fig.add_subplot(gs[2,0])
        ax6 = fig.add_subplot(gs[2,1])

        ax1.scatter(x[int(frame)],y[int(frame)],color='red',edgecolors='black',s=200)
        ax1.plot(x,y,'--k')
        ax1.plot([0,x[int(frame)]],[0,y[int(frame)]],'blue')
        ax1.set_xlabel("X-axis",fontsize=24)
        ax1.set_ylabel("Y-axis",fontsize=24)

        ax2.plot(t,th,'--k')
        ax2.scatter(t[int(frame)],th[int(frame)],color='red',edgecolors='black',s=200)
        ax2.set_xlabel("Time",fontsize=24)
        ax2.set_ylabel(r"$\theta$",fontsize=24)

        ax3.plot(t,dth,'--k')
        ax3.scatter(t[int(frame)],dth[int(frame)],color='red',edgecolors='black',s=200)
        ax3.set_xlabel("Time",fontsize=24)
        ax3.set_ylabel(r"$\dot{\theta}$",fontsize=24)

        ax4.plot(t,k,'--k')
        ax4.scatter(t[int(frame)],k[int(frame)],color='red',edgecolors='black',s=200)
        ax4.set_xlabel("Time",fontsize=24)
        ax4.set_ylabel("KE",fontsize=24)

        ax5.plot(t,p,'--k')
        ax5.scatter(t[int(frame)],p[int(frame)],color='red',edgecolors='black',s=200)
        ax5.set_xlabel("Time",fontsize=24)
        ax5.set_ylabel("PE",fontsize=24)

        ax6.plot(th,dth,'--k')
        ax6.scatter(th[int(frame)],dth[int(frame)],color='red',edgecolors='black',s=200)
        ax6.set_xlabel(r"$\theta$",fontsize=24)
        ax6.set_ylabel(r"$\dot{\theta}$",fontsize=24)

        plt.tight_layout()

        plt.savefig("{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()

def plot_spring_block():
    data = pd.read_csv('data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    x0=data[2]
    x=data[3]
    y=data[4]
    vx=data[5]
    k=data[6]
    p=data[7]

    for frame in frames:
        fig=plt.figure(figsize=(25,20),facecolor='white')

        fig.suptitle(f"Time={t[int(frame)]:.3f}", fontsize=30)

        gs = fig.add_gridspec(3,2)
        ax1 = fig.add_subplot(gs[0,0])
        ax2 = fig.add_subplot(gs[0,1])
        ax3 = fig.add_subplot(gs[1,0])
        ax4 = fig.add_subplot(gs[1,1])
        ax5 = fig.add_subplot(gs[2,0])
        ax6 = fig.add_subplot(gs[2,1])

        ax1.plot([0,x[int(frame)]+x0[int(frame)]],[0,y[int(frame)]],'blue')
        ax1.scatter(x[int(frame)]+x0[int(frame)],y[int(frame)],color='red',edgecolors='black',s=200,marker='s')
        #ax1.plot(x,y,'--k')
        ax1.set_xlim([-1+np.min(x),1+np.max(x)])
        ax1.set_xlabel("X-axis",fontsize=24)
        ax1.set_ylabel("Y-axis",fontsize=24)

        ax2.plot(t,x,'--k')
        ax2.scatter(t[int(frame)],x[int(frame)],color='red',edgecolors='black',s=200)
        ax2.set_xlabel("Time",fontsize=24)
        ax2.set_ylabel("X",fontsize=24)

        ax3.plot(t,vx,'--k')
        ax3.scatter(t[int(frame)],vx[int(frame)],color='red',edgecolors='black',s=200)
        ax3.set_xlabel("Time",fontsize=24)
        ax3.set_ylabel("VX",fontsize=24)

        ax4.plot(t,k,'--k')
        ax4.scatter(t[int(frame)],k[int(frame)],color='red',edgecolors='black',s=200)
        ax4.set_xlabel("Time",fontsize=24)
        ax4.set_ylabel("KE",fontsize=24)

        ax5.plot(t,p,'--k')
        ax5.scatter(t[int(frame)],p[int(frame)],color='red',edgecolors='black',s=200)
        ax5.set_xlabel("Time",fontsize=24)
        ax5.set_ylabel("PE",fontsize=24)

        ax6.plot(x,vx,'--k')
        ax6.scatter(x[int(frame)],vx[int(frame)],color='red',edgecolors='black',s=200)
        ax6.set_xlabel("X",fontsize=24)
        ax6.set_ylabel("VX",fontsize=24)

        plt.tight_layout()

        plt.savefig("{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()