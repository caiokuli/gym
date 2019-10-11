import gym
import random
import threading


def thread_render(env):
    for i in range(10000):
        env.reset()
        env.render()
def thread_bot_controlangle(bot):
    for i in range(10000):
        bot.controlangle()


class Agent():
    def __init__(self,observation):
        self.observation = observation


    def controlangle(self):
        if(self.observation[2] > 0 ):
            self.observation,b,c,d = env.step(1)
        if(self.observation[2] < 0):
            self.observation,b,c,d = env.step(0)
        print(self.observation[2])
        env.reset()

    def controlspeed(self):
        if(self.observation[1] < -2 ):
            self.observation,b,c,d = env.step(1)

        if(self.observation[1] > 2 ):
           self.observation,b,c,d = env.step(0)


    def control(self):
        self.controlspeed()
        #self.controlangle()
        x = threading.Thread(target=self.controlangle, args=(env,))
        x.start
        if(self.observation[0] > 0 ):
            self.observation,b,c,d = env.step(0)
        else:
            self.observation,b,c,d = env.step(1)
        env.reset()



env = gym.make('CartPole-v0')
env.reset()
a,b,c,d = env.step(env.action_space.sample())
bot = Agent(a)



for i in range(10000):
    env.render()
    bot.control()
